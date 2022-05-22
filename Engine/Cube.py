from OpenGL.GL import *
import pygame

class Cube:
    def __init__(self, draw_type):
        self.vertices = [
            (0.5, -0.5, 0.5),
            (-0.5, -0.5, 0.5),
            (0.5, 0.5, 0.5),
            (-0.5, 0.5, 0.5),
            (0.5, 0.5, -0.5),
            (-0.5, 0.5, -0.5),
            (0.5, -0.5, -0.5),
            (-0.5, -0.5, -0.5)
        ]
        
        self.triangles = [0, 2, 3, 0, 3, 1, 0, 2, 4, 0, 6, 4, 0, 7, 1, 0, 7, 6, 5, 3, 1, 5, 1, 7, 5, 2, 3, 5, 2, 4, 5, 6, 7, 5, 6, 4]
        self.draw_type = draw_type
        
    def draw(self):
        glColor(1,0,0,1)
        for i in range(len(self.triangles)-2):
            glBegin(self.draw_type)
            glVertex3fv(self.vertices[self.triangles[i]])
            glVertex3fv(self.vertices[self.triangles[i+1]])
            glVertex3fv(self.vertices[self.triangles[i+2]])
            glEnd()
