import xml.etree.ElementTree as ET
import re
import numpy as np
import pandas as pd
from cellcraft.src.item import *

default_dir = 'x3d/'

def add_cellpack(x3d_file,threshold,blocksize):
    Protcomplex = protein_complex_x3d(x3d_file)
    Protcomplex.parse_file()
    Protcomplex.load_grid(int(threshold),int(blocksize))
    return Protcomplex.grid.values,Protcomplex.colordict,Protcomplex.texture

class protein_complex_x3d():
    def __init__(self, x3d_file):
        self.x3d_file = x3d_file
        self.surfaces = []
        self.pids = []
        self.colors = []
        self.colordict = {}
        self.texture = {}

    def load_grid(self,threshold,blocksize):
        self.grid = cellcraft_grid(threshold,blocksize)
        for pid,surface in zip(self.pids,self.surfaces):
            self.grid.add_coordinates(surface,pid)
        self.grid.make_grid()
        self.grid.def_blocks()

    def parse_file(self):
        df = pd.read_csv(default_dir+self.x3d_file+'.csv')
        df.pdbid = df.pdbid.str.replace('\'', '')
        tree = ET.parse(default_dir+self.x3d_file+'.x3d')
        root = tree.getroot()
        transforms = root.find('Scene').find('Group').getchildren()
        pdb_pat = re.compile('\d...')
        i = 0
        for transform in transforms:
            MetadataString  = transform.find('MetadataString')
            if not MetadataString == None:
                MetadataString = MetadataString.attrib['value'].split('_')

                df[df.pdbid==MetadataString[2]] = row

                self.pids.append(i)
                self.colordict[i] = row.color.tolist()[0]
                self.texture[i] = row.texture.tolist()[0]

                name = MetadataString[1]
                match = pdb_pat.match(MetadataString[2])
                if match:
                    pdb = match.group(0)
                else:
                    pdb = None

                shapes = transform.findall('Shape')
                all_points = []
                for shape in shapes[::row.take_every.tolist()[0]]:
                    points = np.array(shape.find('IndexedTriangleSet').find('Coordinate').attrib['point'].split(),dtype=float)
                    all_points.append(points.reshape((-1,3)))
                self.surfaces.append(np.concatenate(all_points))
                i += 1