import pygame
import os


pygame.init()

screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height))

showSplashScreen = False
splashImage = pygame.image.load("desireCreativeLogo.png").convert()
image_rect = splashImage.get_rect()



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if running == True:
            showSplashScreen = True

    screen.fill((0, 0, 0))

    screen.blit(splashImage, image_rect)

    pygame.display.flip()
    
pygame.quit()