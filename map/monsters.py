from enum import Enum, auto
import numpy as np

from entity import Entity
from render_functions import RenderOrder

from etc.colors import COLORS
from utils.utils import choose_from_list_of_tuples
from components.ai import BasicMonster
from components.attacker import Attacker
from components.harmable import Harmable


class MonsterGroups(Enum):
    NONE = auto()
    SINGLE_ORC = auto() 
    THREE_ORCS = auto() 
    SINGLE_TROLL = auto() 
    TWO_ORCS_AND_TROLL = auto()


def spawn_monsters(monster_schedule, floor, entities):
    for room in floor.rooms:
        monster_group = choose_from_list_of_tuples(MONSTER_SCHEDULE)
        spawn_monster_group(monster_group, room, entities)

def spawn_monster_group(monster_group, room, entities):
    for monster_type in MONSTER_GROUPS[monster_group]:
        monster = monster_type.spawn(room, entities)
        if monster is not None:
            entities.append(monster)


class Monster:

    @classmethod
    def spawn(cls, room, entities, max_tries=25):
        for _ in range(max_tries):
            x, y = room.random_point()
            if not any((x, y) == (entity.x, entity.y) for entity in entities):
                monster = cls.make(x, y)
                break
        else:
            monster = None
        return monster


class Orc(Monster):
    
    @staticmethod
    def make(x, y):
        return Entity(
            x, y, 'O', COLORS['desaturated_green'], 'Orc', 
            attacker=Attacker(power=3),
            harmable=Harmable(hp=10, defense=0),
            ai=BasicMonster(),
            blocks=True,
            render_order=RenderOrder.ACTOR)


class Troll(Monster):
         
    @staticmethod
    def make(x, y):
        return Entity(
            x, y, 'T', COLORS['darker_green'], 'Troll', 
            attacker=Attacker(power=4),
            harmable=Harmable(hp=16, defense=1),
            ai=BasicMonster(),
            blocks=True,
            render_order=RenderOrder.ACTOR)
            

MONSTER_GROUPS = {
    MonsterGroups.NONE: [],
    MonsterGroups.SINGLE_ORC: [Orc],
    MonsterGroups.THREE_ORCS: [Orc, Orc, Orc],
    MonsterGroups.SINGLE_TROLL: [Troll],
    MonsterGroups.TWO_ORCS_AND_TROLL: [Orc, Orc, Orc]
}


MONSTER_SCHEDULE = [
    (0.5, MonsterGroups.NONE),
    (0.5*0.4, MonsterGroups.SINGLE_ORC),
    (0.5*0.2, MonsterGroups.THREE_ORCS),
    (0.5*0.2, MonsterGroups.SINGLE_TROLL),
    (0.5*0.2, MonsterGroups.TWO_ORCS_AND_TROLL),
]
