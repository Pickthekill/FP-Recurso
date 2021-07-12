import pygame
import time
import math

pygame.init()
resX = 1280
resY = 720
screen = pygame.display.set_mode((resX,resY))

pygame.display.set_caption("Sheep & Wolf")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False