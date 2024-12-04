import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1600, 1200
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Movable Blue Triangle")

# Define colors
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)





# Triangle properties
center_x, center_y = width // 2, height // 2
size = 50
angle = 0
speed = 5

def rotate_point(x, y, cx, cy, angle):
    radians = math.radians(angle)
    cos_val = math.cos(radians)
    sin_val = math.sin(radians)
    print(x, cx, y, cy)
    nx = cos_val * (x - cx) - sin_val * (y - cy) + cx
    ny = sin_val * (x - cx) + cos_val * (y - cy) + cy
    
    return nx, ny

def draw_triangle():
    points = [(center_x, center_y - size), (center_x - size, center_y + size), (center_x + size, center_y + size)]
    print(points)
    for x, y in points: print(x, y)
    
    rotated_points = [rotate_point(x, y, center_x, center_y, angle) for x, y in points]
    
    
    pygame.draw.polygon(screen, BLUE, rotated_points)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        center_x += speed * math.sin(math.radians(angle))
        center_y -= speed * math.cos(math.radians(angle))
    if keys[pygame.K_s]:
        center_x -= speed * math.sin(math.radians(angle))
        center_y += speed * math.cos(math.radians(angle))
    if keys[pygame.K_a]:
        angle += 3
    if keys[pygame.K_d]:
        angle -= 3

    # Keep the triangle within the window bounds
    center_x = max(size, min(width - size, center_x))
    center_y = max(size, min(height - size, center_y))

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the blue triangle
    draw_triangle()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()