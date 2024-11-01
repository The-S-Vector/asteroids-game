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
s_colour = (255, 255, 255)
accent_colour = (0, 0, 255)   #green
accent_colour_1 = (0, 255, 0) #blue
accent_colour_2 = (255, 0, 0) #red
m_colour = (0, 0, 0)



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
    
    def __init__(self, x = int, y = int, text = str, function = str, clicked = False, width = 350, height = 90, textsize = 75):
        
        self.coordinates = [x, y]
        self.size = [width, height]
        self.fillcolour = m_colour
        self.content = text
        self.function = function
        self.textcolour = s_colour
        self.click = clicked
        self.textsize = textsize
        
    def clicking(self, clicked):
        
        self.click = clicked
        
        if self.click == True:
                self.textcolour = m_colour
                self.fillcolour = s_colour
        else:
            self.textcolour = s_colour
            self.fillcolour = m_colour
            
#button_frame to make life easy            
def button_frame(lattitude, number, content, function, clicked): return button(screen_width/10*lattitude, screen_height/13*number, content, function, clicked)
        
#MENU
def Menu():
    play_button = button_frame(5, 4, "PLAY", "play()", False)
    character_button = button_frame(5, 6, "SHIP", "character()", False)
    option_button = button_frame(5, 8, "SETTINGS", "settings()", False)
    exit_button = button_frame(5, 10, "EXIT", "exit()", False)
    list_buttons = [play_button, character_button, option_button, exit_button]

    Menuplay = True        
    location = 0
    
    while Menuplay == True:
        screen.fill(m_colour)
        background()
        move = 0
        user_input = userinput()
        
        if user_input == "w": move = -1
        elif user_input == "s": move = 1 
        elif user_input == 13:
            for item in list_buttons:
                if item.click == True: 
                    eval(item.function)
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
        
        title = pygame.font.SysFont("Helvetic", 200).render(" ASTEROIDS++", True, s_colour)
        screen.blit(title, (screen_width/2-title.get_width()/2, screen_height/13*2-title.get_height()/2)) 
            
        pygame.display.flip()

#play
def play():
    
    alive = True
    while alive == True:
        screen.fill(m_colour)#
        background()
        pygame.draw.circle(screen,accent_colour_2, [screen_width/10*5, screen_height/13*6], 100)
        pygame.display.flip()
        userinput()
    
def volumes(effect = int):
    if effect == 0: pygame.mixer.stop # stop playback of all sound channels
    elif effect == 2: pygame.mixer.play 
    elif effect == 1: pygame.mixer.music.set_volume(pygame.mixer.music.get_volume + 5) 
    elif effect == -1: pygame.mixer.music.set_volume(pygame.mixer.music.get_volume - 5)
    
def themes():
    if m_colour == [0,0,0]:
        m_colour = s_colour
        s_colour =  [0,0,0]
    pass
    
#setting
def settings():
    volume_button = button_frame(5, 4, "VOLUME", "volumes()", False)
    theme = button_frame(5, 6, "THEME", "themes()", False)

    list_buttons = [volume_button, theme]

          
    location = 0
    setting = True
    while setting == True:
        screen.fill(m_colour)
               
        background()
        
        move = 0
        user_input = userinput()
        
        if user_input == "w": move = -1
        elif user_input == "s": move = 1 
        elif user_input == 13:
            for item in list_buttons:
                if item.click == True: 
                    eval(item.function)
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
        
        title = pygame.font.SysFont("Helvetic", 200).render(" SETTINGS  ", True, s_colour)
        screen.blit(title, (screen_width/2-title.get_width()/2, screen_height/13*2-title.get_height()/2)) 
            
        pygame.display.flip()


#characterpage 
def character():
    characterising = True
    while characterising == True:
        screen.fill(m_colour)
        background()
        pygame.draw.circle(screen,accent_colour_1, [screen_width/10*5, screen_height/13*6], 100)
        pygame.display.flip()
        userinput()

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
                case 769 | 27: exit()
    return 


def background():
    #create the locations of the stars for when we animate the background

    for star in star_field_slow:
        star[1] += 1
        if star[1] > screen_height:
            star[0] = random.randrange(0, screen_width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, s_colour, star, 3)

    for star in star_field_medium:
        star[1] += 2
        if star[1] > screen_height:
            star[0] = random.randrange(0, screen_width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, s_colour, star, 2)

    for star in star_field_fast:
        star[1] += 3
        if star[1] > screen_height:
            star[0] = random.randrange(0, screen_width)
            star[1] = random.randrange(-20, -5)
        pygame.draw.circle(screen, s_colour, star, 1)
    
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
pygame.mixer.music.load("IB_computer_science_coursework/game/8bit sound track.mp3")
pygame.mixer.music.play(-1)


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
    
    
    
    
    

    
    
    



