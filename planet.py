import pygame as pg
from constants import WIDTH, HEIGHT


class Planet:
    AU = 1.495978707e11  # average distance of the earth in meters from sun astronomical unit
    G = 6.67430e-11  # Gravitational constant
    SCALE = 350 / AU
    TIMESTEP = 60 * 60 * 24  # 1 DAY

    def __init__(
        self,
        name: str,
        x: float,
        y: float,
        radius: float,
        mass: float,
        color: tuple = (255, 255, 255),
    ):
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.color = color

        self.orbit = []
        self.u = 0  # x component of velcity
        self.v = 0  # y component of velocity

        self.is_sun = False
        self.distance_from_sun = 0

    def __str__(self):
        return f"<{self.name.upper()}>"

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        pg.draw.circle(win, self.color, (x, y), self.radius)


def main():
    pass


if __name__ == "__main__":
    main()
