from game.actor import Actor
from game import constants

class Brick(Actor):
    def __init__(self) -> None:
        super().__init__()

        self._position = 0
        self._description = ''
        self.set_width(constants.BRICK_WIDTH)
        self.set_height(constants.BRICK_HEIGHT)

        

    # def get_position(self):
    #     return self._position
    