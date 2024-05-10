import pygame
class Obstaculo():
    def __init__(self, x, y, imagem):
        self.y = y
        self.x = x

        self.image = pygame.image.load(imagem).convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))


    def draw(self, screen):
        screen.blit(self.image, self.rect)

'''
        screen.blit(fase1_bg, (0, 0))
        player.size = 1
        player.draw(screen, obstaculos)

        for n in obstaculos:
            n.draw(screen)
            
        obstaculos = [Obstaculo(30, 462, "Sprites/fase1/plat1.png")]
'''