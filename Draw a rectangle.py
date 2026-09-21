import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(50, 30, 60, 80))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(150, 80, 60, 80))
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(250, 130, 60, 80))

    pygame.display.flip()