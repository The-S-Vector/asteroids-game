import pygame
import time
import sys
import random
import math
import numpy
from numpy import *
# from math import cos, sin, pi

pygame.init()
pygame.mixer.init()

#sound credits: William Benckert - Glitching Through the Sky 

# Define variables 

#https://lospec.com/palette-list

#THEMES
dark_theme = {
    "s_colour" : (255, 255, 255),
    "accent_colour_0" : (0, 0, 255), 
    "accent_colour_1" : (0, 255, 0), 
    "accent_colour_2" : (255, 0, 0), 
    "m_colour" : (0, 0, 0),
    "current" : 0
    }
light_theme = {
    "s_colour" : (0, 0, 0), 
    "accent_colour_0" : (0, 0, 255), 
    "accent_colour_1" : (0, 255, 0), 
    "accent_colour_2" : (255, 0, 0), 
    "m_colour" : (255, 255, 255),
    "current" : 1
    }
Twilight_5_Palette = {
    "s_colour" : ("#fbbbad"), 
    "accent_colour_0" : ("#ee8695"), 
    "accent_colour_1" : ("#4a7a96"), 
    "accent_colour_2" : ("#333f58"), 
    "m_colour" : ("#292831"),
    "current" : 2
    }
    #fbbbad
    #ee8695
    #4a7a96
    #333f58
    #292831
    #https://lospec.com/palette-list/twilight-5
Ink_Palette = {
    "s_colour" : ("#eaf0d8"), 
    "accent_colour_0" : ("#96a2b3"), 
    "accent_colour_1" : ("#596070"), 
    "accent_colour_2" : ("#413a42"), 
    "m_colour" : ("#1f1f29"),
    "current" : 3
    }
    #1f1f29
    #413a42
    #596070
    #96a2b3
    #eaf0d8
leopold_s_dreams_Palette = {
    "s_colour" : ("#474476"), 
    "accent_colour_0" : ("#4888b7"), 
    "accent_colour_1" : ("#6dbcb9"), 
    "accent_colour_2" : ("#8cefb6"), 
    "m_colour" : ("#372134"),
    "current" : 4
    }
    #372134
    #474476
    #4888b7
    #6dbcb9
    #8cefb6
Sunset_Red_Palette = {
    "s_colour" : ("#ee243d"), 
    "accent_colour_0" : ("#af2747"), 
    "accent_colour_1" : ("#6b2341"), 
    "accent_colour_2" : ("#281a2d"), 
    "m_colour" : ("#0d101b"),
    "current" : 5
    }
    #0d101b
    #281a2d
    #6b2341
    #af2747
    #ee243d
five_sheep = {
    "s_colour" : ("#ffdae8"), 
    "accent_colour_0" : ("#b41360"), 
    "accent_colour_1" : ("#ff327c"), 
    "accent_colour_2" : ("#ff80ae"), 
    "m_colour" : ("#480a30"),
    "current" : 6
    }
    #480a30
    #b41360
    #ff327c
    #ff80ae
    #ffdae8 
slimy_05_Palette = {
    "s_colour" : ("#40985e"), 
    "accent_colour_0" : ("#d1cb95"), 
    "accent_colour_1" : ("#1a644e"), 
    "accent_colour_2" : ("#04373b"), 
    "m_colour" : ("#0a1a2f"),
    "current" : 7
    }
    #d1cb95
    #40985e
    #1a644e
    #04373b
    #0a1a2f
NEO_5_Palette = {
    "s_colour" : ("#5433be"), 
    "accent_colour_0" : ("#e624af"), 
    "accent_colour_1" : ("#3df9ea"), 
    "accent_colour_2" : ("#effafa"), 
    "m_colour" : ("#000000"),
    "current" : 8
    }
    #0e0e0e
    #5433be
    #e624af
    #3df9ea 
    #effafa

themes = [dark_theme,light_theme,Twilight_5_Palette,Ink_Palette,leopold_s_dreams_Palette,Sunset_Red_Palette,five_sheep,slimy_05_Palette,NEO_5_Palette]

settings = open("settings.txt", "r")
global current_theme   # terrifing i know
current_theme = eval(settings.readline())

vector = pygame.math.Vector2
clock = pygame.time.Clock()

#asteroid objects
class Asteroids():
    
    def __init__(self):
        self.size = 10
        self.vector = 10
        self.speed = 10
         
        #pygame.draw.polygon()

    
    def collisions():
        pass
    
    def transpoded():
        pass
    
    def gone():
        pass     
#space ship rocket objects 
class Ship():

    def __init__(self, colours, shapes):

        self.colour =  colours            
        self.shape = shapes

    def movement(self):
        self.xvel = 0
        self.yvel = 0 
    
    def shoot(self):
        self.fired = False
        self.reload = 0.3
    
    def death(self):
        self.death = False
#transponder objects
class transponder():
    
    def __init__(self):
        pass

    def fired():
        pass
    
    def hit():
        pass
    
    def miss():
        pass
#buttons
class button():
    
    def __init__(self, x = int, y = int, text = str, function = str,back =str , clicked = False, width = 350, height = 90, textsize = 75):
        
        self.coordinates = [x, y]
        self.size = [width, height]
        self.fillcolour = current_theme["accent_colour_" + str(random.randint(0,2))]  
        self.content = text
        self.function = function
        self.back = back
        self.textcolour = current_theme["s_colour"]
        self.click = clicked
        self.textsize = textsize
        
    def clicking(self, clicked):
        
        self.click = clicked
        
        if self.click == True:
                self.textcolour = current_theme["m_colour"]
                self.fillcolour = current_theme["s_colour"]
        else:
            self.textcolour = current_theme["s_colour"]
            self.fillcolour = current_theme["m_colour"]
           
def Matrix_multy_r(a, angle):
    
    b = [[cos(angle), -sin(angle)],
         [sin(angle), cos(angle)]]
    # b = [[cos(angle), sin(angle), 0],
    #      [-sin(angle), cos(angle), 0],
    #      [point[0], point[1], 1]]
    
    
    # c = [[1,0,0],
    #      [0,1,0],
    #      [-point[0], -point[1], 1]] 
 
    reasult = numpy.dot(a,b)  
    # print(str(reasult) + "--------------")
    # print()
    return reasult
    # reasult2 = numpy.dot(reasult,c)
    # print(str(reasult2) + "reasult2")
    # return reasult2

def Matrix_multy_t(a,t):
    pass
            
#button_frame to make life easy            
def button_frame(lattitude, number, content, function, back, clicked): 
    return button(screen_width/10*lattitude, screen_height/13*number, content, function, back, clicked)
        
def Menu():
    play_button = button_frame(5, 4, "PLAY", "play()", "exit()", False)
    character_button = button_frame(5, 6, "SHIP", "character()","exit()", False)
    option_button = button_frame(5, 8, "SETTINGS", "settings()","exit()", False)
    exit_button = button_frame(5, 10, "EXIT", "exit()","exit()", False)
    list_buttons = [play_button, character_button, option_button, exit_button]

    Menuplay = True        
    location = 0
    
    while Menuplay == True:
        clock.tick(60)
        screen.fill(current_theme["m_colour"])
        background()
        move = 0
        user_input = userinput()
        
        if user_input == "w": move = -1
        elif user_input == "s": move = 1 
        elif user_input == 13:
            for item in list_buttons:
                if item.click == True: 
                    eval(item.function)
                    
        elif user_input == "esc":
            for item in list_buttons:
                if item.click == True: 
                    eval(item.back)
        else: move = 0
            
            
        try: 
            location = location + int(move)
            location = location % len(list_buttons)
        except: 
            pass
        
        
        for buttons in list_buttons:
            if buttons == list_buttons[location]: 
                list_buttons[location].clicking(True)
            
            else:
                buttons.clicking(False)
            
            
            pygame.draw.rect(screen, buttons.fillcolour, pygame.Rect(buttons.coordinates[0] - buttons.size[0]/2, buttons.coordinates[1] - buttons.size[1]/2, buttons.size[0], buttons.size[1]),0, 2, 3)
            subtitle = pygame.font.SysFont("Helvetic", buttons.textsize).render(buttons.content, True, buttons.textcolour)
            screen.blit(subtitle,(buttons.coordinates[0] - 150, buttons.coordinates[1]- 20))
        
        title = pygame.font.SysFont("Helvetic", 200).render(" ASTEROIDS++", True, current_theme["s_colour"])
        screen.blit(title, (screen_width/2-title.get_width()/2, screen_height/13*2-title.get_height()/2)) 
            
        pygame.display.flip()

def play():
    global current_theme
    
    speed = 5
    acceleration = 2
    angle = 0.1
    movement = 0
    
    characters = open("character.txt", "r")
    current_character = eval(characters.readline())

    match current_character["current"]: 
        case 0:shapes = current_character["triangle"]
        case 1:shapes = current_character["arrow"]            
    
    
    user = Ship(current_theme["s_colour"], shapes)
    
    alive = True
    while alive == True:
        clock.tick(60)
        screen.fill(current_theme["m_colour"])
        background()
        user_input = userinput()
        if user_input == "esc": Menu()
             
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit()

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            angle -= 0.1
            # angle_y += ROTATE_SPEED
        if keys[pygame.K_d]:
            angle += 0.1
            # angle_y -= ROTATE_SPEED      
        if keys[pygame.K_w]:
            movement += 5
            # angle_x += ROTATE_SPEED
        if keys[pygame.K_s]:
            movement -=5
            
        location = []
        print(user.shape)
        for point in user.shape:
            point[1] += movement
            
            location.append(Matrix_multy_r(point, angle))  
            
            
        movement = 0 
        SCALE = 1
        
        print(location)
        
        for verteces in location:
            verteces[0] = screen_width/2 - verteces[0]/SCALE
            verteces[1] = screen_height/2 - verteces[1]/SCALE  
        
        pygame.draw.polygon(screen,current_theme["s_colour"],tuple(location), 5)
        
        if speed >= 64:
            acceleration = 0 
        else:
            speed += acceleration^2
            acceleration += acceleration^2
        
        
        pygame.display.flip()
             
def volumes():

    if pygame.mixer.music.get_busy() == True: 
        pygame.mixer.music.pause() # stop playback of all sound channels pygame.mixer.fadeout pygame.mixer.stop

    elif pygame.mixer.music.get_busy() == False: 
        pygame.mixer.music.unpause() 

def themes():
    
    global current_theme   # terrible i know
    themes = [dark_theme,light_theme,Twilight_5_Palette,Ink_Palette,leopold_s_dreams_Palette,Sunset_Red_Palette,five_sheep,slimy_05_Palette,NEO_5_Palette]
    
    settings = open("settings.txt", "r")
    current_theme = eval(settings.readline())
    
    settings = open("settings.txt", "w")
    settings.write(str(themes[(current_theme["current"] + 1) % 9]))
                  
    settings = open("settings.txt", "r")       
    current_theme = eval(settings.readline())       

def settings():
    volume_button = button_frame(5, 4, "VOLUME", "volumes()", "Menu()", False)
    theme = button_frame(5, 6, "THEME", "themes()", "Menu()", False)

    list_buttons = [volume_button, theme]

          
    location = 0
    setting = True
    while setting == True:
        screen.fill(current_theme["m_colour"])
        background()
        
        move = 0
        user_input = userinput()
        
        if user_input == "w": move = -1
        elif user_input == "s": move = 1 
        elif user_input == 13:
            for item in list_buttons:
                if item.click == True: 
                    eval(item.function)
        elif user_input == "esc":
            for item in list_buttons:
                if item.click == True: 
                    eval(item.back)
        else: move = 0
             
        location = location + int(move)
        location = location % len(list_buttons)

        
        for buttons in list_buttons:
            if buttons == list_buttons[location]: 
                list_buttons[location].clicking(True)
            
            else:
                buttons.clicking(False)
            
            pygame.draw.rect(screen, buttons.fillcolour, (buttons.coordinates[0] - buttons.size[0]/2, buttons.coordinates[1] - buttons.size[1]/2, buttons.size[0], buttons.size[1]),0, 2, 3)
            subtitle = pygame.font.SysFont("Helvetic", buttons.textsize).render(buttons.content, True, buttons.textcolour)
            screen.blit(subtitle,(buttons.coordinates[0] - 150, buttons.coordinates[1]- 20))
        
        title = pygame.font.SysFont("Helvetic", 200).render(" SETTINGS  ", True, current_theme["s_colour"])
        screen.blit(title, (screen_width/2-title.get_width()/2, screen_height/13*2-title.get_height()/2)) 
            
        pygame.display.flip()

def change():
    characters = open("character.txt", "r")
    current_character = eval(characters.readline())

    match current_character["current"]: 
        case 0:
            characters = open("character.txt", "w")
            characters.write(str({"triangle": ([-20,40],[0,15],[20,40]), "arrow": ([-20,40],[0,-15],[20,40],[0,15]), "current": 1}))
      
        case 1:
            characters = open("character.txt", "w")
            characters.write(str({"triangle": ([-20,40],[0,15],[20,40]), "arrow": ([-20,40],[0,-15],[20,40],[0,15]), "current": 0}))
                  
    characters = open("character.txt", "r")       
    current_character = eval(characters.readline()) 
       
def character():
    changes = button_frame(5, 4, "CHANGE", "change()", "Menu()", False)

    list_buttons = [changes]
          
    location = 0
    characterising = True
    while characterising == True:
       
        screen.fill(current_theme["m_colour"])
        background()
        
        move = 0
        user_input = userinput()
        
        if user_input == "w": move = -1
        elif user_input == "s": move = 1 
        elif user_input == 13:
            for item in list_buttons:
                if item.click == True: 
                    eval(item.function)
        elif user_input == "esc":
            for item in list_buttons:
                if item.click == True: 
                    eval(item.back)
        else: move = 0
             

        location = location + int(move)
        location = location % len(list_buttons)

        
        for buttons in list_buttons:
            if buttons == list_buttons[location]: 
                list_buttons[location].clicking(True)
            
            else:
                buttons.clicking(False)
            
            pygame.draw.rect(screen, buttons.fillcolour, (buttons.coordinates[0] - buttons.size[0]/2, buttons.coordinates[1] - buttons.size[1]/2, buttons.size[0], buttons.size[1]),0, 2, 3)
            subtitle = pygame.font.SysFont("Helvetic", buttons.textsize).render(buttons.content, True, buttons.textcolour)
            screen.blit(subtitle,(buttons.coordinates[0] - 150, buttons.coordinates[1]- 20))
        
        pygame.draw.rect(screen, current_theme["s_colour"], (screen_width/10*5 - 175, screen_height/13*7 - 150, 350, 300),5, 2, 3)
        
        characters = open("character.txt", "r")
        current_character = eval(characters.readline())

        match current_character["current"]: 
            case 0:
                verteces = current_character["triangle"]
                
                for vertex in  verteces:
                    vertex[0] = int(screen_width/2 - vertex[0]*5)
                    vertex[1] = int(screen_height/13*7 + vertex[1]*5 - 100)
                
                
            case 1:
                verteces = current_character["arrow"]
                               
                for vertex in verteces:
                    vertex[0] = int(screen_width/2 - vertex[0]*5)
                    vertex[1] = int(screen_height/13*7 + vertex[1]*5 - 60)
                    
        

        pygame.draw.polygon(screen,current_theme["s_colour"], verteces, 5)
                #pygame.draw.polygon(screen,current_theme["s_colour"], [(screen_width/10*5 - 50, screen_height/13*9 + 20),(screen_width/10*5, screen_height/13*9 - 100),(screen_width/10*5 + 50, screen_height/13*9 + 20)], 2)

                
                
                
        title = pygame.font.SysFont("Helvetic", 200).render("SHIP HANGAR", True, current_theme["s_colour"])
        screen.blit(title, (screen_width/2-title.get_width()/2, screen_height/13*2-title.get_height()/2)) 
            
        pygame.display.flip()
    
def exit():
    pygame.quit()
    # sys.exit()

def userinput():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
        if event.type == pygame.KEYUP:      
            match event.key:
                case pygame.K_w: return "w"
                case pygame.K_s: return "s"
                case pygame.K_a: return "a"
                case pygame.K_d: return "d"
                case 13: return 13
                case 769 | 27: return "esc"   #escape key
    return 

def background():
    global current_theme
    #create the locations of the stars for when we animate the background

    for star in star_field_slow:
        star[1] += 1
        if star[1] > screen_height:
            star[0] = numpy.random.randint(0, screen_width)
            star[1] = numpy.random.randint(-20, -5)
        pygame.draw.circle(screen, current_theme["accent_colour_0"], star, 3)

    for star in star_field_medium:
        star[1] += 2
        if star[1] > screen_height:
            star[0] = numpy.random.randint(0, screen_width)
            star[1] = numpy.random.randint(-20, -5)
        pygame.draw.circle(screen, current_theme["accent_colour_1"], star, 2)

    for star in star_field_fast:
        star[1] += 3
        if star[1] > screen_height:
            star[0] = numpy.random.randint(0, screen_width)
            star[1] = numpy.random.randint(-20, -5)
        pygame.draw.circle(screen, current_theme["accent_colour_2"], star, 1)
    
    pygame.time.Clock().tick(60)

def draw_regular_polygon(surface, color, vertex_count, radius, position, width=0):
    n, r = vertex_count, radius
    x, y = position
    pygame.draw.polygon(surface, color, [(x + r * cos(2 * pi * i / n), y + r * sin(2 * pi * i / n)) for i in range(n)], width)


# Set up the display window

screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((screen_width, screen_height-60))
pygame.display.set_caption("ASTEROIDS++")
pygame.mixer.music.load("8bitsoundtrack.mp3")
pygame.mixer.music.play(-1)


#https://gist.github.com/ogilviemt/9b05a89d023054e6279f
star_field_slow = []
star_field_medium = []
star_field_fast = []

for slow_stars in range(200): 
    star_loc_x = numpy.random.randint(0, screen_width)
    star_loc_y = numpy.random.randint(0, screen_height)
    star_field_slow.append([star_loc_x, star_loc_y]) 

for medium_stars in range(140):
    star_loc_x = numpy.random.randint(0, screen_width)
    star_loc_y = numpy.random.randint(0, screen_height)
    star_field_medium.append([star_loc_x, star_loc_y])

for fast_stars in range(60):
    star_loc_x = numpy.random.randint(0, screen_width)
    star_loc_y = numpy.random.randint(0, screen_height)
    star_field_fast.append([star_loc_x, star_loc_y])


Menu()
    
    
    
    
    

    
    
    



