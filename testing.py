
# # # importing pygame module
# # # import pygame
 
# # # # importing sys module
# # # import sys
 
# # # # initialising pygame
# # # pygame.init()
 
# # # # creating display
# # # display = pygame.display.set_mode((300, 300))
 
# # # # creating a running loop
# # # while True:
       
# # #     # creating a loop to check events that 
# # #     # are occurring
# # #     for event in pygame.event.get():
# # #         if event.type == pygame.QUIT:
# # #             pygame.quit()
# # #             sys.exit()
         
# # #         # checking if keydown event happened or not
# # #         if event.type == pygame.KEYDOWN:
               
# # #             # checking if key "A" was pressed
# # #             if event.key == pygame.K_a:
# # #                 print("Key A has been pressed")
               
# # #             # checking if key "J" was pressed
# # #             if event.key == pygame.K_j:
# # #                 print("Key J has been pressed")
               
# # #             # checking if key "P" was pressed
# # #             if event.key == pygame.K_p:
# # #                 print("Key P has been pressed")
             
# # #             # checking if key "M" was pressed
# # #             if event.key == pygame.K_m:
# # #                 print("Key M has been pressed")


# # # x = [-5,-4,-3,-2,-1,0,1,2,3,4, 5]

# # # for i in x:
# # #     print(f" {i}: {i % 4}")
    
# # # for i in range(0, len(x)):
# # #     print(f" {i}: {x[i] % 4}")
    
    
    
# # # x = "aaaaabbbbccc"

# # # # print(x.count("b"))

# # # while True:
# # #     pygame.draw.polygon(display,[00,255,255],[[20,30],[30,30],[10,20]],30)
# # #     display.fill([0,0,0])
# # #     #pygame.draw.circle(display,[00,00,255], [100,30], 100)
# # #     pygame.display.flip()


# # # import pygame
# # # import random

# # # screen = pygame.display.set_mode([1024, 768])
# # # height = pygame.display.Info().current_h
# # # width = pygame.display.Info().current_w
# # # pygame.display.set_caption('Window Caption')
# # # clock = pygame.time.Clock()
# # # # clock.tick(30)

# # # #create the locations of the stars for when we animate the background
# # # star_field_slow = []
# # # star_field_medium = []
# # # star_field_fast = []

# # # for slow_stars in range(50): #birth those plasma balls, baby
# # #     star_loc_x = random.randrange(0, width)
# # #     star_loc_y = random.randrange(0, height)
# # #     star_field_slow.append([star_loc_x, star_loc_y]) #i love your balls

# # # for medium_stars in range(35):
# # #     star_loc_x = random.randrange(0, width)
# # #     star_loc_y = random.randrange(0, height)
# # #     star_field_medium.append([star_loc_x, star_loc_y])

# # # for fast_stars in range(15):
# # #     star_loc_x = random.randrange(0, width)
# # #     star_loc_y = random.randrange(0, height)
# # #     star_field_fast.append([star_loc_x, star_loc_y])

# # # #define some commonly used colours
# # # WHITE = (255, 255, 255)
# # # LIGHTGREY = (192, 192, 192)
# # # DARKGREY = (128, 128, 128)
# # # BLACK = (0, 0, 0)
# # # RED = (255, 0, 0)
# # # GREEN = (0, 255, 0)
# # # BLUE = (0, 0, 255)
# # # YELLOW = (255, 255, 0)
# # # MAGENTA = (255, 0, 255)
# # # CYAN = (0, 255, 255)
                                 
# # # #create the window
# # # pygame.init()

# # # app_is_alive = True

# # # while app_is_alive:
# # #     for event in pygame.event.get():
# # #         if event.type == pygame.QUIT:
# # #             print("Exiting... All hail the void!")
# # #             app_is_alive = False #murderer!
# # #         if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
# # #             print("Exiting... All hail the void!")
# # #             app_is_alive = False #murderer!

# # #     #my soul knows only darkness
# # #     screen.fill(BLACK)

# # #     #animate some motherfucking stars
# # #     for star in star_field_slow:
# # #         star[1] += 1
# # #         if star[1] > height:
# # #             star[0] = random.randrange(0, width)
# # #             star[1] = random.randrange(-20, -5)
# # #         pygame.draw.circle(screen, DARKGREY, star, 3)

# # #     for star in star_field_medium:
# # #         star[1] += 4
# # #         if star[1] > height:
# # #             star[0] = random.randrange(0, width)
# # #             star[1] = random.randrange(-20, -5)
# # #         pygame.draw.circle(screen, LIGHTGREY, star, 2)

# # #     for star in star_field_fast:
# # #         star[1] += 8
# # #         if star[1] > height:
# # #             star[0] = random.randrange(0, width)
# # #             star[1] = random.randrange(-20, -5)
# # #         pygame.draw.circle(screen, YELLOW, star, 1)

# # #     #redraw everything we've asked pygame to draw
# # #     pygame.display.flip()

# # #     #set frames per second
    
# # #     clock.tick(30)

# # # #quit gracefully
# # # pygame.quit()

# # # s_colour = (255, 255, 255)
# # # accent_colour = (0, 0, 255)   #green
# # # accent_colour_1 = (0, 255, 0) #blue
# # # accent_colour_2 = (255, 0, 0) #red
# # # m_colour = (0, 0, 0)


# # # #write lines
# # # # settings_c = open("IB_computer_science_coursework/game/settings.txt", "w") 
# # # settings_c = open("IB_computer_science_coursework/game/settings.txt", "w")

# # # theme = {"darktheme": [(255, 255, 255), (0, 0, 255), (0, 255, 0), (255, 0, 0),(0, 0, 0)], 
# # #          "lighttheme": [(0, 0, 0), (0, 0, 255), (0, 255, 0), (255, 0, 0), (255, 255, 255)], 
# # #          "current_dark": True}

# # # settings_c.write(theme)
# # # # settings_c.writelines(theme)
# # # # settings_c.close() 


# # # settings = open("IB_computer_science_coursework/game/settings.txt", "r")
# # # theme = settings.readline()
# # # print(theme)
# # # # if theme.value[2] == True:
# # # #     print("dark theme")
# # # dark_theme = {
# # #     "s_colour" : (255, 255, 255),
# # #     "accent_colour" : (0, 0, 255), 
# # #     "accent_colour_1" : (0, 255, 0), 
# # #     "accent_colour_2" : (255, 0, 0), 
# # #     "m_colour" : (0, 0, 0)
# # #     }


# # # light_theme = {
# # #     "s_colour" : (0, 0, 0), 
# # #     "accent_colour" : (0, 0, 255), 
# # #     "accent_colour_1" : (0, 255, 0), 
# # #     "accent_colour_2" : (255, 0, 0), 
# # #     "m_colour" : (255, 255, 255)
# # #     }

   
    
# # # settings = open("settings.txt", "r")
# # # current_theme = eval(settings.readline())

# # # print(dark_theme)
# # # print(light_theme)

# # # print(current_theme)

# # # settings.close()

# # # match current_theme["m_colour"]: 
# # #     case (0,0,0):
# # #         settings = open("settings.txt", "w")
# # #         settings.writelines(str(light_theme))
# # #         print("it was dark now it is light")
# # #         settings.close()
        
# # #     case (255,255,255):
# # #         settings = open("settings.txt", "w")
# # #         settings.write(str(dark_theme))
# # #         print("light has won")
# # #         settings.close()
        
# # # settings = open("settings.txt", "r")       
# # # current_theme = eval(settings.readline())

# # # print("changed theme")
# # # print(current_theme)
# # # settings.close()
    
# # a = [1,2,3,4,5]
# # print(a[1])
# #     #{"s_colour" : (255, 255, 255), "accent_colour" : (0, 0, 255), "accent_colour_1" : (0, 255, 0), "accent_colour_2" : (255, 0, 0), "m_colour" : (0, 0, 0)}
# import pygame
# from math import *
# import numpy

# pygame.init()
# WINDOW_SIZE =  800
# ROTATE_SPEED = 0.1
# window = pygame.display.set_mode( (WINDOW_SIZE, WINDOW_SIZE) )
# clock = pygame.time.Clock()

# projection_matrix = [[1,0,0],
#                      [0,1,0],
#                      [0,0,0]]

# cube_points = [n for n in range(8)]
# cube_points[0] = [[-1], [-1], [1]]
# cube_points[1] = [[1],[-1],[1]]
# cube_points[2] = [[1],[1],[1]]
# cube_points[3] = [[-1],[1],[1]]
# cube_points[4] = [[-1],[-1],[-1]]
# cube_points[5] = [[1],[-1],[-1]]
# cube_points[6] = [[1],[1],[-1]]
# cube_points[7] = [[-1],[1],[-1]]


# def multiply_m(a, b): return numpy.dot(a,b)
#     # a_rows = len(a)
#     # a_cols = len(a[0])

#     # b_rows = len(b)
#     # b_cols = len(b[0])
#     # # Dot product matrix dimentions = a_rows x b_cols
#     # product = [[0 for _ in range(b_cols)] for _ in range(a_rows)]

#     # if a_cols == b_rows:
            
#         # for i in range(a_rows):
#         #     for j in range(b_cols):
#         #         for k in range(b_rows):
#         #             product[i][j] += a[i][k] * b[k][j]
    
#     # else:
#     #     print("INCOMPATIBLE MATRIX SIZES")
        
#     # return product        


# def connect_points(i, j, points):
#     pygame.draw.line(window, (255, 255, 255), (points[i][0], points[i][1]) , (points[j][0], points[j][1]))

# # Main Loop
# scale = 100
# angle_x = angle_y = angle_z = 0
# while True:
#     clock.tick(60)
#     window.fill((0,0,0))
#     rotation_x = [[1, 0, 0],
#                     [0, cos(angle_x), -sin(angle_x)],
#                     [0, sin(angle_x), cos(angle_x)]]

#     rotation_y = [[cos(angle_y), 0, sin(angle_y)],
#                     [0, 1, 0],
#                     [-sin(angle_y), 0, cos(angle_y)]]

#     rotation_z = [[cos(angle_z), -sin(angle_z), 0],
#                     [sin(angle_z), cos(angle_z), 0],
#                     [0, 0, 1]]

#     points = [0 for _ in range(len(cube_points))]
#     i = 0
#     for point in cube_points:
#         rotate_x = multiply_m(rotation_x, point)
#         rotate_y = multiply_m(rotation_y, rotate_x)
#         rotate_z = multiply_m(rotation_z, rotate_y)
#         point_2d = multiply_m(projection_matrix, rotate_z)
    
#         x = (point_2d[0][0] * scale) + WINDOW_SIZE/2
#         y = (point_2d[1][0] * scale) + WINDOW_SIZE/2

#         points[i] = (x,y)
#         i += 1
#         pygame.draw.circle(window, (255, 0, 0), (x, y), 5)

#     l1 = [0,0,0,1,1,2,2,3,4,4,6,6]
#     l2 = [1,3,4,2,5,6,3,7,5,7,5,7]
    
#     for dots in range(0,12):
#         connect_points(l1[dots],l2[dots], points)
        
#     # connect_points(0, 1, points)
#     # connect_points(0, 3, points)
#     # connect_points(0, 4, points)
#     # connect_points(1, 2, points)
#     # connect_points(1, 5, points)
#     # connect_points(2, 6, points)
#     # connect_points(2, 3, points)
#     # connect_points(3, 7, points)
#     # connect_points(4, 5, points)
#     # connect_points(4, 7, points)
#     # connect_points(6, 5, points)
#     # connect_points(6, 7, points)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
        
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_r]:
#             angle_y = angle_x = angle_z = 0
#         if keys[pygame.K_a]:
#             angle_y += ROTATE_SPEED
#         if keys[pygame.K_d]:
#             angle_y -= ROTATE_SPEED      
#         if keys[pygame.K_w]:
#             angle_x += ROTATE_SPEED
#         if keys[pygame.K_s]:
#             angle_x -= ROTATE_SPEED
#         if keys[pygame.K_q]:
#             angle_z -= ROTATE_SPEED
#         if keys[pygame.K_e]:
#             angle_z += ROTATE_SPEED      
          
#     pygame.display.update()