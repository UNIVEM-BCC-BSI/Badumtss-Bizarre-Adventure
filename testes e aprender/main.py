import pygame

pygame.init()

#TAMANHO TELA
sw = 1024
sh = 1024
screen = pygame.display.set_mode((sw,sh))

#VARIAVEIS

cj = False

#NOME DA ABA
pygame.display.set_caption('Badumtss Bizarre Adventure')
#FONTE E TAMANHO
f = pygame.font.SysFont('Crang',50)
f2 = pygame.font.SysFont('04B_30',50)
#COR LETRA
tc = (0,0,0)


#FUNDO
fundo = pygame.image.load('../img/img1.jpg')
fundo2 = pygame.image.load('../img/idle.png')
screen.blit(fundo,(0,0))
screen.blit(fundo2,(412,712))

def dt (t,f,tc,x,y):
    img=f.render(t,True,tc)
    screen.blit(img,(x,y))

def tg (t, f, tc, x, y):
    img2 = f.render(t, True, tc)
    screen.blit(img2, (x, y))

def tg2 (t, f, tc, x, y):
    img3 = f.render(t, True, tc)
    screen.blit(img3, (x, y))

def tg3 (t, f, tc, x, y):
    img4 = f.render(t, True, tc)
    screen.blit(img4, (x, y))


run = True
while run:

    if cj == True:
        screen.fill((0,0,0))
        pass
    else:
        #screen.fill((52,78,91))
        dt('Aperte o <SPACE> para iniciar',f,tc, 50,512)
        tg('BADUMTSS', f2, tc, 320, 250)
        tg2('BIZARRE', f2, tc, 360, 300)
        tg3('ADVENTURE', f2, tc, 300, 350)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cj = True
                print('entrou')
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()