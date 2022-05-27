from constants import *
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color


class Lives(Actor):
    """
    A record of lives lost. 
    
    The responsibility of Lives is to keep track of a player's lives.

    Attributes:
        self._lives (int): a player's lives
        self._prepare_lives: calls the _prepare_lives method to print it to the screen
    """
    def __init__(self, position):
        """Creates an instance of score
        Arguments:
            _player_name
            _position
        """
        super().__init__()
        self._lives = 3
        self.set_position(position)
        self.set_color(WHITE)
        self._prepare_score()
        

    def remove_life(self):
        """Removes a life from the player.
        
        Args:
            life (int): The player's life count.
        """
        self._lives -= 1
        self._prepare_score()

    def _prepare_score(self):
        text = str(self._lives)
        self.set_text(f"Lives: {text}")
       