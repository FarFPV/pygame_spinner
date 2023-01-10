from math import sin, cos
import sys

import pygame


def multiply_matrix(a, b):
    a_rows = len(a)
    a_cols = len(a[0])
    b_rows = len(b)
    b_cols = len(b[0])
    product = [[0 for i in range(b_cols)] for i in range(a_rows)]
    if a_cols == b_rows:
        for i in range(a_rows):
            for j in range(b_cols):
                for k in range(b_rows):
                    product[i][j] += a[i][k] * b[k][j]
    return product


def project_vertex(vertex, focal_length: int, width: int, height: int):
    x, y, z = vertex
    x_projected = (focal_length * x[0]) // (z[0] + focal_length)
    y_projected = (focal_length * y[0]) // (z[0] + focal_length)
    return [x_projected + width // 2, y_projected + height // 2]


def rotate(vertex, pitch, yaw, roll):
    return multiply_matrix([[cos(roll), -sin(roll), 0], [sin(roll), cos(roll), 0], [0, 0, 1]], multiply_matrix([[cos(yaw), 0, sin(yaw)], [0, 1, 0], [-sin(yaw), 0, cos(yaw)]], multiply_matrix([[1, 0, 0], [0, cos(pitch), -sin(pitch)], [0, sin(pitch), cos(pitch)]], vertex)))


def main():
    width = 800
    height = 600
    black = [0, 0, 0]
    white = [255, 255, 255]
    red = [255, 0, 0]
    vertexes = [[[-100], [-100], [100]], [[100], [-100], [100]], [[100], [100], [100]], [[-100], [100], [100]],
                [[-100], [-100], [-100]], [[100], [-100], [-100]], [[100], [100], [-100]], [[-100], [100], [-100]]]
    edges = {0: {1, 3, 4},
             1: {0, 2, 5},
             2: {1, 3, 6},
             3: {0, 2, 7},
             4: {0, 5, 7},
             5: {1, 4, 6},
             6: {2, 5, 7},
             7: {3, 4, 6}}

    pygame.init()
    screen = pygame.display.set_mode([width, height])
    game_over = False
    while not game_over:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        # Calculate
        vertexes = list(map(lambda vertex: rotate(vertex, 0, 0.025, 0), vertexes))
        vertexes_projected = list(map(lambda vertex: project_vertex(vertex, 400, width, height), vertexes))

        # Frame drawing
        screen.fill(black)
        for i in edges.keys():
            pygame.draw.circle(screen, red, vertexes_projected[i], 6, 0)
        for i in [0, 2, 5, 7]:
            for j in edges[i]:
                pygame.draw.line(screen, white, vertexes_projected[i], vertexes_projected[j], 3)
        pygame.display.flip()
        pygame.time.wait(10)

    sys.exit(0)


if __name__ == '__main__':
    main()
