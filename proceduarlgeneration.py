# Program: Procedural Generation in Pygame: An Intro

# Import the necessary libraries
import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Procedural Generation in Pygame")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define the player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += 5

# Define the enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.y += random.randint(1, 5)

# Create sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create enemies
for _ in range(100):
    enemy = Enemy()
    enemy.rect.x = random.randint(0, screen_width - enemy.rect.width)
    enemy.rect.y = random.randint(-100, -50)
    all_sprites.add(enemy)
    enemies.add(enemy)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update
    all_sprites.update()

    # Collision detection
    hits = pygame.sprite.spritecollide(player, enemies, True)
    if hits:
        player.rect.y -= 50

    # Render
    screen.fill(GREEN)
    all_sprites.draw(screen)
    pygame.display.flip()

    # FPS control
    clock.tick(10)

# Quit the game
pygame.quit()