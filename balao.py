import pygame

class Balao():
    def __init__(self, x, y, text, enabled=True, key=pygame.K_e, antialias=True, color="white", bg=(0, 0, 0, 128)):
        self.x = x
        self.y = y
        self.text = text
        self.enabled = enabled
        self.key = key
        self.antialias = antialias
        self.color = color
        self.bg = bg
        self.contador = 0

        self.criar_texto()

    def criar_texto(self):
        # Cria a fonte e o texto
        fonte_balao = pygame.font.Font(None, 35)
        text_surface = fonte_balao.render(self.text, self.antialias, self.color)
        text_rect = text_surface.get_rect()
        # Cria o fundo, tendo o tamanho do texto + 4px X e Y
        self.image = pygame.Surface((text_rect.width + 4, text_rect.height + 4), pygame.SRCALPHA)
        self.image.fill(self.bg) 
        # Centraliza o texto no meio da caixa
        text_position = ((self.image.get_width() - text_surface.get_width()) // 2, (self.image.get_height() - text_surface.get_height()) // 2)
        # Insere o texto na caixa
        self.image.blit(text_surface, text_position)  
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
    
    def alterar_texto(self, texto):
        self.text = texto
        self.criar_texto()

    def check_player(self, player):
        # Verfica se a tecla de interação está pressionada e se o player está no range.
        keys = pygame.key.get_pressed()
        if keys[self.key] and self.rect.colliderect(player) and self.enabled:
            return True
        else:
            return False
        
    def addContador(self):
        self.contador += 1
    
    def getContador(self):
        return self.contador

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class Balao2():
    def __init__(self, x, y, text, enabled=True, key=pygame.K_e, antialias=True, color="white", bg=(0, 0, 0, 128)):
        self.x = x
        self.y = y
        self.text = text
        self.enabled = enabled
        self.key = key
        self.antialias = antialias
        self.color = color
        self.bg = bg
        self.contador = 0

        self.criar_texto()

    def criar_texto(self):
        # Cria a fonte e o texto
        fonte_balao = pygame.font.Font(None, 35)
        text_surface = fonte_balao.render(self.text, self.antialias, self.color)
        text_rect = text_surface.get_rect()
        # Cria o fundo, tendo o tamanho do texto + 4px X e Y
        self.image = pygame.Surface((text_rect.width + 4, text_rect.height + 4), pygame.SRCALPHA)
        self.image.fill(self.bg) 
        # Centraliza o texto no meio da caixa
        text_position = ((self.image.get_width() - text_surface.get_width()) // 2, (self.image.get_height() - text_surface.get_height()) // 2)
        # Insere o texto na caixa
        self.image.blit(text_surface, text_position)  
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
    
    def alterar_texto(self, texto):
        self.text = texto
        self.criar_texto()

    def check_player(self, player):
        # Verfica se a tecla de interação está pressionada e se o player está no range.
        keys = pygame.key.get_pressed()
        if keys[self.key] and self.rect.colliderect(player) and self.enabled:
            return True
        else:
            return False
        
    def addContador(self):
        self.contador += 1
    
    def getContador(self):
        return self.contador

    def draw(self, screen):
        screen.blit(self.image, self.rect)