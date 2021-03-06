from enum import Enum, auto

class TerrainTypes(Enum):
    FIRST_FLOOR = auto()
    BASIC_FLOOR = auto()
    SHRUB_FLOOR = auto()
    WATER_FLOOR = auto()
    ICE_FLOOR = auto()


TERRAIN_DEFINITIONS = {
    TerrainTypes.FIRST_FLOOR: {
        'upward_stairs': False,
        'min_torches': 0,
        'max_torches': 0,
        'min_pools': 0,
        'max_pools': 1,
        'pool_room_proportion': 0.7,
        'min_rivers': 0,
        'max_rivers': 0,
        'min_grass': 1,
        'max_grass': 6,
        'grass_room_proportion': 2.0,
        'min_shrubs': 0,
        'max_shrubs': 0,
        'shrubs_room_proportion': 0.0,
        'min_ice': 0,
        'max_ice': 0,
        'ice_room_proportion': 0.0,
    },
    TerrainTypes.BASIC_FLOOR: {
        'min_torches': 3,
        'max_torches': 10,
        'min_pools': 2,
        'max_pools': 4,
        'pool_room_proportion': 0.7,
        'min_rivers': 0,
        'max_rivers': 1,
        'min_grass': 3,
        'max_grass': 10,
        'grass_room_proportion': 2.0,
        'min_shrubs': 0,
        'max_shrubs': 0,
        'shrubs_room_proportion': 0.0,
        'min_ice': 0,
        'max_ice': 0,
        'ice_room_proportion': 0.0,
    },
    TerrainTypes.SHRUB_FLOOR: {
        'min_torches': 3,
        'max_torches': 10,
        'min_pools': 0,
        'max_pools': 4,
        'pool_room_proportion': 0.7,
        'min_rivers': 0,
        'max_rivers': 3,
        'min_grass': 2,
        'max_grass': 6,
        'grass_room_proportion': 2.0,
        'min_shrubs': 2,
        'max_shrubs': 6,
        'shrubs_room_proportion': 0.7,
        'min_ice': 0,
        'max_ice': 0,
        'ice_room_proportion': 0.0,
    },
    TerrainTypes.WATER_FLOOR: {
        'min_torches': 3,
        'max_torches': 10,
        'min_pools': 2,
        'max_pools': 8,
        'pool_room_proportion': 0.7,
        'min_rivers': 2,
        'max_rivers': 6,
        'min_grass': 2,
        'max_grass': 8,
        'grass_room_proportion': 2.0,
        'min_shrubs': 0,
        'max_shrubs': 1,
        'shrubs_room_proportion': 0.7,
        'min_ice': 0,
        'max_ice': 0,
        'ice_room_proportion': 0.0,
    },
    TerrainTypes.ICE_FLOOR: {
        'min_torches': 3,
        'max_torches': 10,
        'min_pools': 2,
        'max_pools': 8,
        'pool_room_proportion': 0.7,
        'min_rivers': 0,
        'max_rivers': 4,
        'min_grass': 0,
        'max_grass': 2,
        'grass_room_proportion': 2.0,
        'min_shrubs': 0,
        'max_shrubs': 1,
        'shrubs_room_proportion': 0.7,
        'min_ice': 2,
        'max_ice': 6,
        'ice_room_proportion': 0.5,
    }
}