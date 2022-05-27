from ast import Not
from constants import *
from game.scripting.action import Action
from game.shared.point import Point
from game.services.keyboard_service import KeyboardService

class FrogAction(Action):
    """
    The responsibility of FrogAction is to get the direction and move the frog.

    """
    def __init__(self, keyboard):
        """Constructs a new FrogAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard
        self._direction = Point(0, 0)


    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score = cast.get_first_actor("Score")
        self._direction = Point(0, 0)
        frog = cast.get_first_actor("Player")
        x = frog._position.get_x()
        y = frog._position.get_y()
    

        handle_collisions_class = script.get_second_action("update")
        game_over = handle_collisions_class.get_is_game_over()

        if not game_over:
        # left
            if self._keyboard_service.is_key_down('left'):
                if x >= 10:
                    self._direction = Point(-CELL_SIZE, 0)
                    score.add_points()
            
            # right
            if self._keyboard_service.is_key_down('right'):
                if x <= (MAX_X - 70):
                    self._direction = Point(CELL_SIZE, 0)
                    score.add_points()
            # up
            if self._keyboard_service.is_key_down('up'):
                if y >= 25:
                    self._direction = Point(0, -CELL_SIZE)
                    score.add_points()
            # down
            if self._keyboard_service.is_key_down('down'):
                if y <= 530:
                    self._direction = Point(0, CELL_SIZE)
                    score.add_points()
                

            frog.set_velocity(self._direction)
            frog.move_next()

        else:
            frog.set_velocity(Point(0,0))