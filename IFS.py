import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from Utils import *

pygame.init()

screen_width = 800
screen_height = 800
ortho_left = -400
ortho_right = 400
ortho_top = -400
ortho_bottom = 400


screen = pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Turtle Graphics')

current_position = (0, 0)
direction = np.array([0, 1, 0])

axiom = 'X'
rules = {
    "F":"FF",
    "X": "F+[-F-XF-X][++FF][--XF[+X]][++F--X]"
}
draw_length = 5
angle = 35
stack = []
rule_run_number = 5
instructions = ""

points = []
x = 0
y = 0
def run_rule(run_count):
    global instructions
    instructions = axiom
    for loops in range(run_count):
        old_system = instructions
        instructions = ""
        for c in range(0, len(old_system)):
            if old_system[c] in rules:
                instructions += rules[old_system[c]]
            else:
                instructions += old_system[c]
    
    print("Rule")
    print(instructions)      
        

def init_ortho():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(ortho_left, ortho_right, ortho_top, ortho_bottom)

def line_to(x, y):
    global current_position
    glBegin(GL_LINE_STRIP)
    glVertex2f(current_position[0], current_position[1])
    glVertex2f(x, y)
    glEnd()
    current_position = (x, y)

def reset_position():
    global current_position
    global direction
    current_position = (0, -300)
    direction = np.array([0, 1, 0])

def rotate(angle):
    global direction
    direction = z_rotation(direction, math.radians(angle))

def move_to(pos):
    global current_position
    current_position = (pos[0], pos[1])
    
# def draw_turtle():
#     global direction
    
#     move_to(100, 100)
#     for i in range(100):
#         rotate(15)
#         forward(5)
#         rotate(-25)
#         forward(5)
#         rotate(55)
#         forward(10)
#         rotate(-55)

            

def forward(draw_length):
    new_x = current_position[0] + direction[0] * draw_length
    new_y = current_position[1] + direction[1] * draw_length
    line_to(new_x, new_y)


def draw_points():
    glBegin(GL_POINTS)
    for p in points:
        glVertex2f(p[0], p[1])
    glEnd()

def draw_turtle():
    global x, y
    points.append((x, y))
    # points.append((np.random.randint(-200, 200), np.random.randint(-200, 200)))
    r = np.random.rand()
    # if r<0.1:
    #     x, y = 0.00 * x + 0.00 * y + 0.00, 0.00*x + 0.16 * y + 0.00 
    # elif r < 0.86:
    #     x, y = 0.85 * x + 0.04 * y + 0.00, -0.04 * x + 0.85 * y + 1.6 
    # elif r < 0.93:
    #     x, y = 0.2 * x - 0.26 * y + 0.00, 0.23 * x + 0.22 * y + 1.6
    # else:
    #     x, y = -0.15 * x + 0.28 * y + 0.00, 0.26 * x + 0.24 *y + 0.44
    
    if r < 0.33:
        x, y = 0.5 * x + 0.0 * y + 0.00, 0.00 * x + 0.5 * y + 0.5
    elif r < 0.66:
        x, y = 0.5 * x + 0.0 * y + 0.5, 0.0 * x + 0.5 * y + 0.00 
    else:
        x, y = 0.5 * x + 0.0 * y + 0.00, 0.00 * x + 0.5 * y + 0.00
    
        
# def forward():
#     new_x = current_position[0] + direction[0] * draw_length
#     new_y = current_position[1] + direction[1] * draw_length
#     line_to(new_x, new_y)
init_ortho()
done = False
glLineWidth(1)
glPointSize(1)
glColor3f(0, 1, 0)
# run_rule(rule_run_number)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            p = pygame.mouse.get_pos()
            line_to(p[0], p[1])
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslated(-200, -200, 0)
    glScaled(550, 550, 1)
    glBegin(GL_POINTS)
    glVertex2f(0, 0)
    glEnd()
    reset_position()
    draw_turtle()
    draw_points()
    pygame.display.flip()
    pygame.time.wait(1)
pygame.quit()

