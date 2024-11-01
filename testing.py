
# importing pygame module
import pygame
 
# importing sys module
import sys
 
# initialising pygame
pygame.init()
 
# creating display
display = pygame.display.set_mode((300, 300))
 
# # creating a running loop
# while True:
       
#     # creating a loop to check events that 
#     # are occurring
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
         
#         # checking if keydown event happened or not
#         if event.type == pygame.KEYDOWN:
               
#             # checking if key "A" was pressed
#             if event.key == pygame.K_a:
#                 print("Key A has been pressed")
               
#             # checking if key "J" was pressed
#             if event.key == pygame.K_j:
#                 print("Key J has been pressed")
               
#             # checking if key "P" was pressed
#             if event.key == pygame.K_p:
#                 print("Key P has been pressed")
             
#             # checking if key "M" was pressed
#             if event.key == pygame.K_m:
#                 print("Key M has been pressed")


# x = [-5,-4,-3,-2,-1,0,1,2,3,4, 5]

# for i in x:
#     print(f" {i}: {i % 4}")
    
# for i in range(0, len(x)):
#     print(f" {i}: {x[i] % 4}")
    
    
    
# x = "aaaaabbbbccc"

# # print(x.count("b"))

# while True:
#     pygame.draw.polygon(display,[00,255,255],[[20,30],[30,30],[10,20]],30)
#     display.fill([0,0,0])
#     #pygame.draw.circle(display,[00,00,255], [100,30], 100)
#     pygame.display.flip()


# import pygame
# import random

# screen = pygame.display.set_mode([1024, 768])
# height = pygame.display.Info().current_h
# width = pygame.display.Info().current_w
# pygame.display.set_caption('Window Caption')
# clock = pygame.time.Clock()
# # clock.tick(30)

# #create the locations of the stars for when we animate the background
# star_field_slow = []
# star_field_medium = []
# star_field_fast = []

# for slow_stars in range(50): #birth those plasma balls, baby
#     star_loc_x = random.randrange(0, width)
#     star_loc_y = random.randrange(0, height)
#     star_field_slow.append([star_loc_x, star_loc_y]) #i love your balls

# for medium_stars in range(35):
#     star_loc_x = random.randrange(0, width)
#     star_loc_y = random.randrange(0, height)
#     star_field_medium.append([star_loc_x, star_loc_y])

# for fast_stars in range(15):
#     star_loc_x = random.randrange(0, width)
#     star_loc_y = random.randrange(0, height)
#     star_field_fast.append([star_loc_x, star_loc_y])

# #define some commonly used colours
# WHITE = (255, 255, 255)
# LIGHTGREY = (192, 192, 192)
# DARKGREY = (128, 128, 128)
# BLACK = (0, 0, 0)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)
# MAGENTA = (255, 0, 255)
# CYAN = (0, 255, 255)
                                 
# #create the window
# pygame.init()

# app_is_alive = True

# while app_is_alive:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             print("Exiting... All hail the void!")
#             app_is_alive = False #murderer!
#         if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
#             print("Exiting... All hail the void!")
#             app_is_alive = False #murderer!

#     #my soul knows only darkness
#     screen.fill(BLACK)

#     #animate some motherfucking stars
#     for star in star_field_slow:
#         star[1] += 1
#         if star[1] > height:
#             star[0] = random.randrange(0, width)
#             star[1] = random.randrange(-20, -5)
#         pygame.draw.circle(screen, DARKGREY, star, 3)

#     for star in star_field_medium:
#         star[1] += 4
#         if star[1] > height:
#             star[0] = random.randrange(0, width)
#             star[1] = random.randrange(-20, -5)
#         pygame.draw.circle(screen, LIGHTGREY, star, 2)

#     for star in star_field_fast:
#         star[1] += 8
#         if star[1] > height:
#             star[0] = random.randrange(0, width)
#             star[1] = random.randrange(-20, -5)
#         pygame.draw.circle(screen, YELLOW, star, 1)

#     #redraw everything we've asked pygame to draw
#     pygame.display.flip()

#     #set frames per second
    
#     clock.tick(30)

# #quit gracefully
# pygame.quit()

s_colour = (255, 255, 255)
accent_colour = (0, 0, 255)   #green
accent_colour_1 = (0, 255, 0) #blue
accent_colour_2 = (255, 0, 0) #red
m_colour = (0, 0, 0)


#write lines
# settings_c = open("IB_computer_science_coursework/game/settings.txt", "w") 
settings_c = open("IB_computer_science_coursework/game/settings.txt", "w")

theme = {"darktheme": [(255, 255, 255), (0, 0, 255), (0, 255, 0), (255, 0, 0),(0, 0, 0)], 
         "lighttheme": [(0, 0, 0), (0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 255)], 
         "current_dark": True}

settings_c.write(theme)
# settings_c.writelines(theme)
# settings_c.close() 


settings = open("IB_computer_science_coursework/game/settings.txt", "r")
theme = settings.readline()
print(theme)
# if theme.value[2] == True:
#     print("dark theme")
    
