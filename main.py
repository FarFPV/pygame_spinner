from math import sin, cos
import sys

import pygame


def project_vertex(vertex: list[int, int, int], focal_length: int, width: int, height: int):
    x, y, z = vertex
    x_projected = (focal_length * x) // (z + focal_length)
    y_projected = (focal_length * y) // (z + focal_length)
    return [x_projected + width // 2, y_projected + height // 2]


def rotate(vertex: list[int, int, int], pitch: int, roll: int, yaw: int):
    x, y, z = vertex
    new_x = x * (cos(pitch) * cos(roll)) + y * (sin(yaw) * sin(pitch) * cos(roll) - cos(yaw) * sin(roll)) + z * (cos(yaw) * sin(pitch) * cos(roll) + sin(yaw) * sin(roll))
    new_y = x * (cos(pitch) * sin(roll)) + y * (sin(yaw) * sin(pitch) * sin(roll) + cos(yaw) * cos(roll)) + z * (cos(yaw) * sin(pitch) - sin(roll) + sin(yaw) * cos(roll))
    new_z = x * (-sin(pitch)) + y * (sin(yaw) * cos(pitch)) + z * (cos(yaw) * cos(pitch))
    return [new_x, new_y, new_z]


def main():
    width = 800
    height = 600
    black = [0, 0, 0]
    green = [0, 255, 0]
    vertexes = [[-100, -100, 200], [100, -100, 200], [100, 100, 200], [-100, 100, 200],
                [-100, -100, 0], [100, -100, 0], [100, 100, 0], [-100, 100, 0]]
    edges = {0: {1, 3, 4},
             2: {1, 3, 6},
             5: {1, 4, 6},
             7: {3, 4, 6}}

    # pygame.init()
    # screen = pygame.display.set_mode([width, height])
    game_over = False
    while not game_over:
        # Обработка событий
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         game_over = True

        # Вычисления
        vertexes = list(map(lambda vertex: rotate(vertex, 0, 0, 3), vertexes))
        vertexes_projected = list(map(lambda vertex: project_vertex(vertex, 400, width, height), vertexes))

        # Отрисовка
        # screen.fill(black)
        # for i in edges.keys():
        #     for j in edges[i]:
        #         pygame.draw.line(screen, green, vertexes_projected[i], vertexes_projected[j], 5)
        # pygame.display.flip()
        # pygame.time.wait(10)

    sys.exit(0)


if __name__ == '__main__':
    main()
