import pygame

CHAO = 600
class Player():
    def __init__(self):
        self.images = [pygame.image.load('img/player/idle.png').convert_alpha(),
                       pygame.image.load('img/player/idle.png').convert_alpha(), # pulo
                       pygame.image.load('img/player/idle.png').convert_alpha()]
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=(80, CHAO))
        self.anim = "right"
        self.andando = "idle"
        self.gravity = 0
        self.speed = 2

    def applyGravity(self):
        if self.gravity < 20: self.gravity += 1
        if self.rect.midbottom[1] < CHAO or self.gravity < 0:
            self.rect.y += self.gravity

            if self.anim == "left" or self.anim == "up-left":
                self.anim = "down-left"

            elif self.anim == "right" or self.anim == "up-right":
                self.anim = "down-right"

    def getImage(self):
        if self.anim == "left":
            self.image = pygame.transform.flip(self.images[0], True, False)

        elif self.anim == "right":
            self.image = self.images[0]

        elif self.anim == "up-right":
            self.image = self.images[1]

        elif self.anim == "up-left":
            self.image = self.images[1]
            self.image = pygame.transform.flip(self.images[1], True, False)

        elif self.anim == "down-right":
            self.image = self.images[2]

        elif self.anim == "down-left":
            self.image = self.images[2]
            self.image = pygame.transform.flip(self.images[2], True, False)

    def andar(self, obstaculos):
        if not self.rect.collidelistall(obstaculos):
            if self.speed < 5:
                self.speed += 1

            if self.andando == "right":
                if self.rect.right > 800:
                    self.rect.x -= self.speed
                self.rect.x += self.speed

            elif self.andando == "left":
                if self.rect.left > 0:
                    self.rect.x -= self.speed
        else:
            print("colisao")

    def readkeys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if self.rect.midbottom[1] >= CHAO:
                self.gravity = -20

        if keys[pygame.K_a]:
            self.anim = "left"
            self.andando = "left"

        if keys[pygame.K_d]:
            self.anim = "right"
            self.andando = "right"

        if not keys[pygame.K_d] and not keys[pygame.K_a]:
            self.andando = "idle"
            self.speed = 2

    def draw(self, screen, obstaculos):
        self.getImage()
        self.applyGravity()
        self.andar(obstaculos)
        screen.blit(self.image, self.rect)
