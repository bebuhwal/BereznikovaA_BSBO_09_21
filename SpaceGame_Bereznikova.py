import pygame, controls
from pyshka import Pyshka
from pygame.sprite import Group
from stats import Stats
from scores import Scores
from button import Button


def start_game():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Main Menu")

    font = pygame.font.SysFont("arial", 40)
    text_color = (255, 195, 17)


    start_image = pygame.image.load("images/start.jpg").convert_alpha()
    #scores_image = pygame.image.load("images/scores.jpg").convert_alpha()
    quit_image = pygame.image.load("images/quit.jpg").convert_alpha()

    start_button = Button(300, 200, start_image, 1)
    #scores_button = Button(300, 300, scores_image, 1)
    quit_button = Button(300, 400, quit_image, 1)

    game_menu = True
    show = True

    while show:
        if game_menu:
            if start_button.draw(screen):
                game_menu = False
            if quit_button.draw(screen):
                show = False
        else:
            run()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show = False

        pygame.display.update()
    pygame.quit()

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

start_game()
