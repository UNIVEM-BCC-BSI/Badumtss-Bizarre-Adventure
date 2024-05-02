import pygame
from player import Player
from botoes import Bott
from obstaculos import Obstaculo

pygame.init()

def alterarTelaJogo():
    global screen, tela
    pygame.display.set_mode((800, 600))
    tela = 4

#TAMANHO TELA
sw = 898
sh = 897
screen = pygame.display.set_mode((sw,sh))
clock = pygame.time.Clock()

#ICONE
icon = pygame.image.load('img/player/SPRITE.png')
pygame.display.set_icon(icon)

#MUSICA
pygame.mixer.init()
mb = pygame.mixer.Sound('botao.mp3')
pygame.mixer.music.load('MUSICA.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.3)
mb.set_volume(0.5)

#VARIAVEIS

cj = False

#NOME DA ABA
pygame.display.set_caption('Badumtss Bizarre Adventure')


#FUNDO
fundo = pygame.image.load('img/telaprincipal.png')
cre = pygame.image.load('img/tela.creditos.png')
difi = pygame.image.load('img/tela.dificuldade.png')

tela = 1
run = True

ti = pygame.USEREVENT + 1
pygame.time.set_timer(ti, 70)
player = Player()
obstaculos = [Obstaculo(300, 450, 30, 90), Obstaculo(450, 530, 30, 90)]

while run:
    if tela == 4:
        screen.fill('gray')
        player.draw(screen, obstaculos)
        for n in obstaculos:
            n.draw(screen)

    if tela == 3:
        screen.blit(difi,(-2,-2))
        dificil = Bott('img/dificil.png','img/dificil.click.png',285,700,True, screen)
        medio = Bott('img/medio.png','img/medio.click.png',285,550,True, screen)
        facil = Bott('img/facil.png','img/facil.click.png',285,400,True, screen)
        voltar = Bott('img/voltar.png', 'img/voltar.click.png', 550, 800, True, screen)
        if voltar.cc():
            mb.play()
            if event.type == ti:
                tela = 1
        if dificil.cc():
            mb.play()
            #pygame.mouse.set_visible(False)
            if event.type == ti:
                pygame.mixer.music.pause()
                alterarTelaJogo()

        if medio.cc():
            mb.play()
            #pygame.mouse.set_visible(False)
            if event.type == ti:
                pygame.mixer.music.pause()
                alterarTelaJogo()

        if facil.cc():
            mb.play()
            #pygame.mouse.set_visible(False)
            if event.type == ti:
                pygame.mixer.music.pause()
                alterarTelaJogo()

    if tela == 1:
        screen.blit(fundo, (0, 0))
        bot2 = Bott('img/creditos.png','img/creditos.click.png',285,570,True, screen)
        bot3 = Bott('img/sair.png','img/sair.click.png',285,656,True, screen)
        bot = Bott('img/novojogo.png', 'img/novojogo.click.png', 285, 484, True, screen)
        if bot2.cc():
            mb.play()
            if event.type == ti:
                tela = 2
        if bot.cc():
            mb.play()
            if event.type == ti:
               tela = 3
        if bot3.cc():
            mb.play()
            if event.type == ti:
                run = False
    if tela == 2:
        screen.blit(cre, (-3, -3))
        bot = Bott('img/voltar.png', 'img/voltar.click.png', 550, 800, True, screen)
        if bot.cc():
            mb.play()
            if event.type == ti:
                tela = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        player.readkeys()

    pygame.display.update()
    clock.tick(60)

pygame.quit()