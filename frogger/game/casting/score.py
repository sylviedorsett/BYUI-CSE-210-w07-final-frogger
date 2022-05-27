
from constants import *
from game.casting.actor import Actor
from game.shared.point import Point

class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of players scores and 
    add points for players. 
    Attributes:
        self._score (int): a player's score
        self._prepare_score: calls the _prepare_score method to print it to the screen
    """
    def __init__(self, position):
        """Creates an instance of score
        Arguments:
            _player_name
            _position
        """
        super().__init__()
        self._score = 0
        self.set_position(position)
        self.set_color(WHITE)
        self._prepare_score()
        

    def add_points(self):
        """Adds the given points to the score's total points.
        
        Args:
            score (int): The player's score to add to.
        """
        self._score += 10
        self._prepare_score()

    def _prepare_score(self):
        text = str(self._score)
        self.set_text(f"Score : {text}")
       