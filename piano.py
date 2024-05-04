import pygame
from math import floor

pygame.mixer.init()
musica = pygame.mixer.Sound('musicapiano.mp3')

class Piano():
    # carregamento do piano.
    def __init__(self, x, y):
        self.y = y
        self.x = x
        self.images = [pygame.image.load('Sprites/piano/pianoidle.png'), # idle
                       [pygame.image.load('Sprites/piano/pianomusic_1.png'), # playing 1-3
                        pygame.image.load('Sprites/piano/pianomusic_2.png'),
                        pygame.image.load('Sprites/piano/pianomusic_3.png')]]
        self.image = self.images[0]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.anim_index = 0
        self.anim = "idle"

    # Desenha o piano
    def draw(self, screen, player):
        # verifica se o player esta tocando piano em cima do piano
        if self.rect.colliderect(player.rect) and player.anim == "piano-play":
            self.anim = "play"
            musica.play()
        else:
            self.anim = "idle"
            musica.stop()

        # aplica animação ao piano. idle = parado.
        if self.anim == "idle":
            self.image = self.images[0]
        else:
            # index de animação. floor deixa o numero arredondado.
            self.anim_index += 0.1
            if self.anim_index > 2: self.anim_index = 0
            self.image = self.images[1][floor(self.anim_index)]

        screen.blit(self.image, self.rect)

