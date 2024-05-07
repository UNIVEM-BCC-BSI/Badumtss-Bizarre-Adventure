import pygame

'''
balao = Balao(400, 400, "Texto")
balao.draw(screen)
if balao.check_player(player): print("Playerasjalsja")
'''

class Balao():
    def __init__(self, x, y, text, enabled=True, key=pygame.K_e, antialias=True, color="white", bg=(0, 0, 0, 128)):
        self.x = x
        self.y = y
        self.text = text
        self.key = key
        self.enabled = enabled

        # Cria a fonte e o texto
        fonte_balao = pygame.font.Font(None, 35)
        text_surface = fonte_balao.render(text, antialias, color)
        text_rect = text_surface.get_rect()
        # Cria o fundo, tendo o tamanho do texto + 4px X e Y
        self.image = pygame.Surface((text_rect.width+4, text_rect.height+4), pygame.SRCALPHA)
        self.image.fill(bg) 
        # Centraliza o texto no meio da caixa
        text_position = ((self.image.get_width() - text_surface.get_width()) // 2, (self.image.get_height() - text_surface.get_height()) // 2)
        # Insere o texto na caixa
        self.image.blit(text_surface, text_position)  
        self.rect = self.image.get_rect(topleft=(x, y))
    
    def check_player(self, player):
        # Verfica se a tecla de interação está pressionada e se o player está no range.
        keys = pygame.key.get_pressed()
        if keys[self.key] and self.rect.colliderect(player) and self.enabled:
            return True
        else:
            return False

    def draw(self, screen):
        screen.blit(self.image, self.rect)