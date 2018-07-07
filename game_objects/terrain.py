import random

from entity import Entity
from colors import (
    random_light_green, random_dark_grey, 
    random_light_water, random_dark_water, 
    random_light_ice, random_dark_ice)
from etc.enum import Terrain, EntityTypes, RenderOrder
from etc.colors import COLORS
from etc.chars import CHARS

import components.burnable
import components.encroachable

from components.commitable import (
    TerrainCommitable, WaterCommitable, IceCommitable, 
    ShrubCommitable, BaseCommitable)
from components.dissipatable import NecroticSoilDissipatable
from components.shimmer import WaterShimmer, IceShimmer


class Water:
    """A water terrain tile.

    Water requires entities to swim to cross.

      - The player has a swim stamina.  While swim stamina remains, the player
        can freely move through water.  When the swim stamina is depleated,
        movng through water will drain the player's HP.  Swim stamina is
        recovered every turn the player spends on dry ground.
      - Some entities can move freely through water, i.e. bloats, which float above the water.
      - Land based entities will die immediately upon entering water.

    Additionally:

      - Items that become submerged in water will float.  When floating they
        will move to a random adjacent tile each turn, until they end up on dry
        land.
      - Water can be burned, which will cause a steam entity to spawn in the
        same tile (the water remains).
    """
    @staticmethod
    def make(game_map, x, y):
        game_map.make_transparent_and_walkable(x, y)
        fg_color = random_light_water()
        bg_color = random_light_water()
        dark_fg_color = random_dark_water()
        dark_bg_color = random_dark_water()
        return Entity(
            x, y, CHARS['water'],
            name="Water",
            fg_color=fg_color,
            dark_fg_color=dark_fg_color,
            bg_color=bg_color,
            dark_bg_color=dark_bg_color,
            visible_out_of_fov=True,
            entity_type=EntityTypes.TERRAIN,
            render_order=RenderOrder.TERRAIN,
            burnable=components.burnable.WaterBurnable(),
            commitable=WaterCommitable(),
            shimmer=WaterShimmer())


class Ice:
    """An ice terrain tile.

    Ice affects entities move actions.  If an entity attempts a move action
    that would end in them standing on an ice tile, the move action is instead
    doubled (i.e. instead of moving from (x, y) to (x + dx, y + dy), they
    instead move to (x + 2*dx, y + 2*dy).

    Additionally:
      - Ice can be burned, which removes it from the game map and spawns a
        water entitiy in its place.
    """
    @staticmethod
    def make(game_map, x, y):
        game_map.make_transparent_and_walkable(x, y)
        fg_color = random_light_ice()
        bg_color = random_light_ice()
        dark_fg_color = random_dark_ice()
        dark_bg_color = random_dark_ice()
        return Entity(
            x, y, CHARS['ice'],
            name="Ice",
            fg_color=fg_color,
            dark_fg_color=dark_fg_color,
            bg_color=bg_color,
            dark_bg_color=dark_bg_color,
            visible_out_of_fov=True,
            entity_type=EntityTypes.TERRAIN,
            render_order=RenderOrder.TERRAIN,
            burnable=components.burnable.IceBurnable(),
            commitable=IceCommitable(),
            shimmer=IceShimmer())


class Grass:
    """A grass terrain tile.

    Grass has no effect on movement, but it can be burned.  When grass is
    burned it is removed from teh game map, and spawns a burned grass and a
    fire entity with some probability.  The fire entities can then spread
    throughout the grass, as fire entities have a probability of spreading (by
    burning entities in random adjacent spaces).
    """
    @staticmethod
    def make(game_map, x, y):
        fg_color = random_light_green()
        # Shift down the green component to make the grass dark.
        bg_color = (fg_color[0], fg_color[1] - 60, fg_color[2])
        return Entity(
            x, y, CHARS['grass'],
            name="Grass",
            fg_color=fg_color,
            dark_fg_color=bg_color,
            visible_out_of_fov=True,
            entity_type=EntityTypes.TERRAIN,
            render_order=RenderOrder.TERRAIN,
            burnable=components.burnable.GrassBurnable(),
            commitable=TerrainCommitable())


class BurnedGrass:
    """A burned grass terrain tile.

    Burned grass has no in game function, it is only cosmetic.
    """
    @staticmethod
    def make(game_map, x, y):
        fg_color = random_dark_grey()
        return Entity(
            x, y, CHARS['grass'],
            name="Burned Grass",
            fg_color=fg_color,
            dark_fg_color=fg_color,
            visible_out_of_fov=True,
            entity_type=EntityTypes.TERRAIN,
            render_order=RenderOrder.TERRAIN,
            commitable=TerrainCommitable())

    @staticmethod
    def maybe_make(game_map, x, y, p=0.5):
        spawn = random.uniform(0, 1) < p
        if spawn:
            return BurnedGrass.make(game_map, x, y)
        else:
            return None


class Shrub:
    """A shrub terrain tile.

    Shrubs block visibility. The player may move into the space occupied by a
    shrub, in which case it is trampled and replaced with grass.

    Additionally, shrubs can be burned, and they behave the same way as grass
    with respect to burning.
    """
    @staticmethod
    def make(game_map, x, y):
        fg_color = random_light_green()
        # Shift down the green component to make the grass dark.
        bg_color = (fg_color[0], fg_color[1] - 60, fg_color[2])
        return Entity(
            x, y, CHARS['shrub'],
            name="Shrub",
            fg_color=fg_color,
            dark_fg_color=bg_color,
            visible_out_of_fov=True,
            entity_type=EntityTypes.TERRAIN,
            render_order=RenderOrder.TERRAIN,
            burnable=components.burnable.GrassBurnable(),
            commitable=ShrubCommitable(),
            encroachable=components.encroachable.ShrubEncroachable())


class NecroticSoil:
    """A necrotic soild terrain tile.

    Necrotic soil is left behind in tiles that zomies move through.  Necrotic
    soil dissapates after a few turns, but will harm any entity entering the
    space (with necrotic type damage) while it exists.
    """
    @staticmethod
    def make(game_map, x, y):
        fg_color = COLORS['necrotic_soil']
        return Entity(
            x, y, CHARS['soil'],
            name="Necrotic Soil",
            fg_color=fg_color,
            visible_out_of_fov=True,
            entity_type=EntityTypes.TERRAIN,
            render_order=RenderOrder.TERRAIN,
            commitable=BaseCommitable(),
            dissipatable=NecroticSoilDissipatable(),
            encroachable=components.encroachable.NecroticSoilEncroachable())
