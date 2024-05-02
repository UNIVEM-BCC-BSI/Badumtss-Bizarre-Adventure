import pygame
pygame.init()
w = 500
h = 500
fps = 60
screen = pygame.display.set_mode([w,h])
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf',32)
pygame.display.set_caption('botão')

class Bott:
    def __init__(self,nome,xpos,ypos,enabled):
        self.nome=nome
        self.xpos=xpos
        self.ypos=ypos
        self.enabled=enabled
        self.draw()

    def draw(self):
        bt = pygame.image.load(self.nome)
        bt = pygame.transform.scale(bt,(70,20))
        screen.blit(bt,(self.xpos, self.ypos))


    def cc(self):
        mp = pygame.mouse.get_pos()
        lc = pygame.mouse.get_pressed()[0]
        bt = pygame.rect.Rect((self.xpos, self.ypos), (300, 50))
        if lc and bt.collidepoint(mp) and self.enabled:
            return True
        else:
            return False


run = True
tela = 1
while run:
    timer.tick(fps)
    if tela == 1:
        screen.fill('white')
        bot = Bott('novojogo.png', 104, 255, True)
        if bot.cc():
            tela = 2
    else:
        screen.fill('red')
        bot = Bott('novojogo.png', 104, 255, True)
        if bot.cc():
            tela = 1


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()