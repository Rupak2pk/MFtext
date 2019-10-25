#!/usr/bin/python3

#As a player I want to open the game up because I actually want to pick it up.

#example of a title screen

#importing pygame cause why not
import pygame
import os
import random
pygame.init()
pygame.mouse.set_cursor(*pygame.cursors.arrow)


#image path
current_path = os.path.dirname(__file__) # Where your .py file is locatedh
image_path = os.path.join(current_path, 'Graphics') # The image folder path
#colors 
black = (0,0,0)
white = (255, 255, 255)
green = (0, 225, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

#opening the window
size = (1000, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("test")
carryOn = True
class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        width = 1
        height = 1
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load(os.path.join(image_path, 'goodmouse.png'))
        self.rect = self.image.get_rect()
    def update(self):
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        
        self.rect.x = x
        self.rect.y = y
        
class test(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        width = 20
        height = 15
        self.image = pygame.Surface([width, height])
        self.image = pygame.image.load(os.path.join(image_path, 'itworks.png'))
        self.rect = self.image.get_rect()       
        
all_sprites_list = pygame.sprite.Group()
clock = pygame.time.Clock()        
player = Cursor()
image = test()
all_sprites_list.add(player)
all_sprites_list.add(image)
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
    pygame.mouse.set_visible(False)
    all_sprites_list.update()
    #title screen starter          
    screen.fill(blue)
    all_sprites_list.draw(screen)
    pygame.display
    pygame.display.flip()
    clock.tick(60)
    #updating sprite

    
    
    
pygame.quit()