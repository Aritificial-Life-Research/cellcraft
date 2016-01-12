import math, sys, gzip, os, glob
import wget
from collections import *
from Bio.PDB import *
from Bio.SeqUtils.CheckSum import seguid
from Bio import SeqIO
from Bio import *
from Bio.Alphabet import IUPAC
from Bio.Seq import Seq
from xml.dom import minidom
import urllib
import numpy as np


# transform pdb into bocks cellcraft
class item_cellcraft():
    def __init__(self, coordinates, threshold, blocksize): # add weigth in future
        self.item = coordinates
        self.threshold = threshold
        self.size = blocksize # unit cell
        self.x = self.item[0]
        self.y = self.item[1]
        self.z = self.item[2]

    # define the volume that item will need -> get dimensions
    def vol_prot(self):
        self.lenx = int(cal_minmax(np.amax(self.x),np.amin(self.x)))
        self.leny = int(cal_minmax(np.amax(self.y),np.amin(self.y)))
        self.lenz = int(cal_minmax(np.amax(self.z),np.amin(self.z)))

    # parse item throuh the grid -> give: grid cell unit (A), dimensions (A) X,Y,Z
    def def_blocks(self):
        # generate a 3D histogram
        self.H, self.edges = np.histogramdd(self.item, bins=(self.lenx/4, self.leny/4, self.lenz/4))
        return self.H,self.edges

    # rotate item if needed to center ->  new dimensions, needed????????
    def move_item(self, refrot, reftrans):
        # transport item to ref position
        # get the rotated structures of item for given refs
        pass

    # translate grid into cellcraft format
    def def_cellcraftinput(self):
        pass

    # define the item in cellpack format
    def def_cellpackinput(self):
        pass

    # define the moment the data is requested
    def date_time(self):
        # date and time of the data generation
        pass

# calculate max-min
def cal_minmax(maxi, mini):
    return int(maxi)-int(mini)
