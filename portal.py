import pygame
from player import Player
from math import floor

class Portal():
    # carregamento do portal
    def __init__(self, x, y):
        self.cont = 0
        self.y = y
        self.x = x
        self.images = [pygame.image.load('Sprites/portal/portal_1.png'),
                       pygame.image.load('Sprites/portal/portal_2.png'),
                        pygame.image.load('Sprites/portal/portal_3.png'),
                        pygame.image.load('Sprites/portal/portal_4.png'),
                        pygame.image.load('Sprites/portal/portal_5.png'),
                        pygame.image.load('Sprites/portal/portal_6.png'),
                        pygame.image.load('Sprites/portal/portal_7.png'),
                        pygame.image.load('Sprites/portal/portal_8.png'),
                        pygame.image.load('Sprites/portal/portal_9.png')]
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.anim_index = 0
        self.anim = "idle"
        self.tocando = False

    def draw(self, screen, player):
        self.cont = 0
        if self.rect.colliderect(player.rect):
            self.cont += 1
        self.anim_index += 0.1
        if self.anim_index > 8: self.anim_index = 0
        self.image = self.images[floor(self.anim_index)]
        
        screen.blit(self.image, self.rect)