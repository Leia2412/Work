pip install pygame
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Custom Event Example")
# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Sprite positions
sprite1 = pygame.Rect(50, 100, 60, 60)
sprite2 = pygame.Rect(200, 100, 60, 60)

sprite1_color = RED
sprite2_color = BLUE
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)  # trigger every 2 seconds
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle custom event
        if event.type == CHANGE_COLOR_EVENT:
            # Swap colors
            sprite1_color, sprite2_color = sprite2_color, sprite1_color

    # Draw sprites
    screen.fill((255, 255, 255))  # background
    pygame.draw.rect(screen, sprite1_color, sprite1)
    pygame.draw.rect(screen, sprite2_color, sprite2)
    pygame.display.flip()

pygame.quit()
