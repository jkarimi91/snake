import pygame
from vector import Vector
from snake import Snake
import random
import itertools


class Game(object):
    direction_to_vector = {
                'left': Vector((-1, 0)),
                'right': Vector((1, 0)),
                'down': Vector((0, 1)),
                'up': Vector((0, -1))
            }

    block_size = 10  # pixels
    grid_size = 40  # blocks

    background_color = (0, 0, 0)  # black
    snake_color = (255, 255, 255)  # white
    food_color = (255, 0, 0)  # red

    def __init__(self):
        grid_center = Vector((0.5, 0.5)) * Game.grid_size
        self.snake = Snake(grid_center, Game.direction_to_vector['down'])
        self.screen = pygame.display.set_mode(Vector((1, 1)) * (Game.grid_size * Game.block_size))
        self.food = self.get_random_coords()

    def out_of_bounds(self):
        x, y = self.snake.head()
        if x < 0 or x >= Game.grid_size or y < 0 or y >= Game.grid_size:
            return True
        return False

    def grid_full(self):
        return len(self.snake.body) >= Game.grid_size**2

    def move(self, direction):
        """
        Parameters
        ----------
        direction : {'left', 'right', 'up', 'down'}
            The direction the snake should move in.
        """
        if not self.out_of_bounds() and not self.snake.self_intersecting() and not self.grid_full():
            if direction in Game.direction_to_vector:
                direction = Game.direction_to_vector[direction]
            else:
                direction = self.snake.direction

            ate_food = self.snake.head() == self.food
            self.snake.move(direction, grow=ate_food)

            if ate_food:
                self.food = self.get_random_coords()

    @staticmethod
    def block(grid_coord):
        return  pygame.rect.Rect(grid_coord * Game.block_size, Vector((1, 1)) * Game.block_size)

    def draw(self):
        self.screen.fill(Game.background_color)
        pygame.draw.rect(self.screen, Game.food_color, self.block(self.food))
        for p in self.snake:
            pygame.draw.rect(self.screen, Game.snake_color, self.block(p))
        pygame.display.update()

    def get_random_coords(self):
        possible_vals = set(xrange(Game.grid_size))
        possible_x = possible_vals - set([coord[0] for coord in self.snake.body])
        possible_y = possible_vals - set([coord[1] for coord in self.snake.body])
        x = random.choice(list(possible_x))
        y = random.choice(list(possible_y))
        return Vector((x, y))
