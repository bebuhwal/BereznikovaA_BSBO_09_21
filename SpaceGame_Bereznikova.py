import pygame, controls
from pyshka import Pyshka
from pygame.sprite import Group
from stats import Stats
from scores import Scores


def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Космический бой")
    bg_color = (0,0,0)
    pyshka = Pyshka(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    score = Scores(screen, stats)

    while True:
        controls.events(screen, pyshka, bullets)
        if stats.run_game:
            pyshka.update_pyshka()
            controls.update(bg_color, screen, stats, score, pyshka, inos, bullets)
            controls.update_bullets(screen, stats, score, inos, bullets)
            controls.update_inos(stats, screen, score, pyshka, inos, bullets)


run()