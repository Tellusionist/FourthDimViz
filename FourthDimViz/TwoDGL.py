import pygame

from OpenGL.GL import glTranslatef, glRotatef, glClear, glBegin, glEnd, GL_LINES, glVertex3fv, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT
from OpenGL.GLU import gluPerspective

# setup 3D cube vertices
vertices= (
        ( 1, -1, -1 ),
        ( 1,  1, -1 ),
        (-1,  1, -1 ),
        (-1, -1, -1 ),
        ( 1, -1,  1 ),
        ( 1,  1,  1 ),
        (-1, -1,  1 ),
        (-1,  1,  1 )
    )
# edges connecting each vertex
edges = (
        ( 0, 1 ),
        ( 0, 3 ),
        ( 0, 4 ),
        ( 2, 1 ),
        ( 2, 3 ),
        ( 2, 7 ),
        ( 6, 3 ),
        ( 6, 4 ),
        ( 6, 7 ),
        ( 5, 1 ),
        ( 5, 4 ),
        ( 5, 7 )
    )

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF|pygame.OPENGL)
    
    # perspective options: FOV, asepect ratio, znear, zfar
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    # move "us" back 5 units (so we can see the cube)
    glTranslatef(0.0,0.0, -5)

    # Run pygame, exit when clicking close window
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # rotate by the rotation matrix, angle, x, y, and z
        glRotatef(1, 3, 1, 1)

        # clear the screen, I think?
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        # call the cube funciton we built earlier
        Cube()

        # update the pygame display and wait a bit
        pygame.display.flip()
        pygame.time.wait(1)


main()