from OpenGL.GL import *
from Mesh import *
import pygame

class LoadMesh(Mesh):
    def __init__(self, filename, draw_type):
        
        print("comes here")
        self.vertices = []
        self.triangles = []
        self.filename = filename
        self.draw_type = draw_type
        self.load_drawing()
    
    def load_drawing(self):
        with open(self.filename) as fp:
            print("file opened")
            line = fp.readline()
            while line:
                if line[:2] == "v ":
                    vx, vy, vz = [float(value) for value in line[2:].split(" ")]
                    self.vertices.append((vx,vy,vz))
                if line[:2] == 'f ':
                    t1, t2, t3 = [int(t.split("/")[0]) for t in line[2:].split(" ")]
                    self.triangles.extend([t1-1,t2-1,t3-1])
                line = fp.readline()
        print("file closed")
