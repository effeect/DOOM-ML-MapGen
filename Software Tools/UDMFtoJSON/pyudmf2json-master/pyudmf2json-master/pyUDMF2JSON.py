#!/usr/bin/env python3

from typing import List

import os
import sys
import argparse
import zipfile
import json
import re

import omg
import UDMFParser
import pyUDMF2JSONUtils


def main(args: List[str]):
	parser = argparse.ArgumentParser(description="Converts UDMF text maps to JSON.")

	parser.add_argument(
		"input",
		help="Path to a WAD, a pk3, or a plain UDMF file."
	)

	parser.add_argument(
		"output",
		help="Path to output generated JSON files to.",
		nargs="?",
		default=os.getcwd()
	)

	parser.add_argument(
		"-m", "--maps",
		help="Pattern that specifies which maps to convert. NOTE: This pattern doesn't match WAD files, it instead"
		"matches the map markers in the WADs.",
		action="store"
	)

	parser.add_argument(
		"--no-key-name-correction",

		help="JSON keys have proper plural names for all recognized UDMF constructs"
		"(\"vertices\" instead of \"vertex_list\").",

		action="store_true"
	)

	parser.add_argument(
		"-i", "--indent-size",
		help="Specifies the length of the indentation size. Default is 4.",
		action="store",
		default=4
	)

	parser.add_argument(
		"-v", "--verbose",
		help="Report extra information.",
		action="store_true"
	)

	if len(args) == 0:
		parser.print_help()
		return

	namespace = parser.parse_args()

	if not os.path.exists(namespace.input):
		sys.stderr.write(pyUDMF2JSONUtils.PROGRAM_NAME + ": \"" + namespace.input + "\" does not exist." + os.sep)
		return

	if zipfile.is_zipfile(namespace.input):
		for w in pyUDMF2JSONUtils.next_wad_from_zip(namespace.input):
			do_wad(w, namespace)
	else:
		try:
			do_wad(omg.WadIO(namespace.input), namespace)
		except IOError:
			with open(namespace.input, "r") as f:
				UDMFParser.parse(f.read())

	pass


def do_wad(wadio: omg.WadIO, namespace):
	try:
		for m in pyUDMF2JSONUtils.next_map_entry_from_wad(wadio):
			do_textmap(m, namespace)

	except pyUDMF2JSONUtils.NoMapInWADException as nmiwe:
		if namespace.verbose:
			sys.stderr.write(pyUDMF2JSONUtils.PROGRAM_NAME + ": " + str(nmiwe) + "." + os.linesep)

	except pyUDMF2JSONUtils.NoMapHeaderForTextmapException as nmhfte:
		if namespace.verbose:
			sys.stderr.write(pyUDMF2JSONUtils.PROGRAM_NAME + ": " + str(nmhfte) + "." + os.linesep)

	pass


def do_textmap(map_entry: pyUDMF2JSONUtils.MapEntry, namespace):
	# output_directory/input_pk3_name/map_wad_name
	output_dir_path: str = namespace.output\
		+ os.sep + os.path.basename(namespace.input).rsplit(".", 1)[0]\
		+ os.sep + os.path.split(map_entry.name)[0].rsplit(".", 1)[0]

	map_pattern: str = ".*?"
	if namespace.maps:
		map_pattern = namespace.maps

	if re.search(map_pattern, map_entry.name):
		try:
			os.makedirs(output_dir_path)

			print(pyUDMF2JSONUtils.PROGRAM_NAME + ": Parsing " + map_entry.name + "...")

			output_file_path = output_dir_path + os.sep + os.path.basename(map_entry.name) + ".json"
			with open(output_file_path, "w") as f:
				f.write(json.dumps(UDMFParser.parse(map_entry.textmap, not namespace.no_key_name_correction), indent=namespace.indent_size))
				print(pyUDMF2JSONUtils.PROGRAM_NAME + ": Written to " + output_dir_path)
		except FileExistsError as fee:
			sys.stderr.write(pyUDMF2JSONUtils.PROGRAM_NAME + ": " + str(fee))
		except OSError as oe:
			sys.stderr.write(pyUDMF2JSONUtils.PROGRAM_NAME + ": " + str(oe))

	pass


if __name__ == "__main__":
	main(sys.argv[1:])
