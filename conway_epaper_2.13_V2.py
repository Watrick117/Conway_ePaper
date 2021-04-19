#!/usr/bin/python
import sys
import os

libdir = os.path.join(os.path.dirname(os.path.dirname(
         os.path.realpath(__file__))), 'lib')

if os.path.exists(libdir):
    sys.path.append(libdir)

from waveshare_epd import epd2in13_V2
import time
from PIL import Image, ImageDraw, ImageFont
import traceback
import argparse
import random
import numpy as np
from datetime import datetime
import png

my_parser = argparse.ArgumentParser()
my_parser.add_argument('-s', '--size', action='store', type=int, nargs=2,
                       help="Takes in two arguments that" +
                       "represent the size of the board.")
my_parser.add_argument('-g', '--generation', action='store', type=int,
                       help="Sets the max generation.")
my_parser.add_argument('-p', '--population', action='store',
                       type=int, help="Percentage of times that random" +
                       "cells of life are added to based on board size.")
my_parser.add_argument('-d', '--delete', action='store_true',
                       help="Flag used if you want the images of generations" +
                       "deleted when program is done running.")

# Sanity checks user inputs
args = my_parser.parse_args()

# Fills in default values if user did not define
if args.size is None:
    HGT = 250
    WID = 122
else:
    if args.size[0] > 9 and args.size[1] > 9:
        HGT = int(args.size[0])
        WID = int(args.size[1])
    else:
        print(f'ERROR: Minimum board size is 10 by 10')
        sys.exit(0)

if args.generation is None:
    maxgeneration = 250
else:
    maxgeneration = args.generation

if args.population is None:
    population = .2
else:
    population = args.population / 100

def countNeighbors(oldgen, x, y):
    """Counts the living neighbors of a cell

    Args:
        oldgen:
        x (int): cordanante of the starting cell
        y (int): coordinate of the starting cell

    Returns:
        int: count of the neighbors

    """
    temp = 1

    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):

            # TODO: this needs rewritin to be more understandable
            if not (i == 0 and j == 0):
                count += int(oldgen[(x + i + WID) % WID][(y + j + HGT) % HGT])

    for i in range(-1, 2):
        for j in range(-1, 2):
            temp += 1

    count -= int(oldgen[x][y])

    return count

epd = epd2in13_V2.EPD()
epd.init(epd.FULL_UPDATE)

def main():

    np.random.seed(random.seed(datetime.now()))

    # Generation 0
    generation = 0
    newgen = np.zeros((WID, HGT))
    oldgen = newgen

    # Generation 1 Creation
    # Randomly sets an intial state of living squares
    for i in range(int(WID * HGT * (population))):
        newgen[random.randint(0, WID - 1)][random.randint(0, HGT - 1)] = 1

    while True:

        oldgen = newgen

        # Converts newgen array into an image object
        binary_transform = np.array(newgen).astype(np.uint8)
        binary_transform[binary_transform > 0] = 255
        img = Image.fromarray(binary_transform, 'L')
        epd.display(epd.getbuffer(img))

        # Calculates the state of the next generation
        for x in range(WID):
            for y in range(HGT):
                neighbors = countNeighbors(oldgen, x, y)
                # Calculate dead cells
                if oldgen[x][y] == 0 and neighbors == 3:
                    newgen[x][y] = 1
                # Calculate alive cells
                elif oldgen[x][y] == 1 and (neighbors < 2 or neighbors > 3):
                    newgen[x][y] = 0

        generation += 1

        if generation > maxgeneration:
            break

if __name__ == "__main__":
    main()

while True:
    main()
