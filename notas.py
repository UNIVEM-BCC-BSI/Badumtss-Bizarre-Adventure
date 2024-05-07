import pygame
from player import Player

score = 0

class Notas():
    def __init__(self, x, y, altura, largura):
        self.y = y
        self.x = x
        self.altura = altura
        self.largura = largura
        self.image = pygame.image.load('img/minima.png')
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image,self.rect)

    def colisao(self, player):
        return self.rect.colliderect(player)
    


        
            
