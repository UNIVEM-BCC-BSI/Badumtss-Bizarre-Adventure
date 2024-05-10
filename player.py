import pygame
from math import floor

pygame.mixer.init()

pulo = pygame.mixer.Sound('musicas/sons/pulo.mp3')
pulo.set_volume(0.3)

CHAO = 530

# Index de animações
JUMP_INDEX = 1
IDLE_INDEX = 0
RUN_INDEX = 2
PIANO_P_INDEX = 3

SIZE_GRANDE = 0
SIZE_PEQUENO = 1
class Player():
    def __init__(self):
        self.images = [ # SIZE_GRANDE
                        [[pygame.image.load('Sprites/Badumtss/idle/idle_1.png').convert_alpha(), # idle
                        pygame.image.load('Sprites/Badumtss/idle/idle_2.png').convert_alpha(), # idle
                        pygame.image.load('Sprites/Badumtss/idle/idle_3.png').convert_alpha(), # idle
                        pygame.image.load('Sprites/Badumtss/idle/idle_4.png').convert_alpha(), # idle
                        pygame.image.load('Sprites/Badumtss/idle/idle_5.png').convert_alpha(), # idle
                        pygame.image.load('Sprites/Badumtss/idle/idle_6.png').convert_alpha()], # idle
                        pygame.image.load('Sprites/Badumtss/jump.png').convert_alpha(), # pulo 
                        [pygame.image.load('Sprites/Badumtss/run/run_1.png').convert_alpha(), # andar
                         pygame.image.load('Sprites/Badumtss/run/run_2.png').convert_alpha(), # andar
                         pygame.image.load('Sprites/Badumtss/run/run_3.png').convert_alpha()], # andar
                        [pygame.image.load('Sprites/Badumtss/piano/pianoplay_1.png').convert_alpha(), # piano
                         pygame.image.load('Sprites/Badumtss/piano/pianoplay_2.png').convert_alpha(), # piano
                         pygame.image.load('Sprites/Badumtss/piano/pianoplay_3.png').convert_alpha(), # piano
                         pygame.image.load('Sprites/Badumtss/piano/pianoplay_4.png').convert_alpha()]], 
                        
                        # SIZE_PEQUENO
                        [[pygame.image.load('Sprites/Badumtss-menor/idle/idle_1.png').convert_alpha(), # idle
                        pygame.image.load('Sprites/Badumtss-menor/idle/idle_2.png').convert_alpha(), # idle
                        pygame.image.load('Sprites/Badumtss-menor/idle/idle_3.png').convert_alpha(), # idle
                        pygame.image.load('Sprites/Badumtss-menor/idle/idle_4.png').convert_alpha(), # idle
                        pygame.image.load('Sprites/Badumtss-menor/idle/idle_5.png').convert_alpha(), # idle
                        pygame.image.load('Sprites/Badumtss-menor/idle/idle_6.png').convert_alpha()], # idle
                        pygame.image.load('Sprites/Badumtss-menor/jump.png').convert_alpha(), # pulo 
                        [pygame.image.load('Sprites/Badumtss-menor/run/run_1.png').convert_alpha(), # andar
                         pygame.image.load('Sprites/Badumtss-menor/run/run_2.png').convert_alpha(), # andar
                         pygame.image.load('Sprites/Badumtss-menor/run/run_3.png').convert_alpha()]]] 

        self.image = self.images[SIZE_GRANDE][IDLE_INDEX][0]
        self.rect = self.image.get_rect(midbottom=(80, CHAO))

        # animação
        self.anim = "idle"
        self.anim_index = 0
        self.size = SIZE_GRANDE

        self.andando = "idle"
        self.jumping = False
        self.gravity = 0
        self.speed = 2
        self.obstaculo = 0
        self.em_obstaculo = False

    def applyGravity(self, obstaculos):
        # Mantem o valor da gravidade no padrão: 20
        if self.jumping and self.gravity < 20:
            self.gravity += 1

        # Caso não esteja durante o pulo e não está em contato com um obstáculo
        else:
            if self.anim in ["jump-left", "jump-right"]:
                self.anim = "idle"
                self.jumping = False
                self.em_obstaculo = False

        if not self.jumping and self.size == SIZE_PEQUENO and self.gravity < 0:
            self.gravity = 10

        # Se o jogador estiver pulando ou não estiver em contato com um obstáculo
        if self.jumping or (self.rect.midbottom[1] < CHAO and not self.em_obstaculo and self.size == SIZE_GRANDE) or (self.size == SIZE_PEQUENO and not self.em_obstaculo):
            self.rect.y += self.gravity

            if self.anim == "jump-left" or self.anim == "left":
                self.anim = "jump-left"
            else:
                self.anim = "jump-right"

            if not self.em_obstaculo:
                for pos, obstaculo in enumerate(obstaculos):
                    if self.rect.colliderect(obstaculo.rect):
                        if not obstaculo.chao and self.rect.bottom > obstaculo.rect.top: 
                            self.rect.bottom = obstaculo.rect.top
                            self.em_obstaculo = True
                            self.obstaculo = pos
                            self.gravity = 0
                            self.anim = "idle"
                            self.jumping = False
                        else: 
                            self.rect.top = obstaculo.rect.bottom + 1
                            self.gravity = 1
                        
                        break 

            if self.rect.midbottom[1] > CHAO and self.size == SIZE_GRANDE:
                self.rect.y = 357

        # Reinicia o índice do obstáculo se não houver mais colisão
        if self.em_obstaculo:
            lista = list(range(obstaculos[self.obstaculo].rect.topleft[0], obstaculos[self.obstaculo].rect.topright[0]))
            if self.rect.bottomleft[0] + 1 not in lista and self.rect.bottomright[0] + 1 not in lista: 
                self.obstaculo = 0
                self.em_obstaculo = False
                self.jumping = True


    def getImage(self):
        if self.anim == "idle":
            self.anim_index += 0.1
            if self.anim_index > 5: self.anim_index = 0
            self.image = self.images[self.size][IDLE_INDEX][floor(self.anim_index)]

        elif self.anim == "piano-play":
            self.anim_index += 0.1
            if self.anim_index > 3: self.anim_index = 0
            self.image = self.images[self.size][PIANO_P_INDEX][floor(self.anim_index)]

        elif self.anim == "left":
            self.anim_index += 0.1
            if self.anim_index > 2: self.anim_index = 0
            self.image = pygame.transform.flip(self.images[self.size][RUN_INDEX][floor(self.anim_index)], True, False)

        elif self.anim == "right":
            self.anim_index += 0.1
            if self.anim_index > 2: self.anim_index = 0
            self.image = self.images[self.size][RUN_INDEX][floor(self.anim_index)]

        elif self.anim == "jump-right":
            self.image = self.images[self.size][JUMP_INDEX]

        elif self.anim == "jump-left":
            self.image = pygame.transform.flip(self.images[self.size][JUMP_INDEX], True, False)

        self.rect = self.image.get_rect(x=self.rect.x, y=self.rect.y)


    def andar(self, obstaculos):
        (xant, yant) = (self.rect.left, self.rect.top)
             
        if self.speed < 5 and self.size == SIZE_GRANDE:
            self.speed += 1

        elif self.speed < 2 and self.size == SIZE_PEQUENO:
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
                self.em_obstaculo = False
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

    def alterar_tamanho(self, tamanho, xy):
        self.size = tamanho
        self.rect = self.image.get_rect(x=xy[0], y=xy[1])
        self.andando = "idle"
        self.anim = "idle"

    def draw(self, screen, obstaculos):
        self.getImage()
        self.applyGravity(obstaculos)
        self.andar(obstaculos)
        screen.blit(self.image, self.rect)
