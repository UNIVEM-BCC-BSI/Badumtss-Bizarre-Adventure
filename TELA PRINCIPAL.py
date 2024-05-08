import pygame
from player import Player
from botoes import Bott
from obstaculos import Obstaculo
from piano import Piano
from notas import Notas
from balao import Balao
as
score = 0

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
icon = pygame.image.load('Sprites/Badumtss/jump.png')
pygame.display.set_icon(icon)

#MUSICA/SONS
pygame.mixer.init()
mb = pygame.mixer.Sound('musicas/sons/botao.mp3')
do = pygame.mixer.Sound('musicas/sons/do.mp3')
re = pygame.mixer.Sound('musicas/sons/re.mp3')
mi = pygame.mixer.Sound('musicas/sons/mi.mp3')
fa = pygame.mixer.Sound('musicas/sons/fa.mp3')
sol = pygame.mixer.Sound('musicas/sons/sol.mp3')
la = pygame.mixer.Sound('musicas/sons/la.mp3')
si = pygame.mixer.Sound('musicas/sons/si.mp3')
pygame.mixer.music.load('musicas/MUSICA.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)
mb.set_volume(0.5)
toca = True

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
pygame.time.set_timer(ti, 30)
player = Player()

# OBSTACULOS
obstaculos = [Obstaculo(600, 400, 40, 150)]

notas = [Notas(600,450,20,20),
         Notas(500,450,20,20),
         Notas(400,450,20,20),
         Notas(300,450,20,20)
         ]
#PENTAGRAMA
penta = pygame.image.load('img/penta2.png')
penta = pygame.transform.scale(penta, (600, 400))
nota = pygame.image.load('img/minima.png')
nota = pygame.transform.scale(nota, (30, 30))


balao = Balao(400, 400, "Texto", key=pygame.K_q)


# Quarto
quarto = pygame.image.load('Sprites/quarto/quarto2.png')
piano = Piano(300,316)
tocador = True
while run:
    if tela == 4:
        screen.blit(quarto, (0, 0))
        screen.blit(penta,(-150, -100))
        piano.draw(screen, player)
        player.draw(screen, obstaculos)
        
        for n in obstaculos:
            n.draw(screen)

        for n in notas:
            n.draw(screen)           
            if n.colisao(player):
                notas.remove(n)
                score+=1
                print(score)
                if score == 1:
                    sol.play()
                if score == 2:
                    si.play()
                if score == 3:
                    re.play()
                if score == 4:
                    si.play()

        balao.draw(screen)
        if balao.check_player(player): 
            if balao.getContador() == 0:
                print("Playerasjalsja")
            else:
                balao.alterar_texto("obaaaaaaaaa")
            balao.addContador() 
            
        if score == 1:
            screen.blit(nota, (60,90))
        if score == 2:
            screen.blit(nota, (60,90))
            screen.blit(nota, (90,75))
        if score == 3:
            screen.blit(nota, (60,90))
            screen.blit(nota, (90,75))
            screen.blit(nota, (120,60))
        if score == 4:
            screen.blit(nota, (60,90))
            screen.blit(nota, (90,75))
            screen.blit(nota, (120,60))
            screen.blit(nota, (150,75))

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