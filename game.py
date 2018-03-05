import pygame
from vector import Vector
from snake import Snake


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

    def __init__(self):
        grid_center = Vector((0.5, 0.5)) * Game.grid_size
        self.snake = Snake(grid_center, Game.direction_to_vector['down'])
        self.screen = pygame.display.set_mode(Vector((1, 1)) * (Game.grid_size * Game.block_size))

    def out_of_bounds(self):
        x, y = self.snake.head()
        if x < 0 or x >= Game.grid_size or y < 0 or y >= Game.grid_size:
            return True
        return False

    def move(self, direction):
        """
        Parameters
        ----------
        direction : {'left', 'right', 'up', 'down'}
            The direction the snake should move in.
        """
        if not self.out_of_bounds() and not self.snake.self_intersecting():
            if direction in Game.direction_to_vector:
                direction = Game.direction_to_vector[direction]
            else:
                direction = self.snake.direction
            self.snake.move(direction)

    def draw(self):
        self.screen.fill(Game.background_color)
        for p in self.snake:
            rect = pygame.rect.Rect(p * Game.block_size, Vector((1, 1)) * Game.block_size)
            pygame.draw.rect(self.screen, Game.snake_color, rect)
        pygame.display.update()

