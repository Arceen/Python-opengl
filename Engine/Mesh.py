from OpenGL.GL import *
import pygame

class Mesh:
    def __init__(self):
        self.vertices = [
            (0.5, -0.5, 0.5),
            (-0.5, -0.5, 0.5),
            (0.5, 0.5, 0.5),
            (-0.5, 0.5, 0.5),
            (0.5, 0.5, -0.5),
            (-0.5, 0.5, -0.5)
        ]
        self.triangles = [0, 2, 3, 0, 3, 1]
        self.draw_type = GL_LINE_LOOP
        
    def draw(self):
        for i in range(0, len(self.triangles)-2, 3):
            glBegin(self.draw_type)
            glVertex3fv(self.vertices[self.triangles[i]])
            glVertex3fv(self.vertices[self.triangles[i+1]])
            glVertex3fv(self.vertices[self.triangles[i+2]])
            glEnd()
