from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import curses

import numpy as np

import sys

from pycolab import ascii_art
from pycolab import human_ui
from pycolab import rendering
from pycolab import things as plab_things
from pycolab.prefab_parts import sprites as prefab_sprites

WAREHOUSES_ART = [
    # Legend:
    #     '#': impassable walls.            '.': outdoor scenery.
    #     '_': goal locations for boxes.    'P': player starting location.
    #     '0'-'9': box starting locations.  ' ': boring old warehouse floor.

    ['..........',
     '..######..',     # Map #0, "Tyro"
     '..#  _ #..',
     '.##12 ##..',     # In this map, all of the sprites have the same thing
     '.#  _3 #..',     # underneath them: regular warehouse floor (' ').
     '.#_  4P#..',     # (Contrast with Map #1.) This allows us to use just a
     '.#_######.',     # single character as the what_lies_beneath argument to
     '.# # ## #.',     # ascii_art_to_game.
     '.# 5  _ #.',
     '.########.',
     '..........']]

WAREHOUSES_ART = [

 ['............_.................',
  '._............................',
  '..............................',
  '.........................P....',
  '..............................',
  '..P...........................',
  '..............................',
  '..............................',
  '..............................',
  '.........................._...',
  '..............................',
  '..............................',
  '....P.........................']]

