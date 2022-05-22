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
    gluOrtho2D(-5, 5, -5, 5)

def plot_prev_lines():
    global prev_points
    for points in prev_points:
        glBegin(GL_LINE_STRIP)
        for point in points: 
            glVertex2f(point[0], point[1])
        glEnd()

def plot_points():
    global points
    glBegin(GL_POINTS)
    for point in points: 
        glVertex2f(point[0], point[1])
    glEnd()
    
def plot_graph():
    # glPointSize(5)
    glBegin(GL_LINE_STRIP)
    px: GL_DOUBLE
    py: GL_DOUBLE
    for px in np.arange(-2, 4, 0.010):
        py = math.exp(-px)*math.cos(2*math.pi*px)
        glVertex2f(px, py)
    glEnd()

def plot_lines():
    # glBegin(GL_LINES)
    glBegin(GL_LINE_STRIP)
    for point in points: 
        glVertex2f(point[0], point[1])
    # for i in range(len(points)-1):
    #     glVertex2f(points[i][0], points[i][1])
    #     glVertex2f(points[i+1][0], points[i+1][1])
        
    glEnd()
done = False
init_ortho()
glPointSize(1)

prev_points = []
points = []
md = False
while not done:
    p = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            md = True
        elif event.type == pygame.MOUSEBUTTONUP:
            md = False
            prev_points.append(points)
            points = []
        elif event.type == MOUSEMOTION and md:
            px, py = pygame.mouse.get_pos()
            px = map_value(0, screen_width, 0, ortho_width, px)
            py = map_value(0, screen_height, ortho_height, 0, py)
            points.append([px, py])
            
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    plot_graph()
    plot_prev_lines()
    plot_lines()
    pygame.display.flip()
    # pygame.time.wait(10)

pygame.quit()