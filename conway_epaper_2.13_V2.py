#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13_V2
import time
from PIL import Image,ImageDraw,ImageFont,ImageOps
import traceback

import argparse
import random
import numpy as np
from datetime import datetime
import png

print("Im working")
time.sleep(30)

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-g', '--generation', action='store', type=int,
    help="Sets the max generation.")
my_parser.add_argument('-p', '--population', action='store', type=int,
    help="Percentage of times that random cells of life are added to based on board size.")
my_parser.add_argument('-s', '--sleep', action='store', type=int,
    help="Time that the program sleeps inbetween generations")
my_parser.add_argument('-d', '--delete', action='store_true',
    help="Flag used if you want the images of generations deleted when program is done running.")

# Sanity checks user inputs
args = my_parser.parse_args()

# Fills in default values if user did not define
height = 250
width = 122

if args.generation is None:
    maxgeneration = 250
else:
    maxgeneration = args.generation

if args.population is None:
    population = .2
else:
    population = args.population / 100

if args.sleep is None:
    sleep = 2
else:
    sleep = args.sleep

logging.basicConfig(level=logging.DEBUG)

path = os.getcwd()
isdir = os.path.isdir("temp")
np.random.seed(random.seed(datetime.now()))

# Generation 0
generation = 0
newtable = np.zeros((width,height))
oldtable = newtable

# Generation 1
# Randomly sets an intial state of living squares
for i in range(int(width * height * (population))):
    newtable[random.randint(0, width - 1 )][random.randint(0, height - 1 )] = 1

print(newtable)

def countNeighbors(oldtable,x,y):
    """Counts the living neighbors of a cell

    Args:
        oldtable: 
        x (int): cordanante of the starting cell
        y (int): coordinate of the starting cell

    Returns:
        int: count of the neighbors

    """
    temp = 1

    count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if not (i==0 and j==0):  #TODO: this needs rewritin to be more understandable
                count += int(oldtable[(x + i + width) % width][(y + j + height) % height])

    for i in range(-1,2):
        for j in range(-1,2):
            temp += 1

    count -= int(oldtable[x][y])

    return count

if isdir == False:
    os.mkdir("temp")

epd = epd2in13_V2.EPD()
logging.info("init and Clear")
epd.init(epd.FULL_UPDATE)

logging.info("Conways Game of life on wave share 2.13in e-Paper")

while True:
    # epd.Clear(0xFF)
    logging.info("Clear Screen")
    #epd.init(epd.FULL_UPDATE)
    #epd.Clear(0xFF)

    oldtable = newtable

    #np.invert(newtable)
    binary_transform = np.array(newtable).astype(np.uint8)
    binary_transform[binary_transform>0] = 255    
    img = Image.fromarray(binary_transform, 'P')
    img.save('image.bmp')

    image = Image.open(os.path.join("image.bmp"))
    epd.display(epd.getbuffer(image))

    # Calculates the state of the next generation
    for x in range(width):
        for y in range(height):
            neighbors =  countNeighbors(oldtable,x,y)
            # Calculate dead cells
            if oldtable[x][y] == 0 and neighbors == 3:
                newtable[x][y] = 1
            # Calculate alive cells
            elif oldtable[x][y] == 1 and (neighbors < 2 or neighbors > 3):
                newtable[x][y] = 0

    #print("Generation: ", generation)
    generation +=1

    if generation > maxgeneration:
        break

    #time.sleep(2)

"""
try:
    
    epd = epd2in13_V2.EPD()
    logging.info("init and Clear")
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)
    
    # read bmp file 
    logging.info("2.read bmp file...")
    image = Image.open(os.path.join(picdir, '2in13.bmp'))
    epd.display(epd.getbuffer(image))
    time.sleep(2)
"""

"""
    # read bmp file on window
    logging.info("3.read bmp file on window...")
    # epd.Clear(0xFF)
    image1 = Image.new('1', (epd.height, epd.width), 255)  # 255: clear the frame
    bmp = Image.open(os.path.join(picdir, '100x100.bmp'))
    image1.paste(bmp, (2,2))    
    epd.display(epd.getbuffer(image1))
    time.sleep(2)
"""
    
# epd.Clear(0xFF)
logging.info("Clear...")
epd.init(epd.FULL_UPDATE)
epd.Clear(0xFF)

logging.info("Goto Sleep...")
epd.sleep()
        
"""
except IOError as e:
    logging.info(e)

    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd2in13_V2.epdconfig.module_exit()
    exit()
"""
