import pygame
class Obstaculo():
    def __init__(self, x, y, altura, largura):
        self.y = y
        self.x = x
        self.altura = altura
        self.largura = largura

        #self.image = pygame.image.load('img/chao.png')
        #self.image = pygame.transform.scale(self.image, (altura,largura))
        self.image = pygame.Surface((largura, altura))
        self.image.fill("black")
        self.rect = self.image.get_rect(topleft=(x, y))


    def draw(self, screen):
        screen.blit(self.image, self.rect)