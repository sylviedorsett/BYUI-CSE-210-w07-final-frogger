import pyray
from game.shared.point import Point


class KeyboardService:
    """
    Watches for a user's input.

    Responsibility: The Keyboard class listens for a user's key strokes and interprets them to represent a point of direction.

    Attributes:
        cell_size (int): the size of a cell on the screen's grid.
    """

    def __init__(self):
        """
        Constructs a new KeyboardService.
        """
        self._keys = {}
        
        self._keys['left'] = pyray.KEY_LEFT
        self._keys['right'] = pyray.KEY_RIGHT
        self._keys['up'] = pyray.KEY_UP
        self._keys['down'] = pyray.KEY_DOWN


    def is_key_up(self, key):
        """
        Checks if the given key is currently up.
        
        Args:
            key (string): The given key (left, right, up, down)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)
        

    def is_key_down(self, key):
        """
        Checks if the given key is currently down.
        
        Args:
            key (string): The given key (left, right, up, down)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)