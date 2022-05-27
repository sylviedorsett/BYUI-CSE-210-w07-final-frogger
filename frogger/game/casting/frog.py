from constants import *

from game.casting.actor import Actor
from game.shared.point import Point

class Frog(Actor):
    """
    A frog in the game.
    
    The responsibility of Frog is to create the player's avatar.
        
    """
    def __init__(self):
        super().__init__()
        self._image = FROG
        self._position = Point(MAX_X/2, 525)
        self._velocity = Point(0, 0)
    

    def get_image(self):
        """Gets the frog's image."""
        return self._image
    
    def move_next(self):
        'Moves the frog using its velocity.'

        position = self.get_position()
        velocity = self.get_velocity()
        new_position = position.add(velocity)
        self.set_position(new_position)









