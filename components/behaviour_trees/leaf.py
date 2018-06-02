from pathfinding import get_shortest_path, get_path_to_radius_of_target

from etc.enum import TreeStates
from etc.enum import ResultTypes
from utils.utils import random_walkable_position, random_adjacent
from components.behaviour_trees.root import Node


class MoveTowards(Node):
    """Move the owner towards a target."""
    def tick(self, owner, target, game_map):
        results = [{ResultTypes.MOVE_TOWARDS: (owner, target.x, target.y)}]
        return TreeStates.SUCCESS, results


class SeekTowardsLInfinityRadius(Node):
    """Seek to stay a fixed radius from a target."""
    def __init__(self, radius):
        self.radius = radius

    def tick(self, owner, target, game_map):
        path = get_path_to_radius_of_target(
            game_map, 
            (owner.x, owner.y),
            (target.x, target.y),
            radius=self.radius,
            routing_avoid=owner.routing_avoid)
        if len(path) <= 1:
            return TreeStates.SUCCESS, []
        results = [{
            ResultTypes.SET_POSITION: (owner, path[1][0], path[1][1])}]
        return TreeStates.SUCCESS, results


class TravelToRandomPosition(Node):
    """Pick a random position on the map and walk towards it until getting
    there.
    """
    def __init__(self):
        self.target_position = None
        self.target_path = None

    def tick(self, owner, target, game_map):
        if not self.target_position:
            self.target_position = random_walkable_position(game_map, owner)
        self.path = get_shortest_path(
            game_map,
            (owner.x, owner.y),
            self.target_position,
            routing_avoid=owner.routing_avoid)
        if len(self.path) <= 2:
            self.target_position = None
            return TreeStates.SUCCESS, []
        results = [{
            ResultTypes.MOVE_TOWARDS: (owner, self.path[1][0], self.path[1][1])}]
        return TreeStates.SUCCESS, results


class Skitter(Node):
    """Move the owner to a random adjacent tile."""
    def tick(self, owner, target, game_map):
        results = [{ResultTypes.MOVE_RANDOM_ADJACENT: owner}]
        return TreeStates.SUCCESS, results


class Attack(Node):
    """The owner attackes the target."""
    def tick(self, owner, target, game_map):
        if owner.attacker and target.harmable and target.harmable.hp > 0:
            return (TreeStates.SUCCESS,
                    owner.attacker.attack(game_map, target))
        else:
            return TreeStates.FAILURE, []


class SpawnEntity(Node):

    def __init__(self, maker):
        self.maker = maker

    def tick(self, owner, target, game_map):
        x, y = random_adjacent((owner.x, owner.y))
        if (game_map.walkable[x, y]
            and not game_map.blocked[x, y]
            and not game_map.water[x, y]):
            entity = self.maker.make(x, y)
            if entity:
                return TreeStates.SUCCESS, [{ResultTypes.ADD_ENTITY: entity}]
        return TreeStates.FAILURE, []
