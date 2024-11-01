import pygame
import time
import sys
import random
import math
from math import cos, sin, pi

pygame.init()
pygame.mixer.init()

#sound credits: William Benckert - Glitching Through the Sky
    

# Define variables 

dark_theme = {
    "s_colour" : (255, 255, 255),
    "accent_colour" : (0, 0, 255), 
    "accent_colour_1" : (0, 255, 0), 
    "accent_colour_2" : (255, 0, 0), 
    "m_colour" : (0, 0, 0)
    }


light_theme = {
    "s_colour" : (0, 0, 0), 
    "accent_colour" : (0, 0, 255), 
    "accent_colour_1" : (0, 255, 0), 
    "accent_colour_2" : (255, 0, 0), 
    "m_colour" : (255, 255, 255)
    }


settings = open("settings.txt", "r")

global current_theme   # terrifing i know

current_theme = eval(settings.readline())




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

    def __init__(self):
        pass

    def spawn():
        pass

    def movement():
        for event in pygame.event.get():
            if event.type == pygame.key("w"):
                pass
            
    
    def shot():
        pass
    
    def secondlife():
        pass
    
    def death():
        pass

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
        self.fillcolour = current_theme["m_colour"]
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
            
#button_frame to make life easy            
def button_frame(lattitude, number, content, function, back, clicked): return button(screen_width/10*lattitude, screen_height/13*number, content, function, back, clicked)
        
#MENU
def Menu():
    play_button = button_frame(5, 4, "PLAY", "play()", "exit()", False)
    character_button = button_frame(5, 6, "SHIP", "character()","exit()", False)
    option_button = button_frame(5, 8, "SETTINGS", "settings()","exit()", False)
    exit_button = button_frame(5, 10, "EXIT", "exit()","exit()", False)
    list_buttons = [play_button, character_button, option_button, exit_button]

    Menuplay = True        
    location = 0
    
    while Menuplay == True:
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

#play
def play():
    
    alive = True
    while alive == True:
        screen.fill(current_theme["m_colour"])
        background()
        pygame.draw.circle(screen,current_theme["accent_colour_2"], [screen_width/10*5, screen_height/13*6], 100)
        pygame.display.flip()
        userinput()
          
def volumes():
    print("boooooom")
    print(pygame.mixer.music.get_busy())

    if pygame.mixer.music.get_busy() == True: 
        pygame.mixer.music.pause() # stop playback of all sound channels pygame.mixer.fadeout pygame.mixer.stop
        print("unpaused")
    elif pygame.mixer.music.get_busy() == False: 
        pygame.mixer.music.unpause() 
        print("paused")

def themes():
    global current_theme   # terrible i know
    
    settings = open("settings.txt", "r")
    current_theme = eval(settings.readline())

    match current_theme["m_colour"]: 
        case (0,0,0):
            settings = open("settings.txt", "w")
            settings.write(str(light_theme))
      
        case (255,255,255):
            settings = open("settings.txt", "w")
            settings.write(str(dark_theme))
                  
    settings = open("settings.txt", "r")       
    current_theme = eval(settings.readline())       
    
#setting
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
        
        title = pygame.font.SysFont("Helvetic", 200).render(" SETTINGS  ", True, current_theme["s_colour"])
        screen.blit(title, (screen_width/2-title.get_width()/2, screen_height/13*2-title.get_height()/2)) 
            
        pygame.display.flip()

#characterpage 
def set():
    pass

def change():
    pass

def character():
    change = button_frame(5, 4, "CHANGE", "change()", "Menu()", False)
    set = button_frame(5, 6, "SET", "set()", "Menu()", False)

    list_buttons = [change, set]

          
    location = 0
    characterising = True
    while characterising == True:
       
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
    #create the locations of the stars for when we animate the background

    for star in star_field_slow:
        star[1] += 1
        if star[1] > screen_height:
            star[0] = random.randrange(0, screen_width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, current_theme["s_colour"], star, 3)

    for star in star_field_medium:
        star[1] += 2
        if star[1] > screen_height:
            star[0] = random.randrange(0, screen_width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, current_theme["s_colour"], star, 2)

    for star in star_field_fast:
        star[1] += 3
        if star[1] > screen_height:
            star[0] = random.randrange(0, screen_width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, current_theme["s_colour"], star, 1)
    
    pygame.time.Clock().tick(30)

def draw_regular_polygon(surface, color, vertex_count, radius, position, width=0):
    n, r = vertex_count, radius
    x, y = position
    pygame.draw.polygon(surface, color, [
        (x + r * cos(2 * pi * i / n), y + r * sin(2 * pi * i / n))
        for i in range(n)
    ], width)


# Set up the display window

screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((screen_width, screen_height-60))
pygame.display.set_caption("ASTEROIDS++")
pygame.mixer.music.load("8bitsoundtrack.mp3")
pygame.mixer.music.play(2)


#https://gist.github.com/ogilviemt/9b05a89d023054e6279f
star_field_slow = []
star_field_medium = []
star_field_fast = []

for slow_stars in range(50): 
    star_loc_x = random.randrange(0, screen_width)
    star_loc_y = random.randrange(0, screen_height)
    star_field_slow.append([star_loc_x, star_loc_y]) 

for medium_stars in range(35):
    star_loc_x = random.randrange(0, screen_width)
    star_loc_y = random.randrange(0, screen_height)
    star_field_medium.append([star_loc_x, star_loc_y])

for fast_stars in range(15):
    star_loc_x = random.randrange(0, screen_width)
    star_loc_y = random.randrange(0, screen_height)
    star_field_fast.append([star_loc_x, star_loc_y])


Menu()
    
    
    
    
    

    
    
    



