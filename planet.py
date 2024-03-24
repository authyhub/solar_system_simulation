class Planet:

    def __init__(self, name, x, y, radius, mass, color: tuple = (255, 255, 255)):
        self.name = name
        self.x = x
        self.y = y
        self.radius = radius
        self.mass = mass
        self.color = color

    def __str__(self):
        return f"<{self.name.upper()}>"


def main():
    earth = Planet("earth", 0, 0, 10, 0, (100, 150, 200))
    print(earth)


if __name__ == "__main__":
    main()
