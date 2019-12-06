#Importing libraries, template from https://www.tensorflow.org/datasets/overview
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

#List of imports
import json
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import tensorflow_datasets as tfds

def jsonProcess(filename) :
    with open(filename) as f :
        data = json.load(f)
        x = np.array(data['xs'])
        y = np.array(data['ys'])

#List of functions for each element of the map 
#https://stackoverflow.com/questions/38381887/how-to-read-json-files-in-tensorflow

def get_linedefs():
    BLOCKING
    BLOCKMONSTERS
    TWOSIDED
    DONTPEGTOP
    DONTPEGBOTTOM
    SECRET
    SOUNDBLOCK
    DONTDRAW
    MAPPED
    RAILING
    PASSUSE
    REPEAT_SPECIAL
    BLOCK_FLOATERS
    THREEDMIDTEX
    SPAC_Use
    SPAC_MCross
    SPAC_Impact
    SPAC_Push
    SPAC_PCross
    SPAC_UseThrough
    TRANSLUCENT
    MONSTERSCANACTIVATE
    BLOCK_PLAYERS
    BLOCKEVERYTHING
    SPAC_Cross
    SPAC_AnyCross
    SPAC_MUse
    SPAC_MPush
    FIRSTSIDEONLY
    ZONEBOUNDARY
    CLIP_MIDTEX
    WRAP_MIDTEX
    CHECKSWITCHRANGE
    BLOCKPROJECTILE
    BLOCKUSE
    BLOCKSIGHT
    BLOCKHITSCAN
    ThreeDMIDTEX_IMPASS

def get_sidedefs():
    alpha
    clipmidtex
    comment
    light
    lightabsolute
    lightfog
    nodecals
    nofakecontrast
    offsetx_bottom
    offsetx_mid
    offsetx_top
    offsetx
    offsety_bottom
    offsety_mid
    offsety_top
    offsety
    scalex_bottom
    scalex_mid
    scalex_top
    scaley_bottom
    scaley_mid
    scaley_top
    sector
    smoothlighting
    texturebottom
    texturemiddle
    texturetop
    wrapmidtex

def get_vertexes():
    x
    y

def get_sectors():
    xpanningfloor
    ypanningfloor
    xpanningceiling
    ypanningceiling
    xscalefloor
    yscalefloor
    xscaleceiling
    yscaleceiling
    rotationfloor
    rotationceiling
    ceilingplane_a
    ceilingplane_b
    ceilingplane_c
    ceilingplane_d
    floorplane_a
    floorplane_b
    floorplane_c
    floorplane_d
    lightfloor
    lightceiling
    lightfloorabsolute
    lightceilingabsolute
    alphafloor
    alphaceiling
    renderstylefloor
    renderstyleceiling
    gravity
    lightcolor
    fadecolor
    desaturation
    silent
    nofallingdamage
    dropactors
    norespawn
    soundsequence
    hidden
    waterzone
    moreids
    damageamount
    damagetype
    damageinterval
    leakiness
    damageterraineffect
    damagehazard
    floorterrain
    ceilingterrain
    portal_ceil_alpha
    portal_ceil_blocksound
    portal_ceil_disabled
    portal_ceil_nopass
    portal_ceil_norender
    portal_ceil_overlaytype
    portal_floor_alpha
    portal_floor_blocksound
    portal_floor_disabled
    portal_floor_nopass
    portal_floor_norender
    portal_floor_overlaytype
    noattack

#def get_segs()
#def get_ssectors():
#def get_nodes
#def get_reject():
#def blockmap():