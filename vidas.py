import pygame

class Vidas:
    def __init__(self):
        self.vidas_max = 5
        self.vidas_ini = self.vidas_max
        self.vida_cheia = pygame.image.load('imagem/vidacheia.png').convert_alpha()
        self.vida_vazia = pygame.image.load('imagem/vidavazia.png').convert_alpha()
        self.vida_larg = self.vida_cheia.get_width()
        self.vida_alt = self.vida_cheia.get_height()
        self.espacamento = 10
        self.posicao = (800 - self.vidas_max * (self.vida_larg + self.espacamento), 10)

    def draw(self, tela):
        x, y = self.posicao
        for i in range(self.vidas_ini):
            tela.blit(self.vida_cheia, (x + i * (self.vida_larg + self.espacamento), y))
        for i in range(self.vidas_ini):
            tela.blit(self.vida_vazia, (x + i * (self.vida_larg + self.espacamento), y))

