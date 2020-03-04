from typing import List
import os
import sys
import zipfile
import omg

PROGRAM_NAME = os.path.basename(sys.argv[0]).rsplit(".", 1)[0]


class NoMapInWADException(Exception):
	"""No UDMF maps found in WAD"""
	pass


class NoMapHeaderForTextmapException(Exception):
	"""TEXTMAP has no corresponding map header entry"""
	pass


class MapEntry:
	"""
	A class that encapsulates a WadIO reference, a corresponding WadIO Entry (TEXTMAP entry), and a name of this map.
	"""

	def __init__(self, wadio: omg.WadIO, entry, name: str):
		self.wadio: omg.WadIO = wadio
		self.entry = entry
		self.name: str = name
		pass

	@property
	def textmap(self) -> str:
		return self.get_textmap()

	def get_textmap(self) -> str:
		lastoffs = self.wadio.basefile.tell()

		self.wadio.basefile.seek(self.entry.ptr)
		textmap = self.wadio.basefile.read(self.entry.size).decode("utf-8")
		self.wadio.basefile.seek(lastoffs)

		return textmap


# okay i know this is pretty gross but i literally had to rewrite omg.WadIO.open() to accept zipfile.ZipExtFile objects
def wadio_from_zip_entry(zip_entry: zipfile.ZipExtFile) -> omg.WadIO:
	wadio: omg.WadIO = omg.WadIO()
	wadio.basefile = zip_entry

	data = zip_entry.read()
	filesize = len(data)
	header = omg.wadio.Header(bytes=data[:omg.wadio.Header._fmtsize])
	if header.type not in ("PWAD", "IWAD") or filesize < 12:
		raise IOError("wadio_from_zip_entry: The file is not a valid WAD file.")
	if filesize < header.dir_ptr + header.dir_len * omg.wadio.Entry._fmtsize:
		raise IOError("wadio_from_zip_entry: Invalid directory information in header.")
	wadio.basefile.seek(header.dir_ptr)
	wadio.entries = [omg.wadio.Entry(bytes=wadio.basefile.read(omg.wadio.Entry._fmtsize)) for i in range(header.dir_len)]

	return wadio


def next_wad_from_zip(path_to_zip: str, pwd=None):
	zip_file = zipfile.ZipFile(path_to_zip, "r")

	for name in zip_file.namelist():
		name_ext = os.path.basename(name).rsplit(".", 1)
		if isinstance(name_ext, list):
			name_ext = name_ext[-1]

			if name_ext == "wad":
				yield wadio_from_zip_entry(zip_file.open(name, "r", pwd))

	zip_file.close()
	pass


def next_map_entry_from_wad(wadio: omg.WadIO):
	textmap_entry_nums: List[int] = wadio.multifind("TEXTMAP")

	if len(textmap_entry_nums) == 0:
		raise NoMapInWADException(
			"\"" + os.path.basename(wadio.basefile.name) + "\"" + " does not contain any UDMF maps")

	for entrynum in textmap_entry_nums:
		if entrynum - 1 < 0 and wadio.entries[entrynum - 1].size != 0:
			raise NoMapHeaderForTextmapException(
				"\"" + wadio.basefile.name + "\""
				+ " contains a TEXTMAP that does not have a corresponding map header")

		map_entry_name: str = os.path.basename(wadio.basefile.name) + "/" + wadio.entries[entrynum - 1].name

		yield MapEntry(wadio, wadio.entries[entrynum], map_entry_name)

	pass
