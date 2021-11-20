from game import constants
from game.action import Action
from game.point import Point

class HandleOffScreenAction(Action):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, cast):
        for ball in cast['balls']:
            x = ball.get_position().get_x()
            y = ball.get_position().get_y()
            dx = ball.get_velocity().get_x()
            dy = ball.get_velocity().get_y()

            if x == 0 or x == 800:
                dx = dx * -1

            if y == 0 or y == 600:
                dy = dy * -1
            
            velocity = Point(dx, dy)
            ball.set_velocity(velocity)
            # position = ball.get_position()
            # self.x = position.get_x()
            # self.y = position.get_y()
            # self.bounce_horizontal(ball)
            # self.bounce_vertical(ball)



        
    # def bounce_horizontal(self, actor):
    #     if actor.get_position().get_x() > constants.MAX_X:
    #         positioned = actor._velocity.reverse()
    #         actor.set_velocity(positioned)


    #     if actor.get_position().get_x() < constants.MAX_X:
    #         positioned = actor._velocity.reverse()
    #         actor.set_velocity(positioned)

    #     if actor.get_position().get_y() > constants.MAX_Y:
    #         positioned = actor._velocity.reverse()
    #         actor.set_velocity(positioned)

    #     if actor.get_position().get_y() < constants.MAX_Y:
    #         positioned = actor._velocity.reverse()
    #         actor.set_velocity(positioned)

    # def bounce_horizontal(self, actor):
    #     if actor.get_position().get_x() > constants.MAX_X:
    #         positioned = actor._velocity.reverse()
    #         actor.set_velocity(positioned)


    #     if actor.get_position().get_x() < constants.MAX_X:
    #         positioned = actor._velocity.reverse()
    #         actor.set_velocity(positioned)


    # def bounce_vertical(self, actor):
    #     if actor.get_position().get_y() > constants.MAX_Y:
    #         positioned = actor._velocity.reverse()
    #         actor.set_velocity(positioned)

    #     if actor.get_position().get_y() < constants.MAX_Y:
    #         positioned = actor._velocity.reverse()
    #         actor.set_velocity(positioned)

            
            




            