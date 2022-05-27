from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
          
        """
        frog = cast.get_first_actor("Player")
        score = cast.get_first_actor("Score")
        lives = cast.get_first_actor("Lives")
        vehicles = cast.get_actors("Vehicles")
        
        messages = cast.get_actors("Message")

        self._video_service.clear_buffer()
        self._video_service.draw_image(frog)
        self._video_service.draw_actors([score])
        self._video_service.draw_actor(lives)
        for vehicle in vehicles:
            self._video_service.draw_image(vehicle)
        self._video_service.draw_actors(messages)
        self._video_service.flush_buffer()