from os import remove
from game.audio_service import AudioService
from game.point import Point
from game import constants
from game.physics_service import PhysicsService
from game.action import Action

class HandleCollisionsAction(Action):
    def __init__(self) -> None:
        super().__init__()

    def execute(self, cast):
        audio = AudioService()
        physics = PhysicsService()
        for ball in cast['balls']:
            # x = ball.get_position().get_x()
            # y = ball.get_position().get_y()
            dx = ball.get_velocity().get_x()
            dy = ball.get_velocity().get_y()

        for paddle in cast['paddle']:
            if physics.is_collision(ball, paddle) == True:
                ball.set_velocity(Point(dx, -dy)) 
                audio.play_sound(constants.SOUND_BOUNCE)

            elif physics.is_collision(ball, paddle) == False:
                ball.set_velocity(Point(dx, dy)) 

        brick_remove_list = []
        brick_list = cast['bricks']
        for bricks in brick_list:
            collision = physics.is_collision(bricks, ball)
            if collision == True:
                ball.set_velocity(Point(-dx, -dy))
                audio.play_sound(constants.SOUND_BOUNCE)
                brick_remove_list.append(bricks)
            for brick_num2 in brick_remove_list:
                if bricks == brick_num2:
                    brick_list.remove(brick_num2)
                    print('true')
                    brick_remove_list.remove(bricks)

            # for group in cast['bricks']:
            #     brick_one = brick_remove_list[0]
            #     if group == brick_one:
            #         print(group)


        # for bricks_num in cast['bricks']:
            

        
            

                
                
                

            # for brick_type in cast['bricks']:
            #     brick_one = brick_remove_list[0]
            #     brick_type.index(brick_one)
                
            #     if brick_type == brick_one:
                    
            # brick_type = brick[0]
            # if brick_type == bricks:
                
                
                
            # brick_remove_list.remove(brick_remove)

            # x1 = paddle.get_position().get_x()
            # y1 = paddle.get_position().get_y()
            # if physics.is_collision(x, x1):
            #     ball.set_velocity(Point(-dx, dy))
            # elif physics.is_collision(y, y1):
            #     ball.set_velocity(Point(dx, -dy))


    # def execute(self, cast):
    #     physics = PhysicsService()
    #     for ball in cast['balls']:
    #         for paddle in cast['paddle']:
    #             x = ball.get_position().get_x()
    #             y = ball.get_position().get_y()
    #             dx = ball.get_velocity().get_x()
    #             dy = ball.get_velocity().get_y()

    #             x1 = paddle.get_position().get_x()
    #             y1 = paddle.get_position().get_y()

    #             if physics.is_collision(x, x1):
    #                 ball.set_velocity(Point(-dx, dy))

    #             elif physics.is_collision(y, y1):
    #                 ball.set_velocity(Point(dx, -dy))
            