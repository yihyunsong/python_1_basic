import pygame 

pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load("4_game/images/background.png")

pygame.display.set_caption("Yihyuns shooting game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (50,50))

    pygame.display.update()

pygame.quit()