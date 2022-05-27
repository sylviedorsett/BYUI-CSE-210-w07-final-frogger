from game.scripting.action import Action


#Implement MoveActorsAction class here! 
class MoveActorsAction(Action):
    """
    An update action that moves all the actors.

    The responsibility of MoveActors Action is to move all the actors.
    """

    def execute(self, cast, script):
        """
        Implements method overriding of the 'execute' method in the Action Class.

        Arguments:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of actions in the game
        """
        # get all the actors from the cast
        actors = cast.get_all_actors()
        # loop through the actors       
        for actor in actors:
        # call the move_next() method on each actor
            actor.move_next()


        