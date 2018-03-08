import pygame
from vector import Vector
from snake import Snake
import random
import itertools

DIRECTION_TO_VECTOR = {
            'left': Vector((-1, 0)),
            'right': Vector((1, 0)),
            'down': Vector((0, 1)),
            'up': Vector((0, -1))
        }

BLOCK_SIZE = 10  # pixels
GRID_SIZE = 40  # blocks

BACKGROUND_COLOR = (0, 0, 0)  # black
SNAKE_COLOR = (255, 255, 255)  # white
FOOD_COLOR = (255, 0, 0)  # red


class Game(object):
    """A game of snake!

    Attributes
    __________
    snake : Snake
        The snake.
    screen : Surface
        The game window/screen.
    food : Vector
        The position of the food.
    """
    def __init__(self):
        grid_center = Vector((0.5, 0.5)) * GRID_SIZE
        self.snake = Snake(grid_center, DIRECTION_TO_VECTOR['down'])
        self.screen = pygame.display.set_mode(Vector((1, 1)) * (GRID_SIZE * BLOCK_SIZE))
        self.food = self.get_random_coords()

    def _out_of_bounds(self):
        """Check if snake has gone out of bounds.

        Returns
        _______
        bool
        """
        x, y = self.snake.head()
        if x < 0 or x >= GRID_SIZE or y < 0 or y >= GRID_SIZE:
            return True
        return False

    def _grid_full(self):
        """Check if the grid has any unoccupied points remaining.

        If the grid is completely occupied by the snake's body,
        then we have reached the end of a perfect game.

        Returns
        _______
        bool
        """
        return len(self.snake.body) >= GRID_SIZE**2

    def move(self, direction):
        """Move the snake 1 step in the given direction.

        Parameters
        ----------
        direction : {'left', 'right', 'up', 'down'}
            If the direction is not one of the valid choices, the snake will move 1 step in the
            direction it was already pointing in.
        """
        if not self.out_of_bounds() and not self.snake.self_intersecting() and not self.grid_full():
            if direction in DIRECTION_TO_VECTOR:
                direction = DIRECTION_TO_VECTOR[direction]
            else:
                direction = self.snake.direction

            ate_food = self.snake.head() == self.food
            self.snake.move(direction, grow=ate_food)

            if ate_food:
                self.food = self.get_random_coords()

    @staticmethod
    def _create_block(grid_coord):
        """Create a visual block for the provided grid coordinates.

        Internally, the game grid is represented by a 2D integer lattice where each point in 
        the lattice is a possible position. In order to visualize the game, we need to create 
        a visual block, which we can draw to the screen, for each occupied lattice point.

        Parameters
        __________
        grid_coord : Vector
            A position in the game grid.

        Returns
        _______
        block : Rect
        """
        return  pygame.rect.Rect(grid_coord * BLOCK_SIZE, Vector((1, 1)) * BLOCK_SIZE)

    def draw(self):
        """Draw the current game state to screen.
        """
        self.screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(self.screen, FOOD_COLOR, self.create_block(self.food))
        for p in self.snake:
            pygame.draw.rect(self.screen, SNAKE_COLOR, self.create_block(p))
        pygame.display.update()

    def _get_random_coords(self):
        """Randomly select an unoccupied point in the game grid.

        Returns
        _______
        coords : Vector
        """
        possible_vals = set(xrange(GRID_SIZE))
        possible_x = possible_vals - set([coord[0] for coord in self.snake.body])
        possible_y = possible_vals - set([coord[1] for coord in self.snake.body])
        x = random.choice(list(possible_x))
        y = random.choice(list(possible_y))
        return Vector((x, y))
