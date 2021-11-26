from game import constants
from game.action import Action
from game.point import Point

class MoveActorsAction(Action):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, cast):
        for group in cast.values():
            for actor in group:
                if actor.get_velocity():
                    self._move_actor(actor)
                    self._move_actor(cast['balls'][0])
        # self._move_actor( cast['balls'][0])

    def _move_actor(self, actor):
        position = actor.get_position()
        velocity = actor.get_velocity()

        x = position.get_x()
        y = position.get_y()
        dx = velocity.get_x()
        dy = velocity.get_y()

        x = (x + dx) % constants.MAX_X
        y = (y + dy) % constants.MAX_Y
        
        position = Point(x, y)
        actor.set_position(position)
