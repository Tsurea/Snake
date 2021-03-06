import pygame
from constantes import *


class Bloc(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.velocity = 25
        self.image = pygame.image.load(corps).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity


class Apple:

    def __init__(self):
        self.image = pygame.image.load(pomme).convert()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0