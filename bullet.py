import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, pyshka):
        """создаем пулю в позиции пушки"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 255, 195, 14
        self.speed = 4
        self.rect.centerx = pyshka.rect.centerx
        self.rect.top = pyshka.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """перемещение пули вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """рисуем пулю на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)