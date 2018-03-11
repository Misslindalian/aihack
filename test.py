#!/usr/bin/python
# The contents of this file are in the public domain. See LICENSE_FOR_EXAMPLE_PROGRAMS.txt
#
# This example shows how to use the correlation_tracker from the dlib Python
# library.  This object lets you track the position of an object as it moves
# from frame to frame in a video sequence.  To use it, you give the
# correlation_tracker the bounding box of the object you want to track in the
# current video frame.  Then it will identify the location of the object in
# subsequent frames.
#
# In this particular example, we are going to run on the
# video sequence that comes with dlib, which can be found in the
# examples/video_frames folder.  This video shows a juice box sitting on a table
# and someone is waving the camera around.  The task is to track the position of
# the juice box as the camera moves around.
#
#
# COMPILING/INSTALLING THE DLIB PYTHON INTERFACE
#   You can install dlib using the command:
#       pip install dlib
#
#   Alternatively, if you want to compile dlib yourself then go into the dlib
#   root folder and run:
#       python setup.py install
#   or
#       python setup.py install --yes USE_AVX_INSTRUCTIONS
#   if you have a CPU that supports AVX instructions, since this makes some
#   things run faster.  
#
#   Compiling dlib should work on any operating system so long as you have
#   CMake installed.  On Ubuntu, this can be done easily by running the
#   command:
#       sudo apt-get install cmake
#
#   Also note that this example requires scikit-image which can be installed
#   via the command:
#       pip install scikit-image
#   Or downloaded from http://scikit-image.org/download.html. 

import os
import glob

import dlib
from skimage import io
import math

# from shapely.geometry import Polygon

def rectIntersection(a, b):
  dx = min(a.right(), b.right()) - max(a.left(), b.left())
  dy = min(a.bottom(), b.bottom()) - max(a.top(), b.top())
  if (dx>=0) and (dy>=0):
    intersection = dx * dy
    unionArea = (ra.xmax - ra.xmin) * (ra.ymax - ra.ymin) + (rb.xmax - rb.xmin) * (rb.ymax - rb.ymin) - intersection
    return intersection * 1.0 / unionArea
  # left = max(r1.left(), r2.left())
  # right = min(r1.right(), r2.right())
  # bottom = max(r1.bottom(), r2.bottom())
  # top = min(r1.top(), r2.top())
  # if left < right and bottom < top:
  #   intersection = (right - left) * (top - bottom)
  #   unionArea = ((r1.right() - r1.left()) * (r1.top() - r1.bottom())) + ((r2.right() - r2.left()) * (r2.top() - r2.bottom())) - intersection;
  #   return intersection * 1.0 / unionArea
  # else:
  #   return 0

from collections import namedtuple
Rectangle = namedtuple('Rectangle', 'xmin ymin xmax ymax')

ra = Rectangle(890, 319, 1012, 364)
rb = Rectangle(963, 324, 1066, 359)
# intersection here is (3, 3, 4, 3.5), or an area of 1*.5=.5

def area(a, b):  # returns None if rectangles don't intersect
    dx = min(a.xmax, b.xmax) - max(a.xmin, b.xmin)
    dy = min(a.ymax, b.ymax) - max(a.ymin, b.ymin)
    if (dx>=0) and (dy>=0):
        return dx*dy

print(area(ra, rb) )
# print( (ra.xmax - ra.xmin) * (ra.ymax - ra.ymin))
# print( (rb.xmax - rb.xmin) * (rb.ymax - rb.ymin))

a = dlib.rectangle( 890, 319, 1012, 364 )
b = dlib.rectangle( 963, 324, 1066, 359 )
print(rectIntersection(a, b) )


# dlib.rectangle(left: int, top: int, right: int, bottom: int)

# left, right, top, bot
# a = dlib.rectangle( 890, 319, 1012, 364 )
# b = dlib.rectangle( 963, 324, 1066, 359 )
# print(rectIntersection(a,b))

# print(a == b)
# print(a == a)