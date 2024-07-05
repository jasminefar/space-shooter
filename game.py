import pygame
import random
import time

pygame.init()

screen_width = 800
screen_height = 600

# colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# screen setup
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Shooter Game")

# Load images
spaceship_img = pygame.image.load("spaceship.png")
asteroid_img = pygame.image.load("asteroid.png")
bullet_img = pygame.image.load("bullet.png")
explosion_img = pygame.image.load("explosion.png")
powerup_img = pygame.image.load("powerup.png")

# fonts
font = pygame.font.SysFont(None, 55)

# classes
class Player:
    def __init__(self):
        self.image = spaceship_img
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height - 100))
        self.speed = 10
        self.shoot_delay = 300  # these r in milliseconds
        self.last_shot = pygame.time.get_ticks()

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot > self.shoot_delay:
            bullets.append(Bullet(self.rect.centerx, self.rect.top))
            self.last_shot = current_time

class Bullet:
    def __init__(self, x, y):
        self.image = bullet_img
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = -10

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            bullets.remove(self)

class Asteroid:
    def __init__(self):
        self.image = asteroid_img
        self.rect = self.image.get_rect(
            topleft=(random.randint(0, screen_width - self.image.get_width()), random.randint(-100, -40))
        )
        self.speed = random.randint(2, 6)

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > screen_height:
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(0, screen_width - self.image.get_width())
            self.speed = random.randint(2, 6)

class Explosion:
    def __init__(self, x, y):
        self.image = explosion_img
        self.rect = self.image.get_rect(center=(x, y))
        self.animation_time = pygame.time.get_ticks()
        self.animation_duration = 200

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.animation_time > self.animation_duration:
            explosions.remove(self)

class PowerUp:
    def __init__(self):
        self.image = powerup_img
        self.rect = self.image.get_rect(
            topleft=(random.randint(0, screen_width - self.image.get_width()), random.randint(-100, -40))
        )
        self.speed
