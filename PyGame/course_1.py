import pygame

successes, fails = pygame.init()
print(successes, fails)

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("TOP GAME")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

x = 100
y = 200
width = 50
height = 50

while True:
    
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    keys = pygame.key.get_pressed()

    pygame.draw.rect(screen, RED, (x, y, width, height))
    pygame.display.update()