import pygame, sys
from bullet import Bullet
from ino import Ino
import time

def events(screen, pyshka, bullets):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #вправо
            if event.key == pygame.K_d:
                pyshka.mright = True
            elif event.key == pygame.K_a:
                pyshka.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, pyshka)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            #вправо
            if event.key == pygame.K_d:
                pyshka.mright = False
            elif event.key == pygame.K_a:
                pyshka.mleft = False

def update(bg_color, screen, stats, score, pyshka, inos, bullets):
    """"обновление экрана"""
    screen.fill(bg_color)
    score.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pyshka.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, score, inos, bullets):
    """обновлять позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        for inos in collisions.values():
            stats.score += 100 * len(inos)
        score.image_score()
        check_high_score(stats, score)
        score.image_pyshka()
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)

def pyshka_kill(stats, screen, score, pyshka, inos, bullets):
    """столкновение пушки и армии"""
    if stats.pyshka_left > 0:
        stats.pyshka_left -= 1
        score.image_pyshka()
        inos.empty()
        bullets.empty()
        create_army(screen, inos)
        pyshka.create_pyshka()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()

def update_inos(stats, screen, score, pyshka, inos, bullets):
    """обновляет позицию пришельцев"""
    inos.update()
    if pygame.sprite.spritecollideany(pyshka, inos):
        pyshka_kill(stats, screen, score, pyshka, inos, bullets)
    inos_check(stats, screen, score, pyshka, inos, bullets)

def inos_check(stat, screen, score, pyshka, inos, bullets):
    """проверка, дошли ли пришельцы до низа экрана"""
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            pyshka_kill(stat, screen, score, pyshka, inos, bullets)
            break

def create_army(screen, inos):
    """создание армии пришельцев"""
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((800 - 100 - 2 * ino_height) / ino_height)

    for row_number in range (number_ino_y - 2):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + (ino.rect.height * row_number)
            inos.add(ino)


def check_high_score(stats, score):
    """проверка рекордов"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        score.image_high_score()
        with open('hightscore.txt', 'w') as f:
            f.write(str(stats.high_score))