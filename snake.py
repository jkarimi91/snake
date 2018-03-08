# https://codereview.stackexchange.com/questions/24267/snake-game-using-pygame
from collections import deque
from vector import Vector


class Snake(object):
    """A snake.

    Attributes
    __________
    direction : Vector
        The direction the snake is pointing in.
    body : deque of Vectors
        The front of the deque, i.e. index 0, is the head of the snake. Each Vector in the 
        deque gives us the position of the ith, relative to the head, body segment.
    """
    def __init__(self, position, direction, init_len=3):
        self.direction = direction
        self.body = deque([position - i * self.direction for i in xrange(init_len)])

    def head(self):
        """Get the position of the snake's head.

        Returns
        _______
        Vector
        """
        return self.body[0]

    def pop_tail(self):
        """Remove the snake's tail.
        """
        self.body.pop()

    def move(self, direction, grow):
        """Move the snake 1 step in the given direction.

        Parameters
        ----------
        direction : Vector
            The direction the snake should move in.
        grow : bool
            Whether the snake should grow 1 segment/step longer during the move.
        """
        if direction != self.direction and direction != -self.direction:
            self.direction = direction
        new_head = self.head() + self.direction
        self.body.appendleft(new_head)

        if not grow:
            self.pop_tail()

    def self_intersecting(self):
        """Check if the snake intersects itself i.e. has it collided with itself?

        Returns
        _______
        bool
        """
        body = iter(self)
        head = body.next()
        return head in body

    def __iter__(self):
        return iter(self.body)
