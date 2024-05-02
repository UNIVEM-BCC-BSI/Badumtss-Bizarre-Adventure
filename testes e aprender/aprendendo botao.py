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
    def __init__(self,text,xpos,ypos,enabled):
        self.text=text
        self.xpos=xpos
        self.ypos=ypos
        self.enabled=enabled
        self.draw()

    def draw(self):
        tb = font.render(self.text,True,'black')
        bt = pygame.rect.Rect((self.xpos,self.ypos),(300,50))
        if self.enabled:
            if self.cc():
                pygame.draw.rect(screen,'dark gray',bt,0,5)

            else:
                pygame.draw.rect(screen,'light gray',bt,0,5)
        else:
            pygame.draw.rect(screen,'black',bt,0,5)
        pygame.draw.rect(screen,'black',bt,2,5)
        screen.blit(tb,(self.xpos+40,self.ypos+6))

    def cc(self):
        mp = pygame.mouse.get_pos()
        lc = pygame.mouse.get_pressed()[0]
        bt = pygame.rect.Rect((self.xpos, self.ypos), (300, 50))
        if lc and bt.collidepoint(mp) and self.enabled:
            return True
        else:
            return False
run = True
while run:
    screen.fill('white')
    timer.tick(fps)
    bot = Bott('NOVO JOGO',10,10,True)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()