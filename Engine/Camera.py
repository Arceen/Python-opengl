import pygame
from OpenGL.GLU import *
from math import *

class Camera:
    def __init__(self):
        self.eye = pygame.math.Vector3(0, 0, 0)
        self.up = pygame.math.Vector3(0, 1, 0)
        self.right = pygame.math.Vector3(1, 0, 0)
        self.forward = pygame.math.Vector3(0, 0, 1)
        self.look = self.eye + self.forward
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            self.eye -= self.forward
        self.look = self.eye + self.forward
        gluLookAt(self.eye.x, self.eye.y, self)