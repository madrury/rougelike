from etc.enum import MonsterGroups
from game_objects.monsters import (
    Orc, Troll, Kruthik, PinkJelly, FireBloat, WaterBloat,
    Zombie, Necromancer)


MONSTER_GROUPS = {
    MonsterGroups.NONE: [],
    MonsterGroups.SINGLE_ORC: [Orc],
    MonsterGroups.THREE_ORCS: [Orc, Orc, Orc],
    MonsterGroups.SINGLE_TROLL: [Troll],
    MonsterGroups.TWO_ORCS_AND_TROLL: [Orc, Orc, Troll],
    MonsterGroups.KRUTHIK_SQARM: [Kruthik]*10,
    MonsterGroups.PINK_JELLY: [PinkJelly],
    MonsterGroups.FIRE_BLOAT: [FireBloat],
    MonsterGroups.WATER_BLOAT: [WaterBloat],
    MonsterGroups.ZOMBIE: [Zombie],
    MonsterGroups.NECROMANCER: [Necromancer]
}


MONSTER_SCHEDULE = [
    (0.8, MonsterGroups.NONE),
    (0.2*0.0, MonsterGroups.SINGLE_ORC),
    (0.2*0.0, MonsterGroups.THREE_ORCS),
    (0.2*0.0, MonsterGroups.SINGLE_TROLL),
    (0.2*0.0, MonsterGroups.TWO_ORCS_AND_TROLL),
    (0.2*0.0, MonsterGroups.KRUTHIK_SQARM),
    (0.2*0.0, MonsterGroups.PINK_JELLY),
    (0.2*0.5, MonsterGroups.FIRE_BLOAT),
    (0.2*0.5, MonsterGroups.WATER_BLOAT),
    (0.2*0.0, MonsterGroups.ZOMBIE),
    (0.2*0.0, MonsterGroups.NECROMANCER),
]
