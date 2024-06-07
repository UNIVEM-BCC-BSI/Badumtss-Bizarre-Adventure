import pygame
from random import choice
from player import Player
from botoes import Bott
from obstaculos import Obstaculo
from piano import Piano
from notas import Notas
from balao import Balao, Balao2, Velho
from portal import Portal, Portal2
from npc import Npc, Npc2
from tela_pergunta import Pergunta
score = 0

pygame.init()

def alterarTelaJogo(telaj):
    global screen, tela, obstaculos, player, VIDA
    pygame.display.set_mode((800, 600))
    if telaj == 1:
        tela = 1
    
    if telaj == 4: 
        tela = 4
        GerarFase()

    elif telaj == 6:
        tela = 6
        player.alterar_tamanho(0, (80, 530))
        obstaculos =[]

    elif telaj == 5:
        tela = 5  
        player.alterar_tamanho(1, (125, 545))
        obstaculos = [Obstaculo(30, 462, "Sprites/fase1/plat1.png"), 
                      Obstaculo(67, 361, "Sprites/fase1/plat1.png"),
                      Obstaculo(509, 392, "Sprites/fase1/plat1.png"),
                      Obstaculo(393, 91, "Sprites/fase1/plat1.png"),
                      Obstaculo(392, 289, "Sprites/fase1/plat1.png"),
                      Obstaculo(781, 228, "Sprites/fase1/plat1.png"),
                      Obstaculo(546, 226, "Sprites/fase1/plat1.png"),
                      Obstaculo(155, 306, "Sprites/fase1/plat1.png"),
                      Obstaculo(96, 224, "Sprites/fase1/plat1.png"),
                      Obstaculo(144, 123, "Sprites/fase1/plat1.png"),
                      Obstaculo(69, 50, "Sprites/fase1/plat1.png"),
                      Obstaculo(672, 398, "Sprites/fase1/c12.png"),
                      Obstaculo(616, 495, "Sprites/fase1/c11.png"),
                      Obstaculo(561, 514, "Sprites/fase1/c10.png"),
                      Obstaculo(499, 544, "Sprites/fase1/c9.png"),
                      Obstaculo(664, 151, "Sprites/fase1/c13.png"),
                      Obstaculo(0, 184, "Sprites/fase1/c8.png"),
                      Obstaculo(0, 258, "Sprites/fase1/c7.png"),
                      Obstaculo(0, 328, "Sprites/fase1/c6.png"),
                      Obstaculo(453, 38, "Sprites/fase1/c15.png"),
                      Obstaculo(536, 1, "Sprites/fase1/c16.png"),
                      Obstaculo(432, 38, "Sprites/fase1/c14.png"),
                      Obstaculo(88, 544, "Sprites/fase1/c1.png"),
                      Obstaculo(172, 435, "Sprites/fase1/c2.png"),
                      Obstaculo(214, 330, "Sprites/fase1/c3.png"),
                      Obstaculo(214, 258, "Sprites/fase1/c4.png"),
                      Obstaculo(214, 43, "Sprites/fase1/c5.png")]

def GerarFase():
    global notas, player, PLAYER_NOTAS, VIDA, NOTA_INDEX, obstaculos, MORTO, balao, portal, score
    notas = [Notas(181,403,20,20),
         Notas(169,275,20,20),
         Notas(19,153,20,20),
         Notas(81,19,20,20),
         Notas(265,12,20,20),
         Notas(504,8,20,20),
         Notas(404,257,20,20),
         Notas(559,194,20,20),
         Notas(695,119,20,20),
         Notas(522,360,20,20),
         Notas(516,511,20,20),
         Notas(639,462,20,20)]
    obstaculos = []
    player = Player()
    PLAYER_NOTAS = 0
    VIDA = 4
    NOTA_INDEX = 0
    MORTO = -1
    portal.cont = 0
    score = 0
    balao = Balao(80, 233, "Meu nome é Avô! (Aperte Q para interagir)", key=pygame.K_q)

#TAMANHO TELA
sw = 898
sh = 600#897
screen = pygame.display.set_mode((sw,sh))
clock = pygame.time.Clock()

# FASES
FASE_1 = 5

# Vida
VIDA_IMAGENS = [
    pygame.image.load("Sprites/vida/vida_0.png").convert_alpha(),
    pygame.image.load("Sprites/vida/vida_1.png").convert_alpha(),
    pygame.image.load("Sprites/vida/vida_2.png").convert_alpha(),
    pygame.image.load("Sprites/vida/vida_3.png").convert_alpha(),
    pygame.image.load("Sprites/vida/vida_4.png").convert_alpha()
]
def renderizarVida(screen):
    global VIDA
    VIDA_IMG = VIDA_IMAGENS[VIDA]
    screen.blit(VIDA_IMG, (700, 10))

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
pygame.mixer.music.set_volume(0.1)
mb.set_volume(0.1)
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

# EVENTOS
ti = pygame.USEREVENT + 1
FASE1_TEXTO_NPC = pygame.USEREVENT + 2
CLICK_CORRETO_PERGUNTA = pygame.USEREVENT + 3
TIMER_MORTO = pygame.USEREVENT + 4
TIMER_OCULTAR_VELHO = pygame.USEREVENT + 5

pygame.time.set_timer(ti, 30)

# OBSTACULOS
obstaculos = []

#PENTAGRAMA
nota = pygame.image.load('imgs_part/notas_a_pegar.png')
nota = pygame.transform.scale(nota, (30, 30))

# Quarto
quarto = pygame.image.load('Sprites/quarto/quarto2.png')
piano = Piano(300, 316)
portal = Portal(500, 300)
portal2 = Portal2(757, 340)
npc2 = Npc2(150, 265)
npc = Npc(200, 265)
balao = Balao(80, 233, "Meu nome é Avô! (Aperte Q para interagir)", key=pygame.K_q)
balao2 = Balao2(60, 233, "Agora que recuperou as notas, toque seu piano!", key=pygame.K_q)

# Fase 1
GerarFase()
fase1_bg = pygame.image.load('Sprites/fase1/ref.png') # fase1-fundo
NOTAS_CORRETAS = ["mi", "re#", "mi", "re#", "mi", "si", "re", "do", "la", "do", "mi", "la", "re", "mi", "sol#", "si", "do"]
NOTAS_POSSIVEIS = ["do", "re", "mi", "fa", "sol", "la", "si", "do", "re#", "mi#", "fa#", "do#", "sol#", "la#"]
PERGUNTA = Pergunta()
pergunta_mostrando = False
pode_mover = True
velho = Velho("Você recuperou todas as notas. Volte para o portal.")

while run:
    if tela == 6:
        screen.blit(quarto, (0, 0))
        piano.draw(screen, player)
        balao2.draw(screen)

        npc2.draw(screen, player)
        player.draw(screen, obstaculos, 7)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] and npc2.rect.colliderect(player):  
            pygame.time.set_timer(FASE1_TEXTO_NPC, 500, 1)
        

    if tela == FASE_1:
        screen.blit(fase1_bg, (0, 0))
        player.draw(screen, obstaculos, PLAYER_NOTAS, pode_mover, VIDA)
        if player.rect.y > 610:
            player.alterar_tamanho(1, (125, 545))

        # Morto
        if VIDA == 0 and MORTO == -1:
            MORTO = 5
            pygame.time.set_timer(TIMER_MORTO, 1000, 5)

        # Renderização obstaculos
        for n in obstaculos:
            n.draw(screen)

        # Renderização notas
        for n in notas:
            n.draw(screen)      
            # Colidir com nota     
            if n.colisao(player):
                notas.remove(n)
                lista = [NOTAS_CORRETAS[NOTA_INDEX]]
                while len(lista) < 4:
                    nota = choice(NOTAS_POSSIVEIS)
                    if nota not in lista:
                        lista.append(nota)

                PERGUNTA = Pergunta(NOTA_INDEX, lista)
                pergunta_mostrando = True
                pode_mover = False

        # Portal
        if NOTA_INDEX >= 12:
            portal2.draw(screen, player)
        
        if portal2.cont != 0:
            alterarTelaJogo(6)

        if pergunta_mostrando:
            PERGUNTA.draw(screen)

        if MORTO > 0:
            TELA_MORREU = pygame.Surface((800, 600), pygame.SRCALPHA)
            TELA_MORREU.fill((0, 0, 0, 190))
            fonte = pygame.font.Font(None, 45)

            txt = fonte.render("MORTO... CONTINUANDO EM", True, "red")
            TELA_MORREU.blit(txt, (400 - txt.get_width() / 2, 200))

            fonte = pygame.font.Font(None, 60)
            txt = fonte.render(f"{MORTO}", True, "white")
            TELA_MORREU.blit(txt, (400 - txt.get_width() / 2, 250))
            screen.blit(TELA_MORREU, (0,0))

        renderizarVida(screen)
        velho.draw(screen)

    if tela == 4:
        screen.blit(quarto, (0, 0))
        piano.draw(screen, player)
        balao.draw(screen)

        npc.draw(screen, player)
        player.draw(screen, obstaculos, PLAYER_NOTAS)
        if balao.getContador() == 4: portal.draw(screen, player)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] and npc.rect.colliderect(player):  
            pygame.time.set_timer(FASE1_TEXTO_NPC, 500, 1)
        
        if portal.cont != 0:
            alterarTelaJogo(5)

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
                alterarTelaJogo(4)

        if medio.cc():
 
            mb.play()
            #pygame.mouse.set_visible(False)
            if event.type == ti:
                pygame.mixer.music.pause()
                alterarTelaJogo(4)

        if facil.cc():
 
            #pygame.mouse.set_visible(False)
            if event.type == ti:
                pygame.mixer.music.pause()
                alterarTelaJogo(4)

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
            pygame.mixer.music.pause()
            mb.play()
            if event.type == ti:
               alterarTelaJogo(4)
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

        if event.type == FASE1_TEXTO_NPC:
            if balao.getContador() < 4: balao.addContador()
            if balao.getContador() == 1:        
                balao.alterar_texto("Não consegue tocar seu piano, não é? [...]")
            elif balao.getContador() == 2:
                balao.alterar_texto('Algumas notas de sua partitura fugiram [...]')
            elif balao.getContador() == 3:
                balao.alterar_texto('Colete as notas e poderá tocar seu piano novamente! [...]')
            elif balao.getContador() == 4:
                balao.alterar_texto("Entre pelo portal e começe sua jornada!")

        if event.type == CLICK_CORRETO_PERGUNTA:
            if PERGUNTA.ClicouCorreto:
                score += 1
            else:
                VIDA -= 1
            
            NOTA_INDEX += 1
            pergunta_mostrando = False
            pode_mover = True

            if NOTA_INDEX == 12:
                velho.mostrar("Você recuperou as notas. Volte para o portal.")
                pode_mover = False  

        if event.type == TIMER_MORTO:
            MORTO -= 1
            if MORTO == 0:
                alterarTelaJogo(1)

        if event.type == TIMER_OCULTAR_VELHO:
            velho.ocultar()
            pode_mover = True

        player.readkeys()

    # if pygame.mouse.get_pressed()[0] and tela > 4:
    #     print(pygame.mouse.get_pos())
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()