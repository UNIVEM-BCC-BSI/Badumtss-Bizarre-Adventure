import pygame
class Obstaculo():
    def __init__(self, x, y, imagem, chao=False):
        self.y = y
        self.x = x
        self.chao = chao

        self.image = pygame.image.load(imagem).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))


    def draw(self, screen):
        screen.blit(self.image, self.rect)

'''
        

        
'''