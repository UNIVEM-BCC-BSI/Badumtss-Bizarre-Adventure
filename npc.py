import pygame
from player import Player
from math import floor

class Npc():
    # carregamento do portal
    def __init__(self, x, y):
        self.cont = 0
        self.y = y
        self.x = x
        self.images = [pygame.image.load('Sprites/npcs/avo/avo_1.png'),
                       pygame.image.load('Sprites/npcs/avo/avo_2.png'),
                        pygame.image.load('Sprites/npcs/avo/avo_3.png'),
                        pygame.image.load('Sprites/npcs/avo/avo_4.png'),
                        pygame.image.load('Sprites/npcs/avo/avo_5.png'),
                        pygame.image.load('Sprites/npcs/avo/avo_6.png')]
        
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
        if self.anim_index > 5: self.anim_index = 0
        self.image = self.images[floor(self.anim_index)]
        
        screen.blit(self.image, self.rect)