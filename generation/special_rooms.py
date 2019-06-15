from enum import Enum, auto

from etc.config import GLOBAL_FLOOR_CONFIG
from game_objects.terrain import StationaryTorch
from generation.room import DungeonRoom, PinnedDungeonRoom, Rectangle



class FirstRoom:
    """A special long room filled with pillars.  Used as the first room in
    the game, where the player intially spawns.
    """
    def __init__(self, width=17, height=25):
        self.width = width
        self.height = height

    def make(self):
        floor_width = GLOBAL_FLOOR_CONFIG['width']
        floor_height = GLOBAL_FLOOR_CONFIG['height']
        floor_width_midpoint = GLOBAL_FLOOR_CONFIG['width'] // 2
        pillars = [
            StationaryTorch.make(None, floor_width_midpoint - 5, y) 
                for y in range(floor_height - 6, floor_height - 9*3, -3)] + [
            StationaryTorch.make(None, floor_width_midpoint - 3, y) 
                for y in range(floor_height - 6, floor_height - 9*3, -3)] + [
            StationaryTorch.make(None, floor_width_midpoint + 3, y)
                for y in range(floor_height - 6, floor_height - 9*3, -3)] + [
            StationaryTorch.make(None, floor_width_midpoint + 5, y)
                for y in range(floor_height - 6, floor_height - 9*3, -3)]
        room = make_rectangle_room(self.width, self.height)
        pin_location = (floor_width // 2 - self.width // 2, floor_height - self.height - 2)
        pillars_room_pinned = PinnedDungeonRoom(room, pin_location, objects=pillars)
        return pillars_room_pinned


def make_rectangle_room(width=16, height=25):
    """Construct a simple rectangular room.

    Parameters
    ----------
    width: int
      The width of the room.

    height: int
      The height of the room.

    Returns
    -------
    room: DungeonRoom
    """
    room = DungeonRoom(width, height)
    room.add_rectangle(Rectangle(0, 0, width, height))
    return room


class RoomType(Enum):
    FIRST_ROOM = auto()

ROOM_CONSTRUCTORS = {
    RoomType.FIRST_ROOM: FirstRoom()
}