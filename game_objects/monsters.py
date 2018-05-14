from entity import Entity

from etc.colors import COLORS
from etc.enum import RenderOrder, EntityTypes, MonsterGroups, RoutingOptions
from components.ai import BasicMonster, HuntingMonster, SkitteringMonster
from components.attacker import Attacker
from components.burnable import AliveBurnable
from components.commitable import BlockingCommitable
from components.movable import Movable
from components.scaldable import AliveScaldable
import components.harmable


class Kruthik:

    @staticmethod
    def make(x, y):
        return Entity(
            x, y, 'k', COLORS['kruthik'], 'Kruthik', 
            entity_type=EntityTypes.MONSTER,
            blocks=True,
            render_order=RenderOrder.ACTOR,
            routing_avoid=[RoutingOptions.AVOID_WATER,
                           RoutingOptions.AVOID_FIRE,
                           RoutingOptions.AVOID_MONSTERS,
                           RoutingOptions.AVOID_STEAM],
            ai=SkitteringMonster(),
            attacker=Attacker(power=2),
            burnable=AliveBurnable(),
            commitable=BlockingCommitable(),
            harmable=components.harmable.Harmable(hp=1, defense=0),
            movable=Movable(),
            scaldable=AliveScaldable())


class Orc:
    
    @staticmethod
    def make(x, y):
        return Entity(
            x, y, 'O', COLORS['orc'], 'Orc', 
            entity_type=EntityTypes.MONSTER,
            blocks=True,
            render_order=RenderOrder.ACTOR,
            routing_avoid=[RoutingOptions.AVOID_WATER,
                           RoutingOptions.AVOID_FIRE,
                           RoutingOptions.AVOID_MONSTERS,
                           RoutingOptions.AVOID_STEAM],
            ai=BasicMonster(),
            attacker=Attacker(power=3),
            burnable=AliveBurnable(),
            commitable=BlockingCommitable(),
            harmable=components.harmable.Harmable(hp=10, defense=0),
            movable=Movable(),
            scaldable=AliveScaldable())


class PinkJelly:

    @staticmethod
    def make(x, y, hp=20):
        return Entity(
            x, y, 'J', COLORS['pink_jelly'], 'Pink Jelly', 
            entity_type=EntityTypes.MONSTER,
            blocks=True,
            render_order=RenderOrder.ACTOR,
            routing_avoid=[RoutingOptions.AVOID_WATER,
                           RoutingOptions.AVOID_FIRE,
                           RoutingOptions.AVOID_MONSTERS,
                           RoutingOptions.AVOID_STEAM],
            ai=BasicMonster(),
            attacker=Attacker(power=3),
            burnable=AliveBurnable(),
            commitable=BlockingCommitable(),
            harmable=components.harmable.PinkJellyHarmable(
                hp=hp, defense=0),
            movable=Movable(),
            scaldable=AliveScaldable())

    def make_if_possible(game_map, x, y, hp=20):
        if (game_map.within_bounds(x, y) 
            and game_map.walkable[x, y]
            and not game_map.blocked[x, y]
            and not game_map.water[x, y]):
            return PinkJelly.make(x, y, hp=hp)


class Troll:
         
    @staticmethod
    def make(x, y):
        return Entity(
            x, y, 'T', COLORS['troll'], 'Troll', 
            entity_type=EntityTypes.MONSTER,
            blocks=True,
            render_order=RenderOrder.ACTOR,
            routing_avoid=[RoutingOptions.AVOID_WATER,
                           RoutingOptions.AVOID_FIRE,
                           RoutingOptions.AVOID_MONSTERS,
                           RoutingOptions.AVOID_STEAM],
            attacker=Attacker(power=5),
            harmable=components.harmable.Harmable(hp=16, defense=1),
            ai=HuntingMonster(),
            burnable=AliveBurnable(),
            commitable=BlockingCommitable(),
            movable=Movable(),
            scaldable=AliveScaldable())
