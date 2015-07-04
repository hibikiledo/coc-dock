__author__ = 'Hibiki'

# import our wrapper modules
import adb_wrapper as adb
import matlab_wrapper as matlab

# Good to have utils !
from utils import group_points

# Import our model
from models import Point

from os import listdir
import csv
import time
import threading

# DEFINE PATHS
TEMPLATE_PATH = 'templates'
TEMP_PATH = 'temp'

# Initialize the game
adb.init()

raw_input("Is Game Ready ? [Y/n] ")

# Have a list contaning references to threads
thread_ref = []

# Capture current screen
adb.screenshot('screenshots/coc.png')

# Perform preprocessing
matlab.preprocess('coc.png', 'coc.bmp')


# Iterate through each template and allocate a thread for each template
# This allow concurrent matching for each result type
for template in listdir(TEMPLATE_PATH):

    if template in [".DS_Store", "unused"]:
        continue

    # create new thread
    t = threading.Thread(target=matlab.locateres, args=('coc.bmp', template, 'coc-{}.out'.format(template)))
    # keep the reference
    thread_ref.append(t)
    # start the thread
    t.start()


# Wait for all thread to finish before continue
for t in thread_ref:
    t.join()

# Read output of matlab script (in temp folder) as list of points
points = []
for output_file in listdir((TEMP_PATH)):
    # open file
    with open('/'.join([TEMP_PATH, output_file]), 'rb') as of:
        # get reader
        reader = csv.reader(of, delimiter=':')
        # create new Point instance and keep in a list
        for rec in reader:
            points.append(Point(rec[0], rec[1]))

print "[INFO] List of points before grouping"
for p in points:
    print "     %-5d : %-5d" % (p.x, p.y)

# Perform point grouping
grouped_points = group_points(points)

print "[INFO] List of points after grouping"
for p in grouped_points:
     print "     %-5d : %-5d" % (p.x, p.y)

# Tap according to groupped points
for p in grouped_points:
    print "[INFO] Tapping at", "%-5d : %-5d" % (p.x, p.y)
    adb.tap(p.x, p.y)





