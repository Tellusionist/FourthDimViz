import pygame
import numpy as np

pygame.init()

display = (500,500)
screen = pygame.display.set_mode(display)

# colors
white = (255,255,255)
black = (0,0,0)

old_vertices = np.array(
    [
    [250, 250],
    [250, 350],
    [350, 250],
    [350, 350]
    ]
)

vertices = np.array(
    [
    [-50, -50],
    [-50, 50],
    [50, -50],
    [50, 50]
    ]
)

edges = [
    (0,1),
    (0,2),
    (1,3),
    (2,3)
]

#left_shift_matrix = np.array([[1.05, 1]])
left_shift_matrix = np.array(
    [
    [1, 0],
    [1, 0],
    [1, 0],
    [1, 0],
    ]
)


theta = np.radians(-3)
c, s = np.cos(theta), np.sin(theta)
rotation_matrix = np.array(
    [
    [c,-s],
    [s, c]
    ]
)

#for vertex in vertices:
#    pygame.draw.circle(screen, white, vertex, 2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    screen.fill(black)
    for edge in edges:
        pygame.draw.line(screen, white, vertices[edge[0]]+250, vertices[edge[1]]+250, 1 )

    pygame.display.update()
    pygame.time.wait(30)
    #vertices = vertices+left_shift_matrix
    vertices = np.matmul(vertices, rotation_matrix)
