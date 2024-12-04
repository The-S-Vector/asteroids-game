# import pygame
# import time
# import sys
# import random
# import math
# from math import cos, sin, pi

# pygame.init()

# black = [0,0,0]
# red = [255,0,0]
# blue = [0,0,255]

# screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
# screen = pygame.display.set_mode((screen_width, screen_height-60))
# pygame.display.set_caption("ASTEROIDS++")

# # def userinput():
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT: exit()
# #         print(pygame.key.get_pressed())
# #         if event.type == pygame.key.get_pressed():     
            
# #             match event.key:
# #                 case pygame.K_w: return "w"
# #                 case pygame.K_s: return "s"
# #                 case pygame.K_a: return "a"
# #                 case pygame.K_d: return "d"
# #                 case 13: return 13
# #                 case 769 | 27: exit()
# #     return

# x = screen_width/2
# y = screen_height/2
# a = screen_width/2 
# b = screen_height/2 + 10

# coordinates = [x, y]
# point = [a, b]
# vector = [coordinates, point]
# vectors = a,b,x,y

# difference_x = coordinates[0] - point[0]
# difference_y = coordinates[1] - point[1] 



# def draw_regular_polygon(surface, color, vertex_count, radius, position, width=0):
#     n, r = vertex_count, radius
#     x, y = position
#     pygame.draw.polygon(surface, color, [(x + radius * cos(2 * pi * i / vertex_count), y + radius * sin(2 * pi * i / vertex_count)) for i in range(n)], width)


# while True:
#     screen.fill(black)

#     # pygame.draw.polygon(screen, red, [[100, 100][200, 200][300, 300]])
#     # pygame.draw.polygon(screen, red, [(50,5)(100,100)], 5)
    
 
#     # pygame.draw.polygon(screen,(255, 0, 0), [(100, 50), (50, 150), (150, 150)], True)
#     # draw_regular_polygon(screen, red,8, 50, (200,200), 2)
#     pygame.draw.circle(screen, red, [coordinates[0],coordinates[1]], 20)
#     pygame.draw.line(screen,blue,[400,350], [400, 320], 2)


#     key_pressed_is = pygame.key.get_pressed() 
  
#     # Changing the coordinates 
#     # of the player 
#     # if key_pressed_is[K_a]: 
#     #     coordinates[0] -= 8
#     # if key_pressed_is[K_d]: 
#     #     coordinates[0] += 8
#     # if key_pressed_is[K_w]: 
#     #     coordinates[1] -= 8
#     # if key_pressed_is[K_s]: 
#     #     coordinates[1] += 8
        
        
#     if key_pressed_is[K_LEFT]: 
#         x -= 8
#     if key_pressed_is[K_RIGHT]: 
#         x += 8
#     if key_pressed_is[K_UP]: 
#         y -= 8
#     if key_pressed_is[K_DOWN]: 
#         y += 8

#     pygame.time.Clock().tick(30)

#     pygame.display.flip()

import math 

center_x = 100
center_y = 100
speed = 0


for i in range(0,370,10):
    center_x = speed * math.sin(math.radians(i))
    center_y = speed * math.cos(math.radians(i))
    print(center_x,center_y)
    
    print(i)