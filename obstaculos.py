import pygame
class Obstaculo():
    def __init__(self, x, y, altura, largura):
        self.y = y
        self.x = x
        self.altura = altura
        self.largura = largura

        self.image = pygame.Surface((largura, altura))
        self.image.fill("green")
        self.rect = self.image.get_rect(topleft=(x, y))


    def draw(self, screen):
        screen.blit(self.image, self.rect)