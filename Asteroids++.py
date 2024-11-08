import pygame
import time
import sys
import random
import math
import numpy
from numpy import *
# from math import cos, sin, pi


#inisiallising pygame and sound library
pygame.init()
pygame.mixer.init()

#sound credits: William Benckert - Glitching Through the Sky 
#Theme source: https://lospec.com/palette-list

# GAME DESCRIPTION---------------------------------------------------------------------------------
# a simple asteroid game where the player has to survive for as long as possible while also
# shooting out transponders as some asteroid will have ores

# LORE DUMP: 
# mining colony in asteroid belt
# task is to fly about and locate ores so that the large mining ships can go collect them...
# future features could include different ship mechanics and upgrade options... 

#Seb TO-DO
# 1) check if the global variable is neccessary 
# 2) some local variable assignment in subroutines is redundant...
# 3) matrix multiplication issues
# 4) volume fade in and out or play pause



#THEMES - these are the theme pallets (sub, accent1,accent2,accent3 and main colour respectively)
#hide all of them...
dark_theme = {
    "s_colour" : (255, 255, 255), # second colour
    "accent_colour_0" : (0, 0, 255), 
    "accent_colour_1" : (0, 255, 0), 
    "accent_colour_2" : (255, 0, 0), 
    "m_colour" : (0, 0, 0), # main colour
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

#saving it to another file 
settings = open("settings.txt", "r")
global current_theme   #global variable terrifing i know...
current_theme = eval(settings.readline())
    
    
#assigning clock speed to clock
clock = pygame.time.Clock()



#OBJECTS
#asteroid objects
class Asteroids():
    
    def __init__(self):
        self.size = 10
        self.vector = 10
        self.speed = 10
        
        #not in use yet
        #pygame.draw.polygon()
        
    #other characteristics 
    def collisions():
        pass
    def transpoded():
        pass
    def gone():
        pass     
#space ship rocket objects 
class Ship():

    def __init__(self, colours, shapes): #creation and eastheitic characteristics
        self.colour =  colours            
        self.shape = shapes

    def movement(self): #velocities, not implimented yet. This is to introduct acceleration...
        self.xvel = 0
        self.yvel = 0 
    
    def shoot(self):  #not implimented yet but this is to manage shooting capabilities 
        self.fired = False
        self.reload = 0.3
    
    def death(self):  #death can only be delayed...
        self.death = False
#transponder objects
class transponder(): # not implimetned yet....
    
    def __init__(self):
        pass

    def fired():
        pass
    
    def hit():
        pass
    
    def miss():
        pass
#buttons
class button(): #how i create all the buttons
    
    #I create them bassed off certain desired characteristics....
    def __init__(self, x = int, y = int, text = str, function = str,back =str , clicked = False, width = 350, height = 90, textsize = 75):
        
        #characteristics...self evident names...
        self.coordinates = [x, y]
        self.size = [width, height]
        self.fillcolour = current_theme["s_colour"]  
        self.content = text
        self.function = function
        self.back = back
        self.textcolour = current_theme["s_colour"]
        self.click = clicked
        self.textsize = textsize
        
        #this is to detect which one is selected and highlight the button
    def clicking(self, clicked):
        
        self.click = clicked
        
        #if selected flip the fillcolour and text colour around if not leave
        if self.click == True:
                self.textcolour = current_theme["m_colour"]
                self.fillcolour = current_theme["s_colour"]
        else:
            self.textcolour = current_theme["s_colour"]
            self.fillcolour = current_theme["m_colour"]
           
 
#SUB-FUNCTIONS  

#MATRIX MULTIPLICATION FOR OBJECT ROTATION         
# get the coordinates of each point and the desired turning angle
def Matrix_multy_r(coordinates, angle): 
    
    # https://en.wikipedia.org/wiki/2D_computer_graphics#Non-standard_orientation_of_the_coordinate_system
    
    #define 2d rotation matrix
    b = [[cos(angle), -sin(angle)],
         [sin(angle), cos(angle)]]
    
    #multiply the matric and output
    return numpy.dot(coordinates,b)
    
    ##Combined transformation and rotation matrix
    
    # b = [[cos(angle), sin(angle), 0],
    #      [-sin(angle), cos(angle), 0],
    #      [point[0], point[1], 1]]
    
    
    # c = [[1,0,0],
    #      [0,1,0],
    #      [-point[0], -point[1], 1]] 
 

    # reasult2 = numpy.dot(reasult,c)
    # print(str(reasult2) + "reasult2")
    # return reasult2
    
    
#A ONE LINER SUBFUNCTION TO CREATE BUTTON OBJECT        
#button_frame to make life easy            
def button_frame(lattitude, number, content, function, back, clicked): 
    return button(screen_width/10*lattitude, screen_height/13*number, content, function, back, clicked)
  
  
#THE MENU PAGE      
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

#THE GAME PAGE...NOT REALLY A PAGE
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
   
   
#THIS FUNCTION WORKS WITH SETTINGS FUNTION TO CHANGE THE VOLUME         
def volumes():

    #if music on pause else play...EASY
    if pygame.mixer.music.get_busy() == True: 
        pygame.mixer.music.fadeout(0.5) # stop playback of all sound channels: pygame.mixer.music.fadeout | pygame.mixer.music.stop | pygame.mixer.music.pause()

    elif pygame.mixer.music.get_busy() == False: 
        pygame.mixer.music.fadein(0.5) 

#THIS FUNCTION WORKS WITH SETTINGS FUNCTION TO CHANGE THE THEME 
def themes():
    
    global current_theme   # terrible i know
    #I don't know this effects global and local variables as i don't think i should be calling them in here....
    themes = [dark_theme,light_theme,Twilight_5_Palette,Ink_Palette,leopold_s_dreams_Palette,Sunset_Red_Palette,five_sheep,slimy_05_Palette,NEO_5_Palette]
    
    #read from external file
    settings = open("settings.txt", "r")
    current_theme = eval(settings.readline())
    
    #write the next theme by cycling through
    settings = open("settings.txt", "w")
    settings.write(str(themes[(current_theme["current"] + 1) % len(themes)]))
    
    #same issue about not needing to do this as it is localscope?              
    settings = open("settings.txt", "r")       
    current_theme = eval(settings.readline())       

#SETTINGS PAGE
def settings():
    #create buttons
    volume_button = button_frame(5, 4, "VOLUME", "volumes()", "Menu()", False)
    theme = button_frame(5, 6, "THEME", "themes()", "Menu()", False)

    list_buttons = [volume_button, theme]

    #start loop and set location too 0      
    location = 0
    setting = True
    while setting == True:
        
        #fill screen balck and call background animation
        screen.fill(current_theme["m_colour"])
        background()
        
        # set move variableto 0 so that the selection stops moving up or down and ask for user input
        move = 0
        user_input = userinput()
        
        #if input match...
        if user_input == "w": move = -1
        elif user_input == "s": move = 1 
        elif user_input == 13: # check for every button what their function is and call it
            for item in list_buttons:
                if item.click == True: 
                    eval(item.function)
        elif user_input == "esc": #check for every button what their back function is and call it....NOT neccesry for a for loop but could be usefull
            for item in list_buttons:
                if item.click == True: 
                    eval(item.back)
        else: move = 0 # else do not move selector
             
             
        #the location of the selector is added by the move
        location = location + int(move)
        location = location % len(list_buttons) #the location is then modulode by the number of buttons so that it does not overflow

        
        #for every buuton check if the location matches it, selecte it if it does
        for buttons in list_buttons:
            if buttons == list_buttons[location]: 
                list_buttons[location].clicking(True)
            
            else:
                buttons.clicking(False)
            
            #draw the buttons and selector square
            pygame.draw.rect(screen, buttons.fillcolour, (buttons.coordinates[0] - buttons.size[0]/2, buttons.coordinates[1] - buttons.size[1]/2, buttons.size[0], buttons.size[1]),0, 2, 3)
            subtitle = pygame.font.SysFont("Helvetic", buttons.textsize).render(buttons.content, True, buttons.textcolour)
            screen.blit(subtitle,(buttons.coordinates[0] - 150, buttons.coordinates[1]- 20))
        
        #draw the title 
        title = pygame.font.SysFont("Helvetic", 200).render(" SETTINGS  ", True, current_theme["s_colour"])
        screen.blit(title, (screen_width/2-title.get_width()/2, screen_height/13*2-title.get_height()/2)) 
            
        #update screen
        pygame.display.flip()

#THIS FUNCTION WORKS WITH SETTINGS FUNCTION TO CHANGE THE CHARACTER
def change():
    #reads the current character cheet from the save file
    characters = open("character.txt", "r")
    current_character = eval(characters.readline())

    #Matches the current ship to the differetn types as changes it...this is dones by looking at and assigning the current key in the dictionary
    match current_character["current"]: 
        case 0:
            characters = open("character.txt", "w")
            characters.write(str({"triangle": ([-20,40],[0,15],[20,40]), "arrow": ([-20,40],[0,-15],[20,40],[0,15]), "current": 1}))
      
        case 1:
            characters = open("character.txt", "w")
            characters.write(str({"triangle": ([-20,40],[0,15],[20,40]), "arrow": ([-20,40],[0,-15],[20,40],[0,15]), "current": 0}))
    
    
    #I DON'T BELIVE THIS IS NECCESSARY AS THIS VARIABLE IS IN A LOCAL SCOPE SO IT DOES NOT MATTER??              
    characters = open("character.txt", "r")       
    current_character = eval(characters.readline())  
       
#THIS IS THE SHIP/CHARACTER PAGE
def character():
    
    #Instead of leaving it as a frame work for a menu i optimsied it, this means it will nee to be drastically changed if i want to add another button...
    
    #creates a change button by calling the button subfunction and creating an object 
    changes = button_frame(5, 4, "CHANGE", "change()", "Menu()", False)
          
    #starts a loop       
    characterising = True
    while characterising == True:
       
        #screen fill with main colour and run background animation
        screen.fill(current_theme["m_colour"])
        background()
        
        #this bassically causes the square to light up...
        changes.clicking(True)
        
        #ask for user input
        user_input = userinput()

        #if user input is equal to enter than check if the button
        if user_input == 13:
                eval(changes.function)
        elif user_input == "esc":
                eval(changes.back)
        else: pass
             

        #This highlites the button and writes the text inside the button     
        pygame.draw.rect(screen, changes.fillcolour, (changes.coordinates[0] - changes.size[0]/2, changes.coordinates[1] - changes.size[1]/2, changes.size[0], changes.size[1]),0, 2, 3)
        subtitle = pygame.font.SysFont("Helvetic", changes.textsize).render(changes.content, True, changes.textcolour)
        screen.blit(subtitle,(changes.coordinates[0] - 150, changes.coordinates[1]- 20))
    
        
        #This gets the information from the character file
        characters = open("character.txt", "r")
        current_character = eval(characters.readline())

        match current_character["current"]:  
                       
            # for every point of the ship change the coordinates so that they fit inside the square
            case 0:
                verteces = current_character["triangle"]
                for vertex in  verteces:
                    vertex[0] = int(screen_width/2 - vertex[0]*5) #change the x so it is 5 times away from the center line of the screen
                    vertex[1] = int(screen_height/13*7 + vertex[1]*5 - 100) 
                
            case 1:
                verteces = current_character["arrow"]       
                for vertex in verteces:
                    vertex[0] = int(screen_width/2 - vertex[0]*5)
                    vertex[1] = int(screen_height/13*7 + vertex[1]*5 - 60)
                    
        #this draws the verteces
        pygame.draw.polygon(screen,current_theme["s_colour"], verteces, 5)
        pygame.draw.rect(screen, current_theme["s_colour"], (screen_width/10*5 - 175, screen_height/13*7 - 150, 350, 300),5, 2, 3)
        
        #this draws the title at the top of the page
        title = pygame.font.SysFont("Helvetic", 200).render("SHIP HANGAR", True, current_theme["s_colour"])
        screen.blit(title, (screen_width/2-title.get_width()/2, screen_height/13*2-title.get_height()/2)) 
            
        #this updates the page
        pygame.display.flip()

#THE EXIT PAGE    
def exit(): # self explanitory?
    pygame.quit()  
    sys.exit()

#THIS IS THE INPUTS FUNCTION
def userinput():
    for event in pygame.event.get(): # gets the registered keys of the events stack 
        if event.type == pygame.QUIT: exit() # if the event is the close button than exit
        if event.type == pygame.KEYUP:      #if a key is released match the event to the following
            match event.key:
                case pygame.K_w: return "w"
                case pygame.K_s: return "s"
                case pygame.K_a: return "a"
                case pygame.K_d: return "d"
                case 13: return 13 # this is the enter key code
                case 769 | 27: return "esc"   #escape key
    return #return nothing, theif!

#THIS DOES THE BACKGROUND STAR ANIMATION 
def background():
    global current_theme  #disgusting stuff..
    #create the locations of the stars for when we animate the background

    for star in star_field_slow: #if the slow stars reach the bottom they get moved back up at a random x and y coordinate
        star[1] += 1
        if star[1] > screen_height: # if it reaches the bottom 
            star[0] = numpy.random.randint(0, screen_width) #ramdom x coordinate bassed off the width of the screen
            star[1] = numpy.random.randint(-20, -5)  # random height 20 to 5 pixels above the screen
        pygame.draw.circle(screen, current_theme["accent_colour_0"], star, 3) # their colour depend on the theme

    for star in star_field_medium: # see above but for medium speed stars
        star[1] += 2
        if star[1] > screen_height:
            star[0] = numpy.random.randint(0, screen_width)
            star[1] = numpy.random.randint(-20, -5)
        pygame.draw.circle(screen, current_theme["accent_colour_1"], star, 2)

    for star in star_field_fast: # see aboce but for fast stars 
        star[1] += 3
        if star[1] > screen_height:
            star[0] = numpy.random.randint(0, screen_width)
            star[1] = numpy.random.randint(-20, -5)
        pygame.draw.circle(screen, current_theme["accent_colour_2"], star, 1)
    
    pygame.time.Clock().tick(30) # caps their speed fps


#NOT IN USE MAKES POLYGONE FOR ASTEROID
# def draw_regular_polygon(surface, color, vertex_count, radius, position, width=0):
#     n, r = vertex_count, radius
#     x, y = position
#     pygame.draw.polygon(surface, color, [(x + r * cos(2 * pi * i / n), y + r * sin(2 * pi * i / n)) for i in range(n)], width)



# Set up the display window
screen_width, screen_height = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((screen_width, screen_height-60))
pygame.display.set_caption("ASTEROIDS++")

#MUSIC
pygame.mixer.music.load("8bitsoundtrack.mp3")
pygame.mixer.music.play(-1) #indefinit play loops



#CREATE THE STARS FOR BACKGROUND, credit: https://gist.github.com/ogilviemt/9b05a89d023054e6279f
star_field_slow = []
star_field_medium = []
star_field_fast = []

for slow_stars in range(200): #200 random x and y coordinates...
    star_loc_x = numpy.random.randint(0, screen_width)
    star_loc_y = numpy.random.randint(0, screen_height)
    star_field_slow.append([star_loc_x, star_loc_y]) 

for medium_stars in range(140): #140 random x and y coordinates
    star_loc_x = numpy.random.randint(0, screen_width)
    star_loc_y = numpy.random.randint(0, screen_height)
    star_field_medium.append([star_loc_x, star_loc_y])

for fast_stars in range(60): #60 random x and y coordinates
    star_loc_x = numpy.random.randint(0, screen_width)
    star_loc_y = numpy.random.randint(0, screen_height)
    star_field_fast.append([star_loc_x, star_loc_y])


#The start
Menu()
    
    
    
    
    

    
    
    



