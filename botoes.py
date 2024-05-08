import pygame
class Bott:
    def __init__(self,nome, nome_esc, xpos, ypos, enabled, screen):
        self.nome=nome
        self.nome_esc=nome_esc
        self.xpos=xpos
        self.ypos=ypos
        self.enabled=enabled
        self.draw(screen)

    def draw(self, screen):
        if self.enabled:
            if self.cc():
                bt = pygame.image.load(self.nome_esc)
            else:
                bt = pygame.image.load(self.nome)

            bt = pygame.transform.scale(bt, (320, 60))
            screen.blit(bt,(self.xpos, self.ypos))


    def cc(self):
        mp = pygame.mouse.get_pos()
        lc = pygame.mouse.get_pressed()[0]
        bt = pygame.rect.Rect((self.xpos, self.ypos), (300, 50))
        if lc and bt.collidepoint(mp) and self.enabled:
            return True
        else:
            return False
