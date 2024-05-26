import pygame
from random import shuffle

class Pergunta():
    def __init__(self, cont:int=0, opcoes:list=["no"]*4):
        self.pergunta = cont
        self.correta = opcoes[0] 
        self.opcoes = shuffle(opcoes)
        self.pressing = False
        self.ClicouCorreto = False
        
        # background
        self.image = pygame.Surface((700, 500), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 230))

        # texto
        fonte = pygame.font.Font(None, 35)
        text_surface = fonte.render("O que essa figura representa?", True, "white")
        self.image.blit(text_surface, (180, 10))

        # perguntas
        img = pygame.image.load(f"imgs_part/partitura_{cont+1}.png").convert_alpha()
        img = pygame.transform.scale(img, (300, 250))
        self.image.blit(img, (200, 40))

        self.buttons = [Botao(opcoes[0], 100, 300), Botao(opcoes[1], 400, 300),
                        Botao(opcoes[2], 100, 400), Botao(opcoes[3], 400, 400)]
        
        # rect bg
        self.rect = self.image.get_rect(topleft=(50, 50))

    def draw(self, screen):
        for btn in self.buttons:
            btn.draw(self.image)
            if btn.click() and not self.pressing:
                self.pressing = True
                EVENTO = pygame.event.Event(pygame.USEREVENT + 3)
                pygame.event.post(EVENTO)
                
                if btn.texto == self.correta:
                    self.ClicouCorreto = True
                else:
                    self.ClicouCorreto = False

            elif self.pressing and not pygame.mouse.get_pressed()[0]:
                self.pressing = False

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
        self.clicking = False

    def draw(self, screen):
        self.hover()
        self.clicando()
        if self.hovering:
            self.image.fill((158, 158, 158, 128))
        else:
            self.image.fill((0, 0, 0, 128))
        
        # texto
        fonte = pygame.font.Font(None, 25)
        text_surface = fonte.render(self.texto.upper(), True, "white")
        self.image.blit(text_surface, (20, 10))
        # self.rect = self.image.get_rect(topleft=(self.x, self.y))

        screen.blit(self.image, self.rect)

    def clicando(self):
        self.hover()
        if pygame.mouse.get_pressed()[0] and self.hovering and not self.clicking:
            self.clicking = True
        elif self.clicking and not pygame.mouse.get_pressed()[0]:
            self.clicking = False
    
    def click(self):
        return self.clicking

    def hover(self):
        mp = pygame.mouse.get_pos()
        if mp[0] in self.lista_x and mp[1] in self.lista_y and not self.hovering:
            self.hovering = True
        elif self.hovering and not (mp[0] in self.lista_x and mp[1] in self.lista_y):
            self.hovering = False