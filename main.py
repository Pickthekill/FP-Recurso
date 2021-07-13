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
bg1 = pygame.image.load('Background1.png') 
bg2 = pygame.image.load('Background2.png')
bg3 = pygame.image.load('Background3.png') 
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


#start of the program
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if (phase == 1):
            if(sheep_x == 0):
                if(wolf1_x == sheep_x + 1 and wolf1_y == sheep_y - 1 or wolf2_x == sheep_x + 1 and wolf2_y == sheep_y - 1 or wolf3_x == sheep_x + 1 and wolf3_y == sheep_y - 1 or wolf4_x == sheep_x + 1 and wolf4_y == sheep_y - 1):
                    if(wolf1_x == sheep_x + 1 and wolf1_y == sheep_y + 1 or wolf2_x == sheep_x + 1 and wolf2_y == sheep_y + 1 or wolf3_x == sheep_x + 1 and wolf3_y == sheep_y + 1 or wolf4_x == sheep_x + 1 and wolf4_y == sheep_y + 1):
                        phase = 2
            elif (sheep_x == 7):
                if (wolf1_x == sheep_x - 1 and wolf1_y == sheep_y - 1 or wolf2_x == sheep_x - 1 and wolf2_y == sheep_y - 1 or wolf3_x == sheep_x - 1 and wolf3_y == sheep_y - 1 or wolf4_x == sheep_x - 1 and wolf4_y == sheep_y - 1):
                    if (wolf1_x == sheep_x - 1 and wolf1_y == sheep_y + 1 or wolf2_x == sheep_x - 1 and wolf2_y == sheep_y + 1 or wolf3_x == sheep_x - 1 and wolf3_y == sheep_y + 1 or wolf4_x == sheep_x - 1 and wolf4_y == sheep_y + 1):
                        phase = 2
            elif (wolf1_x == sheep_x - 1 and wolf1_y == sheep_y - 1 or wolf2_x == sheep_x - 1 and wolf2_y == sheep_y - 1 or wolf3_x == sheep_x - 1 and wolf3_y == sheep_y - 1 or wolf4_x == sheep_x - 1 and wolf4_y == sheep_y - 1):
                if(wolf1_x == sheep_x + 1 and wolf1_y == sheep_y - 1 or wolf2_x == sheep_x + 1 and wolf2_y == sheep_y - 1 or wolf3_x == sheep_x + 1 and wolf3_y == sheep_y - 1 or wolf4_x == sheep_x + 1 and wolf4_y == sheep_y - 1):
                    if(wolf1_x == sheep_x + 1 and wolf1_y == sheep_y + 1 or wolf2_x == sheep_x + 1 and wolf2_y == sheep_y + 1 or wolf3_x == sheep_x + 1 and wolf3_y == sheep_y + 1 or wolf4_x == sheep_x + 1 and wolf4_y == sheep_y + 1):
                        if (wolf1_x == sheep_x - 1 and wolf1_y == sheep_y + 1 or wolf2_x == sheep_x - 1 and wolf2_y == sheep_y + 1 or wolf3_x == sheep_x - 1 and wolf3_y == sheep_y + 1 or wolf4_x == sheep_x - 1 and wolf4_y == sheep_y + 1):
                            phase = 2
            
            #Turn action
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                
                if (turn == 0):
                    if (mouse[0] >= (392 + ((sheep_x - 1)*62)) and mouse[0] <= (392 + 62 + ((sheep_x - 1)*62)) and mouse[1] >= (195 + ((sheep_y - 1)*62)) and mouse[1] <= (195 + 62 + ((sheep_y - 1)*62))):
                        if(sheep_x != 0 and sheep_y != 0):
                            sheep_x = sheep_x - 1
                            sheep_y = sheep_y - 1
                            turn = 1
                    if (mouse[0] >= (392 + ((sheep_x + 1)*62)) and mouse[0] <= (392 + 62 + ((sheep_x + 1)*62)) and mouse[1] >= (195 + ((sheep_y - 1)*62)) and mouse[1] <= (195 + 62 + ((sheep_y - 1)*62))):
                        if(sheep_x != 7 and sheep_y != 0):
                            sheep_x = sheep_x + 1
                            sheep_y = sheep_y - 1
                            turn = 1
                    if (mouse[0] >= (392 + ((sheep_x - 1)*62)) and mouse[0] <= (392 + 62 + ((sheep_x - 1)*62)) and mouse[1] >= (195 + ((sheep_y + 1)*62)) and mouse[1] <= (195 + 62 + ((sheep_y + 1)*62))):
                        if(sheep_x != 0 and sheep_y != 7):
                            sheep_x = sheep_x - 1
                            sheep_y = sheep_y + 1
                            turn = 1
                    if (mouse[0] >= (392 + ((sheep_x + 1)*62)) and mouse[0] <= (392 + 62 + ((sheep_x + 1)*62)) and mouse[1] >= (195 + ((sheep_y + 1)*62)) and mouse[1] <= (195 + 62 + ((sheep_y + 1)*62))):
                        if(sheep_x != 7 and sheep_y != 7):
                            sheep_x = sheep_x + 1
                            sheep_y = sheep_y + 1
                            turn = 1

                if (turn == 1):
                    if(sheep_x == 0):
                        if(wolf1_x == sheep_x + 1 and wolf1_y == sheep_y - 1 or wolf2_x == sheep_x + 1 and wolf2_y == sheep_y - 1 or wolf3_x == sheep_x + 1 and wolf3_y == sheep_y - 1 or wolf4_x == sheep_x + 1 and wolf4_y == sheep_y - 1):
                            if(wolf1_x == sheep_x + 1 and wolf1_y == sheep_y + 1 or wolf2_x == sheep_x + 1 and wolf2_y == sheep_y + 1 or wolf3_x == sheep_x + 1 and wolf3_y == sheep_y + 1 or wolf4_x == sheep_x + 1 and wolf4_y == sheep_y + 1):
                                phase = 2
                    elif (sheep_x == 7):
                        if (wolf1_x == sheep_x - 1 and wolf1_y == sheep_y - 1 or wolf2_x == sheep_x - 1 and wolf2_y == sheep_y - 1 or wolf3_x == sheep_x - 1 and wolf3_y == sheep_y - 1 or wolf4_x == sheep_x - 1 and wolf4_y == sheep_y - 1):
                            if (wolf1_x == sheep_x - 1 and wolf1_y == sheep_y + 1 or wolf2_x == sheep_x - 1 and wolf2_y == sheep_y + 1 or wolf3_x == sheep_x - 1 and wolf3_y == sheep_y + 1 or wolf4_x == sheep_x - 1 and wolf4_y == sheep_y + 1):
                                phase = 2
                    elif (wolf1_x == sheep_x - 1 and wolf1_y == sheep_y - 1 or wolf2_x == sheep_x - 1 and wolf2_y == sheep_y - 1 or wolf3_x == sheep_x - 1 and wolf3_y == sheep_y - 1 or wolf4_x == sheep_x - 1 and wolf4_y == sheep_y - 1):
                        if(wolf1_x == sheep_x + 1 and wolf1_y == sheep_y - 1 or wolf2_x == sheep_x + 1 and wolf2_y == sheep_y - 1 or wolf3_x == sheep_x + 1 and wolf3_y == sheep_y - 1 or wolf4_x == sheep_x + 1 and wolf4_y == sheep_y - 1):
                            if(wolf1_x == sheep_x + 1 and wolf1_y == sheep_y + 1 or wolf2_x == sheep_x + 1 and wolf2_y == sheep_y + 1 or wolf3_x == sheep_x + 1 and wolf3_y == sheep_y + 1 or wolf4_x == sheep_x + 1 and wolf4_y == sheep_y + 1):
                                if (wolf1_x == sheep_x - 1 and wolf1_y == sheep_y + 1 or wolf2_x == sheep_x - 1 and wolf2_y == sheep_y + 1 or wolf3_x == sheep_x - 1 and wolf3_y == sheep_y + 1 or wolf4_x == sheep_x - 1 and wolf4_y == sheep_y + 1):
                                    phase = 2
                    
                    if (sheep_y == 0):
                        phase = 3

                    if (mouse[0] >= (392 + (wolf1_x*62)) and mouse[0] <= (392 + 62 + (wolf1_x*62)) and mouse[1] >= (195 + (wolf1_y*62)) and mouse[1] <= (195 + 62 + (wolf1_y*62))):
                        selected_wolf = 1
                        turn = 2
                    if (mouse[0] >= (392 + (wolf2_x*62)) and mouse[0] <= (392 + 62 + (wolf2_x*62)) and mouse[1] >= (195 + (wolf2_y*62)) and mouse[1] <= (195 + 62 + (wolf2_y*62))):
                        selected_wolf = 2
                        turn = 2
                    if (mouse[0] >= (392 + (wolf3_x*62)) and mouse[0] <= (392 + 62 + (wolf3_x*62)) and mouse[1] >= (195 + (wolf3_y*62)) and mouse[1] <= (195 + 62 + (wolf3_y*62))):
                        selected_wolf = 3
                        turn = 2
                    if (mouse[0] >= (392 + (wolf4_x*62)) and mouse[0] <= (392 + 62 + (wolf4_x*62)) and mouse[1] >= (195 + (wolf4_y*62)) and mouse[1] <= (195 + 62 + (wolf4_y*62))):
                        selected_wolf = 4
                        turn = 2

                if (turn == 2):
                    if (mouse[0] >= (392 + ((wolf1_x - 1)*62)) and mouse[0] <= (392 + 62+ ((wolf1_x - 1)*62)) and mouse[1] >= (195 + ((wolf1_y + 1)*62)) and mouse[1] <= (195 + 62 + ((wolf1_y + 1)*62))):
                        if (selected_wolf == 1 and wolf1_x != 0):
                            turn = 0
                            wolf1_x = wolf1_x - 1
                            wolf1_y = wolf1_y + 1
                    if (mouse[0] >= (392 + ((wolf1_x + 1)*62)) and mouse[0] <= (392 + 62+ ((wolf1_x + 1)*62)) and mouse[1] >= (195 + ((wolf1_y + 1)*62)) and mouse[1] <= (195 + 62 + ((wolf1_y + 1)*62))):
                        if (selected_wolf == 1 and wolf1_x != 7):
                            turn = 0
                            wolf1_x = wolf1_x + 1
                            wolf1_y = wolf1_y + 1
                    if (mouse[0] >= (392 + ((wolf2_x - 1)*62)) and mouse[0] <= (392 + 62+ ((wolf2_x - 1)*62)) and mouse[1] >= (195 + ((wolf2_y + 1)*62)) and mouse[1] <= (195 + 62 + ((wolf2_y + 1)*62))):
                        if (selected_wolf == 2 and wolf2_x != 0):
                            turn = 0
                            wolf2_x = wolf2_x - 1
                            wolf2_y = wolf2_y + 1
                    if (mouse[0] >= (392 + ((wolf2_x + 1)*62)) and mouse[0] <= (392 + 62+ ((wolf2_x + 1)*62)) and mouse[1] >= (195 + ((wolf2_y + 1)*62)) and mouse[1] <= (195 + 62 + ((wolf2_y + 1)*62))):
                        if (selected_wolf == 2 and wolf2_x != 7):
                            turn = 0
                            wolf2_x = wolf2_x + 1
                            wolf2_y = wolf2_y + 1
                    if (mouse[0] >= (392 + ((wolf3_x - 1)*62)) and mouse[0] <= (392 + 62+ ((wolf3_x - 1)*62)) and mouse[1] >= (195 + ((wolf3_y + 1)*62)) and mouse[1] <= (195 + 62 + ((wolf3_y + 1)*62))):
                        if (selected_wolf == 3 and wolf3_x != 0):
                            turn = 0
                            wolf3_x = wolf3_x - 1
                            wolf3_y = wolf3_y + 1
                    if (mouse[0] >= (392 + ((wolf3_x + 1)*62)) and mouse[0] <= (392 + 62+ ((wolf3_x + 1)*62)) and mouse[1] >= (195 + ((wolf3_y + 1)*62)) and mouse[1] <= (195 + 62 + ((wolf3_y + 1)*62))):
                        if (selected_wolf == 3 and wolf3_x != 7):
                            turn = 0
                            wolf3_x = wolf3_x + 1
                            wolf3_y = wolf3_y + 1
                    if (mouse[0] >= (392 + ((wolf4_x - 1)*62)) and mouse[0] <= (392 + 62+ ((wolf4_x - 1)*62)) and mouse[1] >= (195 + ((wolf4_y + 1)*62)) and mouse[1] <= (195 + 62 + ((wolf4_y + 1)*62))):
                        if (selected_wolf == 4 and wolf4_x != 0):
                            turn = 0
                            wolf4_x = wolf4_x - 1
                            wolf4_y = wolf4_y + 1
                    if (mouse[0] >= (392 + ((wolf4_x + 1)*62)) and mouse[0] <= (392 + 62+ ((wolf4_x + 1)*62)) and mouse[1] >= (195 + ((wolf4_y + 1)*62)) and mouse[1] <= (195 + 62 + ((wolf4_y + 1)*62))):
                        if (selected_wolf == 4 and wolf4_x != 7):
                            turn = 0
                            wolf4_x = wolf4_x + 1
                            wolf4_y = wolf4_y + 1
        
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                #play the game
                if(mouse[0] >= 492 and mouse[0] <= 789 and mouse[1] >= 329 and mouse[1] <= 444):
                    turn = 0
                    phase = 1
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
                #exit the game
                if(mouse[0] >= 492 and mouse[0] <= 789 and mouse[1] >= 460 and mouse[1] <= 535):
                    running = False

    
    if (phase == 1):
        screen.blit(bg2, (0,0))

        if (turn == 0):
            #Verificação de esquerda
            if(sheep_x == 0):
                if(not(wolf1_x == sheep_x - 1 and wolf1_y == sheep_y - 1 or wolf2_x == sheep_x - 1 and wolf2_y == sheep_y - 1 or wolf3_x == sheep_x - 1 and wolf3_y == sheep_y - 1 or wolf4_x == sheep_x - 1 and wolf4_y == sheep_y - 1)):
                    screen.blit(sheep_block, (392 + ((sheep_x + 1)*62), 195 + ((sheep_y + 1)*62)))
                    screen.blit(sheep_block, (392 + ((sheep_x + 1)*62), 195 + ((sheep_y - 1)*62)))
            #Verificação de direita
            if(sheep_x == 7):
                if(not(wolf1_x == sheep_x + 1 and wolf1_y == sheep_y - 1 or wolf2_x == sheep_x + 1 and wolf2_y == sheep_y - 1 or wolf3_x == sheep_x + 1 and wolf3_y == sheep_y - 1 or wolf4_x == sheep_x + 1 and wolf4_y == sheep_y - 1)):
                    screen.blit(sheep_block, (392 + ((sheep_x - 1)*62), 195 + ((sheep_y - 1)*62)))
                    screen.blit(sheep_block, (392 + ((sheep_x - 1)*62), 195 + ((sheep_y + 1)*62)))
            #Verificação de cima
            if(sheep_y == 0):
                if(not(wolf1_x == sheep_x + 1 and wolf1_y == sheep_y - 1 or wolf2_x == sheep_x + 1 and wolf2_y == sheep_y - 1 or wolf3_x == sheep_x + 1 and wolf3_y == sheep_y - 1 or wolf4_x == sheep_x + 1 and wolf4_y == sheep_y - 1)):
                    screen.blit(sheep_block, (392 + ((sheep_x + 1)*62), 195 + ((sheep_y + 1)*62)))
                    screen.blit(sheep_block, (392 + ((sheep_x - 1)*62), 195 + ((sheep_y + 1)*62)))
            #Verificação de baixo
            if(sheep_y == 7):
                if(not(wolf1_x == sheep_x + 1 and wolf1_y == sheep_y - 1 or wolf2_x == sheep_x + 1 and wolf2_y == sheep_y - 1 or wolf3_x == sheep_x + 1 and wolf3_y == sheep_y - 1 or wolf4_x == sheep_x + 1 and wolf4_y == sheep_y - 1)):
                    screen.blit(sheep_block, (392 + ((sheep_x - 1)*62), 195 + ((sheep_y - 1)*62)))
                    screen.blit(sheep_block, (392 + ((sheep_x + 1)*62), 195 + ((sheep_y - 1)*62)))
            else:
                if(not(wolf1_x == sheep_x + 1 and wolf1_y == sheep_y - 1 or wolf2_x == sheep_x + 1 and wolf2_y == sheep_y - 1 or wolf3_x == sheep_x + 1 and wolf3_y == sheep_y - 1 or wolf4_x == sheep_x + 1 and wolf4_y == sheep_y - 1)):
                    screen.blit(sheep_block, (392 + ((sheep_x - 1)*62), 195 + ((sheep_y - 1)*62)))
                    screen.blit(sheep_block, (392 + ((sheep_x + 1)*62), 195 + ((sheep_y + 1)*62)))
                    screen.blit(sheep_block, (392 + ((sheep_x + 1)*62), 195 + ((sheep_y - 1)*62)))
                    screen.blit(sheep_block, (392 + ((sheep_x - 1)*62), 195 + ((sheep_y + 1)*62)))

        if (turn == 1):
            screen.blit(wolf_select, (392 + (wolf1_x*62), 195 + (wolf1_y*62)))
            screen.blit(wolf_select, (392 + (wolf2_x*62), 195 + (wolf2_y*62)))
            screen.blit(wolf_select, (392 + (wolf3_x*62), 195 + (wolf3_y*62)))
            screen.blit(wolf_select, (392 + (wolf4_x*62), 195 + (wolf4_y*62)))

        if (turn == 2):
            if (selected_wolf == 1):
                if(wolf1_x != 0):
                    screen.blit(wolf_select, (392 + ((wolf1_x - 1)*62), 195 + ((wolf1_y + 1)*62)))
                if(wolf1_x != 7):
                    screen.blit(wolf_select, (392 + ((wolf1_x + 1)*62), 195 + ((wolf1_y + 1)*62)))
            if (selected_wolf == 2):
                if(wolf2_x != 0):
                    screen.blit(wolf_select, (392 + ((wolf2_x - 1)*62), 195 + ((wolf2_y + 1)*62)))
                if(wolf2_x != 7):
                    screen.blit(wolf_select, (392 + ((wolf2_x + 1)*62), 195 + ((wolf2_y + 1)*62)))
            if (selected_wolf == 3):
                if(wolf3_x != 0):
                    screen.blit(wolf_select, (392 + ((wolf3_x - 1)*62), 195 + ((wolf3_y + 1)*62)))
                if(wolf3_x != 7):
                    screen.blit(wolf_select, (392 + ((wolf3_x + 1)*62), 195 + ((wolf3_y + 1)*62)))
            if (selected_wolf == 4):
                if(wolf4_x != 0):
                    screen.blit(wolf_select, (392 + ((wolf4_x - 1)*62), 195 + ((wolf4_y + 1)*62)))
                if(wolf4_x != 7):
                    screen.blit(wolf_select, (392 + ((wolf4_x + 1)*62), 195 + ((wolf4_y + 1)*62)))

        #Sheep and wolves icons
        screen.blit(sheep_icon, (392 + (sheep_x*62), 195 + (sheep_y*62)))
        screen.blit(wolf_icon, (388 + (wolf1_x*62), 195 + (wolf1_y*62)))
        screen.blit(wolf_icon, (388 + (wolf2_x*62), 195 + (wolf2_y*62)))
        screen.blit(wolf_icon, (388 + (wolf3_x*62), 195 + (wolf3_y*62)))
        screen.blit(wolf_icon, (388 + (wolf4_x*62), 195 + (wolf4_y*62)))

    elif (phase == 2):
        screen.blit(bg3, (0,0))
        screen.blit(sheep_lost, (243, 45))
        screen.blit(play_button, (492,329))
        screen.blit(exit_button, (492,460))
    elif (phase == 3):
        screen.blit(bg3, (0,0))
        screen.blit(wolves_lost, (243, 45))
        screen.blit(play_button, (492,329))
        screen.blit(exit_button, (492,460))
    else:
        screen.blit(bg1, (0,0))
        screen.blit(play_button, (492,329))
        screen.blit(exit_button, (492,460))

#Display update necessary for any image to appear or change        
    pygame.display.update()
