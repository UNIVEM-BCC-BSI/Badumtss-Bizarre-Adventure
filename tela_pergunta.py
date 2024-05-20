import pygame
from random import shuffle

class Pergunta():
    def __init__(self, pergunta:str="pergunta", opcoes:list=["none"]*4):
        self.pergunta = pergunta
        self.correta = opcoes[0] 
        self.opcoes = shuffle(opcoes)

        # background
        self.image = pygame.Surface((700, 500), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 230))

        # texto
        fonte = pygame.font.Font(None, 35)
        text_surface = fonte.render(self.pergunta, True, "white")
        self.image.blit(text_surface, (20, 20))

        self.buttons = [Botao(opcoes[0], 100, 300), Botao(opcoes[1], 400, 300),
                        Botao(opcoes[2], 100, 400), Botao(opcoes[3], 400, 400)]
        
        # rect bg
        self.rect = self.image.get_rect(topleft=(50, 50))

    def draw(self, screen):
        for btn in self.buttons:
            btn.draw(self.image)
        screen.blit(self.image, self.rect)


class Botao:
    def __init__(self, texto, x, y):
        self.texto = texto
        self.x = x
        self.y = y

        # listas
        x2 = self.x + 50
        y2 = self.y + 50
        self.lista_x = tuple(range(x2, x2+200))
        self.lista_y = tuple(range(y2, y2+75))

        self.image = pygame.Surface((200, 75), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 128))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.hovering = False

    def draw(self, image):
        self.hover()
        if self.hovering:
            self.image.fill((158, 158, 158, 128))
        else:
            self.image.fill((0, 0, 0, 128))
        
        # texto
        fonte = pygame.font.Font(None, 25)
        text_surface = fonte.render(self.texto, True, "white")
        self.image.blit(text_surface, (5, 5))
        # self.rect = self.image.get_rect(topleft=(self.x, self.y))

        image.blit(self.image, self.rect)

    def clicando(self):
        self.hover()
        if pygame.mouse.get_pressed()[0] and self.hovering:
            return True
        else:
            return False
    
    def hover(self):
        mp = pygame.mouse.get_pos()
        if mp[0] in self.lista_x and mp[1] in self.lista_y and not self.hovering:
            self.hovering = True
        elif self.hovering and not (mp[0] in self.lista_x and mp[1] in self.lista_y):
            self.hovering = False