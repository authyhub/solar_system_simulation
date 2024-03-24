import pygame as pg
import math
from planet import Planet
from constants import WIDTH, HEIGHT

pg.init()
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Planet Simulation")

BGC = (0, 10, 55)


def main():
    sun = Planet("sun", 0, 0, 50, 0, (225, 225, 0))
    earth = Planet("earth", 0, 0, 10, 0, (100, 150, 200))
    print(earth, sun)

    simulate = True
    clock = pg.time.Clock()
    while simulate:
        clock.tick(60)
        WIN.fill(BGC)
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                simulate = False
    pg.quit()


if __name__ == "__main__":
    main()
