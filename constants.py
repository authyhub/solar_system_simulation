import pygame as pg

WIDTH, HEIGHT = 1000, 1000
AU = 1.495978707e11
solar_system = [
    {
        "name": "Sun",
        "radius": 60,  # 696340000,
        "mass": 1.989e30,
        "au_from_sun": 0,
        "color": "#FFFF00",
        "is_sun": True,
        "v_ave": 0,
    },
    {
        "name": "Mercury",
        "radius": 10,  # 2439700,
        "mass": 3.285e23,
        "au_from_sun": 0.39,
        "color": "#BFBFBF",
        "is_sun": False,
        "v_ave": 47870,
    },
    {
        "name": "Venus",
        "radius": 16,  # 6051800,
        "mass": 4.867e24,
        "au_from_sun": 0.72,
        "color": "#FFA500",
        "is_sun": False,
        "v_ave": 35020,
    },
    {
        "name": "Earth",
        "radius": 20,  # 6371000,
        "mass": 5.972e24,
        "au_from_sun": 1,
        "color": "#0000FF",
        "is_sun": False,
        "v_ave": 29790,
    },
    {
        "name": "Mars",
        "radius": 14,  # 3389500,
        "mass": 6.39e23,
        "au_from_sun": 1.52,
        "color": "#aa5000",
        "is_sun": False,
        "v_ave": 24077,
    },
]
