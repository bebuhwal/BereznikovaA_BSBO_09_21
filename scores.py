import pygame.font
from pyshka import Pyshka
from pygame.sprite import Group

class Scores():
    """вывод игровой информации"""
    def __init__(self, screen, stats):
        """инициализация подсчета очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_score()
        self.image_high_score()
        self.image_pyshka()

    def image_score(self):
        """преобразовывает текст счета в граф. изображение"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_pyshka(self):
        """колличество жизней"""
        self.pyshka = Group()
        for pyshka_number in range(self.stats.pyshka_left):
            pyshka = Pyshka(self.screen)
            pyshka.rect.x = 15 + pyshka_number * pyshka.rect.width
            pyshka.rect.y = 20
            self.pyshka.add(pyshka)

    def image_high_score(self):
        """преобразует рекорд в граф изображение"""
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (0,0,0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def show_score(self):
        """отображение счета на экране"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.pyshka.draw(self.screen)

