import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
from Utils import *

pygame.init()

screen_width=800
screen_height=600
ortho_width = 640
ortho_height = 480

screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF |  OPENGL)
pygame.display.set_caption('OpenGL in python')

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, ortho_width, 0, ortho_height)

def plot_points():
    glBegin(GL_POINTS)
    for point in points: 
        glVertex2f(point[0], point[1])
    glEnd()

done = False
init_ortho()
glPointSize(5)

points = []

while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == MOUSEBUTTONDOWN:
            px, py = pygame.mouse.get_pos()
            px = map_value(0, screen_width, 0, ortho_width, px)
            py = map_value(0, screen_height, ortho_height, 0, py)
            points.append([px, py])
            
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_points()
    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()