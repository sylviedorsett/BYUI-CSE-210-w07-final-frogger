from constants import *

from game.casting.actor import Actor
from game.casting.cast import Cast
from game.casting.frog import Frog
from game.casting.lives import Lives
from game.casting.score import Score
from game.casting.vehicles import Vehicle
from game.director import Director
from game.scripting.action import Action
from game.scripting.script import Script
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.frog_action import FrogAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point

def main():

    #create the cast with a player (frog), score, lives and vehicles
    cast = Cast()
    cast.add_actor("Player", Frog())
    cast.add_actor("Score", Score(Point(25, 0)))
    cast.add_actor("Lives", Lives(Point(MAX_X-100, 0)))
    cast.add_actor("Vehicles", Vehicle(TRUCK1, 25, 100, 4))
    cast.add_actor("Vehicles", Vehicle(TRUCK1, 350, 100, 4))
    cast.add_actor("Vehicles", Vehicle(TRUCK1, 450, 100, 4))    
    cast.add_actor("Vehicles", Vehicle(CAR1, 325, 200, -5))
    cast.add_actor("Vehicles", Vehicle(CAR1, 175, 200, -5))
    cast.add_actor("Vehicles", Vehicle(CAR1, 425, 200, -5))
    cast.add_actor("Vehicles", Vehicle(CAR1, 575, 200, -5))
    cast.add_actor("Vehicles", Vehicle(TRUCK2, 100, 300, 2))
    cast.add_actor("Vehicles", Vehicle(TRUCK2, 300, 300, 2))
    cast.add_actor("Vehicles", Vehicle(TRUCK2, 500, 300, 2))
    cast.add_actor("Vehicles", Vehicle(CAR2, 300, 400, -3))
    cast.add_actor("Vehicles", Vehicle(CAR2, 100, 400, -3))
    cast.add_actor("Vehicles", Vehicle(CAR2, 675, 400, -3))


    keyboard = KeyboardService()
    video = VideoService()

    script = Script()
    script.add_action("input", FrogAction(keyboard))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video))

    director = Director(video)
    director.start_game(cast, script)
    

if __name__ == "__main__":
    main()
