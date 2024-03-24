class Planet:
    AU = 1.495978707e11  # average distance of the earth in meters from sun astronomical unit
    G = 6.67430e-11  # Gravitational constant
    SCALE = 350 / AU

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


def main():
    pass


if __name__ == "__main__":
    main()
