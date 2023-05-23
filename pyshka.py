import pygame
from pygame.sprite import Sprite

class Pyshka(Sprite):

    def __init__(self, screen):
        """инициализация пушки"""
        super(Pyshka, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/pyshka.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        """рисование пушки"""
        self.screen.blit(self.image, self.rect)

    def update_pyshka(self):
        """обновление позиции пушки"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 2
        if self.mleft and self.rect.left > 0:
            self.rect.centerx -= 2

    def create_pyshka(self):
        """размещает пушку в центре"""
        self.center = self.screen_rect.centerx