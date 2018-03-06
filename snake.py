# https://codereview.stackexchange.com/questions/24267/snake-game-using-pygame
from collections import deque
from vector import Vector


class Snake(object):
    def __init__(self, position, direction, init_len=3):
        self.direction = direction
        self.body = deque([position - i * self.direction for i in xrange(init_len)])

    def head(self):
        return self.body[0]

    def pop_tail(self):
        self.body.pop()

    def move(self, direction, grow):
        """
        Parameters
        ----------
        direction : vector
            The direction the snake should move in.
        grow : bool
            Whether the snake should grow 1 segment longer.
        """
        if direction != self.direction and direction != -self.direction:
            self.direction = direction
        new_head = self.head() + self.direction
        self.body.appendleft(new_head)

        if not grow:
            self.pop_tail()

    def self_intersecting(self):
        body = iter(self)
        head = body.next()
        return head in body

    def __iter__(self):
        return iter(self.body)
