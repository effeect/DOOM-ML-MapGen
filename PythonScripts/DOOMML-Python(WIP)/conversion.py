# Written by Oliver Dimes

# Thanks to https://www.vipinajayakumar.com/parsing-text-with-python/ and https://stackoverflow.com/questions/51345024/read-text-file-and-parse-in-python/51345210#51345210
import re
#These are all of the types of parameters we could possbily have
linedefParas = ["BLOCKING",
    "BLOCKMONSTERS",
    "TWOSIDED",
    "DONTPEGTOP",
    "DONTPEGBOTTOM",
    "SECRET",
    "SOUNDBLOCK",
    "DONTDRAW",
    "MAPPED",
    "RAILING",
    "PASSUSE",
    "REPEAT_SPECIAL",
    "BLOCK_FLOATERS",
    "THREEDMIDTEX",
    "SPAC_Use",
    "SPAC_MCross",
    "SPAC_Impact",
    "SPAC_Push",
    "SPAC_PCross",
    "SPAC_UseThrough",
    "TRANSLUCENT",
    "MONSTERSCANACTIVATE",
    "BLOCK_PLAYERS",
    "BLOCKEVERYTHING",
    "SPAC_Cross",
    "SPAC_AnyCross",
    "SPAC_MUse",
    "SPAC_MPush",
    "FIRSTSIDEONLY",
    "ZONEBOUNDARY",
    "CLIP_MIDTEX",
    "WRAP_MIDTEX",
    "CHECKSWITCHRANGE",
    "BLOCKPROJECTILE",
    "BLOCKUSE",
    "BLOCKSIGHT",
    "BLOCKHITSCAN",
    "ThreeDMIDTEX_IMPASS"]
sidedefParas = ["alpha",
    "clipmidtex",
    "comment",
    "light",
    "lightabsolute",
    "lightfog",
    "nodecals",
    "nofakecontrast",
    "offsetx_bottom",
    "offsetx_mid",
    "offsetx_top",
    "offsetx",
    "offsety_bottom",
    "offsety_mid",
    "offsety_top",
    "offsety",
    "scalex_bottom",
    "scalex_mid",
    "scalex_top",
    "scaley_bottom",
    "scaley_mid",
    "scaley_top",
    "sector",
    "smoothlighting",
    "texturebottom",
    "texturemiddle",
    "texturetop",
    "wrapmidtex" ]
vertexParas = ["x","y"]
sectorParas = ["xpanningfloor",
    "ypanningfloor",
    "xpanningceiling",
    "ypanningceiling",
    "xscalefloor",
    "yscalefloor",
    "xscaleceiling",
    "yscaleceiling",
    "rotationfloor",
    "rotationceiling",
    "ceilingplane_a",
    "ceilingplane_b",
    "ceilingplane_c",
    "ceilingplane_d",
    "floorplane_a",
    "floorplane_b",
    "floorplane_c",
    "floorplane_d",
    "lightfloor",
    "lightceiling",
    "lightfloorabsolute",
    "lightceilingabsolute",
    "alphafloor",
    "alphaceiling",
    "renderstylefloor",
    "renderstyleceiling",
    "gravity",
    "lightcolor",
    "fadecolor",
    "desaturation",
    "silent",
    "nofallingdamage",
    "dropactors",
    "norespawn",
    "soundsequence",
    "hidden",
    "waterzone",
    "moreids",
    "damageamount",
    "damagetype",
    "damageinterval",
    "leakiness",
    "damageterraineffect",
    "damagehazard",
    "floorterrain",
    "ceilingterrain",
    "portal_ceil_alpha",
    "portal_ceil_blocksound",
    "portal_ceil_disabled",
    "portal_ceil_nopass",
    "portal_ceil_norender",
    "portal_ceil_overlaytype",
    "portal_floor_alpha",
    "portal_floor_blocksound",
    "portal_floor_disabled",
    "portal_floor_nopass",
    "portal_floor_norender",
    "portal_floor_overlaytype",
    "noattack"]




def txtToJson(filename):  # This function is to convert a TEXTMAP doom file to useable JSON file with Pandas
    fin = open(filename, "rt")
    data = fin.read()

    #General things we can replace
    data = data.replace(';', ',')
    data = data.replace('=', ':')
    data = data.replace('}', '},')

    #Loops through lists to match words and change the paras to be JSON compliant
    for x in linedefParas :
        string = "\"%s\"" % x.lower()
        data = data.replace(x, string)
    for y in sidedefParas :
        string = "\"%s\"" % y
        data = data.replace(y, string)
    for z in vertexParas : #A serious thanks to Kevin on Stackoverflow for asking my question : https://stackoverflow.com/questions/59666022/how-do-i-manipulate-string-x-by-itself-without-mixing-it-in-other-strings/59666177#59666177
        data = re.sub(rf"\b{z}\b", lambda match: f'"{match.group()}"', data)
    for a in sectorParas :
        string = "\"%s\"" % a
        data = data.replace(a, string)


    fin.close() #Closing the python reader to avoid a memory leak

    fin = open(filename, "wt")
    fin.write(data)
    fin.close()
    print("Operation Complete")


def jsonToTxt(filename):  # This function is to put JSON back into TEXTMAP which allows for DOOM to run
    fin = open(filename, "rt")
    data = fin.read()
    data = data.replace(',', ';')
    data = data.replace(':', '=')
    fin.close()

    fin = open(filename, "wt")
    fin.write(data)
    fin.close()
    print("Operation Complete")


txtToJson("JSONData/TEXTMAPAgain.txt")