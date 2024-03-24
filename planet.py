class Planet:

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
    earth = Planet("earth", 0, 0, 10, 0, (100, 150, 200))
    print(earth)


if __name__ == "__main__":
    main()
