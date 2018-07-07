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
            commitable=IceCommitable(),
            shimmer=IceShimmer())


class Grass:

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
