import math
from planet import Planet
from constants import WIDTH, HEIGHT, pg, solar_system, AU

pg.init()
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Planet Simulation")


def main():
    BGC = (0, 10, 55)
    bodies = [
        Planet(
            body["name"],
            AU * body["au_from_sun"],
            0,
            body["radius"],
            body["mass"],
            body["color"],
            body["is_sun"],
        )
        for body in solar_system
    ]

    print(bodies)

    for body in bodies:
        print(body.x)

    simulate = True
    clock = pg.time.Clock()
    while simulate:
        clock.tick(60)
        WIN.fill(BGC)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                simulate = False
        for body in bodies:
            body.update_position(bodies)
            body.draw(WIN)
        pg.display.update()
    pg.quit()


if __name__ == "__main__":
    main()
