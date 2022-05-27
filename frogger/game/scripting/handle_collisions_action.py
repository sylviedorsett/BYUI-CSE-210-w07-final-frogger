from constants import *
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._winner = False
        self._loser = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
        
            if self._winner:
                self._handle_winner(cast)
            
            if self._loser:
                self._handle_loser(cast)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the frog collides with one of the vehicles.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        frog = cast.get_first_actor("Player")
        vehicles = cast.get_actors("Vehicles")
        life = cast.get_first_actor("Lives")
        
        y = frog.get_position().get_y()
        if y <= 25:
            self._winner= True
            self._is_game_over = True

        for vehicle in vehicles:
            if vehicle.get_position().equals(frog.get_position()):
                #remove a life
                life.remove_life()

                if life._lives == 0:
                    self._is_game_over = True
                    self._loser = True
                position = Point(MAX_X/2, 525)
                frog.set_position(position)


    def _handle_winner(self, cast):
        if self._winner:
            message = Actor()
            message.set_text("You Win!")
            message.set_color = WHITE
            position = Point(400, 250)
            message.set_position(position)
            cast.add_actor("Message", message)

    def _handle_loser(self, cast):
        """Shows the 'game over' message and turns the snakes white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._loser:
            message = Actor()
            message.set_text("Game Over")
            message.set_color = WHITE
            position = Point(400, 250)
            message.set_position(position)
            cast.add_actor("Message", message)


    def get_is_game_over(self):
        return self._is_game_over

    def get_is_winner(self):
        return self._winner

    