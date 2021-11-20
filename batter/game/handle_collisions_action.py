from game import constants
from game.action import Action

class HandleCollisionsAction(Action):
    def __init__(self) -> None:
        super().__init__()


    def execute(self, cast):
        for ball, paddle in cast['ball']:
            position = ball.get_position()
            self.x = position.get_x()
            self.y = position.get_y()
            position1 = paddle.get_position()
            self.x = position1.get_x()
            self.y = position1.get_y()