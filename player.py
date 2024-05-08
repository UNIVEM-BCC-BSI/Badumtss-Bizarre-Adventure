import pygame
from math import floor

pygame.mixer.init()

pulo = pygame.mixer.Sound('musicas/sons/pulo.mp3')
pulo.set_volume(0.3)

CHAO = 530
JUMP_INDEX = 1
IDLE_INDEX = 0
RUN_INDEX = 2
PIANO_P_INDEX = 3
class Player():
    def __init__(self):
        self.images = [[pygame.image.load('Sprites/Badumtss/idle/idle_1.png').convert_alpha(),
                        pygame.image.load('Sprites/Badumtss/idle/idle_2.png').convert_alpha(),
                        pygame.image.load('Sprites/Badumtss/idle/idle_3.png').convert_alpha(),
                        pygame.image.load('Sprites/Badumtss/idle/idle_4.png').convert_alpha(),
                        pygame.image.load('Sprites/Badumtss/idle/idle_5.png').convert_alpha(),
                        pygame.image.load('Sprites/Badumtss/idle/idle_6.png').convert_alpha()], # idle
                       pygame.image.load('Sprites/Badumtss/jump.png').convert_alpha(), # pulo 
                        [pygame.image.load('Sprites/Badumtss/run/run_1.png').convert_alpha(),
                         pygame.image.load('Sprites/Badumtss/run/run_2.png').convert_alpha(),
                         pygame.image.load('Sprites/Badumtss/run/run_3.png').convert_alpha()],
                        [pygame.image.load('Sprites/Badumtss/piano/pianoplay_1.png').convert_alpha(),
                         pygame.image.load('Sprites/Badumtss/piano/pianoplay_2.png').convert_alpha(),
                         pygame.image.load('Sprites/Badumtss/piano/pianoplay_3.png').convert_alpha(),
                         pygame.image.load('Sprites/Badumtss/piano/pianoplay_4.png').convert_alpha()]] # andar

        self.image = self.images[IDLE_INDEX][0]
        self.rect = self.image.get_rect(midbottom=(80, CHAO))
        
        # animação
        self.anim = "idle"
        self.anim_index = 0

        self.andando = "idle"
        self.jumping = False
        self.gravity = 0
        self.speed = 2
        self.obstaculo = False

    def applyGravity(self, obstaculos):
        # Mantem o valor da gravidade no padrão - 20
        if self.gravity < 19: 
            self.gravity += 1
        # Caso não esteja durante o pulo
        else: 
            if self.anim in ["jump-left", "jump-right"]:
                self.anim = "idle"
                self.jumping = False
        
        if self.jumping or self.gravity < 0 and not self.obstaculo: #         
            self.rect.y += self.gravity  
            if self.anim == "jump-left" or self.anim == "left": 
                self.anim = "jump-left"
            else:
                self.anim = "jump-right"       
            print("Aplicando pulo")           
        
        (xant, yant) = (self.rect.left, self.rect.top)
        if self.rect.collidelistall(obstaculos) and self.jumping:
            self.anim = "idle"
            self.jumping = False
            self.obstaculo = True
            self.rect.left, self.rect.top = xant, yant
            print("Em obstaculo")

        if not self.jumping and not self.obstaculo and self.rect.midbottom[1] < CHAO:
            print("Corrigindo")
            self.rect.y += self.gravity 
            if self.rect.midbottom[1] > CHAO: 
                self.rect.y = 357
                

    def getImage(self):
        if self.anim == "idle":
            self.anim_index += 0.1
            if self.anim_index > 5: self.anim_index = 0
            self.image = self.images[IDLE_INDEX][floor(self.anim_index)]

        elif self.anim == "piano-play":
            self.anim_index += 0.1
            if self.anim_index > 3: self.anim_index = 0
            self.image = self.images[PIANO_P_INDEX][floor(self.anim_index)]

        elif self.anim == "left":
            self.anim_index += 0.1
            if self.anim_index > 2: self.anim_index = 0
            self.image = pygame.transform.flip(self.images[RUN_INDEX][floor(self.anim_index)], True, False)

        elif self.anim == "right":
            self.anim_index += 0.1
            if self.anim_index > 2: self.anim_index = 0
            self.image = self.images[RUN_INDEX][floor(self.anim_index)]

        elif self.anim == "jump-right":
            self.image = self.images[JUMP_INDEX]

        elif self.anim == "jump-left":
            self.image = pygame.transform.flip(self.images[JUMP_INDEX], True, False)



    def andar(self, obstaculos):
        (xant, yant) = (self.rect.left, self.rect.top)
             
        if self.speed < 5:
            self.speed += 1

        if self.andando == "right":
            if self.rect.right > 800:
                self.rect.x -= self.speed
            self.rect.x += self.speed

        elif self.andando == "left":
            if self.rect.left > 0:
                self.rect.x -= self.speed
        
        if self.rect.collidelistall(obstaculos):
            self.rect.left, self.rect.top = xant, yant

    def readkeys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if not self.jumping:
                self.gravity = -20
                self.jumping = True
                self.obstaculo = False
                print("Falso")
                pulo.play()

        if keys[pygame.K_a]:
            if not self.jumping: self.anim = "left"
            self.andando = "left"

        if keys[pygame.K_d]:
            if not self.jumping: self.anim = "right"
            self.andando = "right"

        if keys[pygame.K_e]:
            if not self.jumping and (self.rect.left > 230 and self.rect.right < 580):
                self.anim = "piano-play"
                self.andando = "idle"

        if not keys[pygame.K_d] and not keys[pygame.K_a] and not keys[pygame.K_e] and self.andando != "idle" and not self.jumping:
            if not self.jumping: self.anim = "idle"
            self.andando = "idle"
            self.speed = 2

    def draw(self, screen, obstaculos):
        self.getImage()
        self.applyGravity(obstaculos)
        self.andar(obstaculos)
        screen.blit(self.image, self.rect)
