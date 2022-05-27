from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.snake import Snake
from game.casting.player_one import PlayerOne
from game.casting.player_two import PlayerTwo
from game.directing.director import Director
from game.scripting.action import Action
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point

import pytest

def test_get_x():
    """
    Verify that the get_x method returns the value of the x axis.
    """
    a_point = Point(0, 2)
    assert a_point.get_x == 0

def test_get_y():
    """
    Verify that the get_x method returns the value of the x axis.
    """
    a_point = Point(0, 2)
    assert a_point.get_x == 2

def test_scale():
    """
    Verify that the scale method return accurate results
    """
    a_point = Point(2, 2)
    assert a_point.scale(5) == Point(10, 10)

def test_to_tuple():
    """
    Verify that the to_tuple method returns a tuple.
    """
    a_class = Actor()
    assert a_class.to_tuple(red = 255, green = 255, blue = 255, alpha = 255) == (255, 255, 255, 255)

def test_get_text():
    """
    Verify that the _get_text method returns the text
    """
    an_actor = Actor()
    an_actor._text = "a"

    assert an_actor._get_text == "a"

def test_get_color(self):
    """
    Verify that the _get_color method returns the color
    """
    an_actor = Actor()
    an_actor._color = Color(255, 255, 255)
    assert an_actor.get_color == (255, 255, 255, 255)

def test_get_font_size(self):
    """
    Verify that the _get_font_size method returns the font_size.
    """
    an_actor = Actor()
    an_actor._font_size = 15
    assert an_actor.get_font_size == 15