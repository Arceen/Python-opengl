import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math


pygame.init()

screen_width=800
screen_height=600

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF |  OPENGL)
pygame.display.set_caption('OpenGL in python')

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-2, 4, -2, 2)

def plot_graph():
    # glPointSize(5)
    glBegin(GL_POINTS)
    px: GL_DOUBLE
    py: GL_DOUBLE
    for px in np.arange(-2, 4, 0.005):
        py = math.exp(-px)*math.cos(2*math.pi*px)
        glVertex2f(px, py)
    glEnd()

done = False
init_ortho()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_graph()
    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()