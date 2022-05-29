# Pygame шаблон - скелет для нового проекта Pygfme
import pygame
import random
import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder,'img')
player_img = pygame.image.load(os.path.join(img_folder,'maleperson.png'))

WIDTH = 500 # Щирина окна
HEIGHT = 600 # Высота окна
FPS = 30 #Частота кадров в секунду

#Colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Player1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,30))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH -30,HEIGHT - HEIGHT +30)
        self.speed = 5
    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom > HEIGHT:
            self.speed -= 10
        elif self.rect.top < 0:
            self.speed += 10
    

    
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100,100))
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2,HEIGHT/2)
    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

class Player2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH - WIDTH + 30,HEIGHT - HEIGHT + 30)

# Создаем окно игры
pygame.init()
pygame.mixer.init() #Для звука
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Шаблон') 
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
player1 = Player1()
player2 = Player2()
all_sprites.add(player)
all_sprites.add(player1)
all_sprites.add(player2)

# Цикл игры
running = True
while running:
    #Держим цикл на правильной скорости
    clock.tick(FPS)
    #Ввод событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #Обновление
    all_sprites.update()
    #Рендеринг или отрисовка
    screen.fill(BLUE)
    all_sprites.draw(screen)
    #посли отрисовки всего переворачиваем экран
    pygame.display.flip()
pygame.quit() 