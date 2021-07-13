import pygame
import time
import math

pygame.init()
resX = 1280
resY = 720
screen = pygame.display.set_mode((resX,resY))

#Background Phase
phase = 0
#Turns (between sheep and wolf)
turn = 0
selected_wolf = 0

#Name of the window
pygame.display.set_caption("Sheep & Wolf")

#Loading images using variables
bg = pygame.image.load('Background1.png') 
bg2 = pygame.image.load('Background2.png') 
exit_button = pygame.image.load('exit.png') 
play_button = pygame.image.load('play.png') 
sheep_icon = pygame.image.load('sheep.png')
wolf_icon = pygame.image.load('wolf.png')
sheep_block = pygame.image.load('sheep_block.png') 
wolf_block = pygame.image.load('wolf_block.png') 
wolf_select = pygame.image.load('select_wolf.png') 
sheep_lost = pygame.image.load('sheep_lost.png') 
wolves_lost = pygame.image.load('wolves_lost.png') 

block_size = (70, 66)

#Sheep and wolf positioning
sheep_x = 4
sheep_y = 7
wolf1_x = 1
wolf1_y = 0
wolf2_x = 3
wolf2_y = 0
wolf3_x = 5
wolf3_y = 0
wolf4_x = 7
wolf4_y = 0

screen.fill((0, 0, 0))
        
screen.blit(bg, (0,0))
screen.blit(play_button, (492,329))
screen.blit(exit_button, (492,460))


#start of the program
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if(mouse[0] >= 492 and mouse[0] <= 789 and mouse[1] >= 329 and mouse[1] <= 444):
                    phase = 1
                if(mouse[0] >= 492 and mouse[0] <= 789 and mouse[1] >= 460 and mouse[1] <= 535):
                    running = False
    
    if (phase == 1):
        screen.blit(bg2, (0,0))
        
#Display update necessary for any image to appear or change        
    pygame.display.update()
