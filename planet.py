from constants import WIDTH, HEIGHT, pg, AU
import math


class Planet:
    AU = AU  # average distance of the earth in meters from sun astronomical unit
    G = 6.67430e-11  # Gravitational constant
    SCALE = 300 / AU
    TIMESTEP = 60 * 60 * 24  # 1 DAY

    def __init__(
        self,
        name: str,
        x: float,
        y: float,
        v: float,
        radius: float,
        mass: float,
        color: tuple = (255, 255, 255),
        is_sun: bool = False,
    ):
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.color = color

        self.orbit = []
        self.u = 0  # x component of velcity
        self.v = v  # y component of velocity

        self.is_sun = is_sun
        self.distance_from_sun = 0

    def __str__(self):
        return f"<{self.name.upper()}>"

    def __repr__(self):
        return self.name.title()

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        pg.draw.circle(win, self.color, (x, y), self.radius)

    def attraction(self, other):

        if not isinstance(other, Planet):
            raise TypeError(
                "Invalid type, the object should be an instance of class Planet"
            )
        ox, oy = other.x, other.y
        x_dist = ox - self.x
        y_dist = oy - self.y
        dist = math.sqrt(x_dist**2 + y_dist**2)
        if other.is_sun:
            self.distance_from_sun == dist
        force = Planet.G * self.mass * other.mass / dist**2
        theta = math.atan2(y_dist, x_dist)
        fx = force * math.cos(theta)
        fy = force * math.sin(theta)
        return fx, fy

    def update_position(self, planets):
        total_fx, total_fy = 0, 0

        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.u += total_fx / self.mass * Planet.TIMESTEP
        self.v += total_fy / self.mass * Planet.TIMESTEP

        self.x += self.u * Planet.TIMESTEP
        self.y += self.v * Planet.TIMESTEP

        self.orbit.append((self.x, self.y))


def main():
    pass


if __name__ == "__main__":
    main()
