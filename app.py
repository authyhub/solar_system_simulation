import pygame as pg
import math


pg.init()
WIDTH, HEIGHT = 1000, 1000
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Planet Simulation")

BGC = (0, 10, 55)


def main():
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
