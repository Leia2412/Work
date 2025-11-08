import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My first game screen")

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)  # You can change this to any color you like

# Set up font
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to my game!", True, BLUE)

# Rectangle setup
rect_width, rect_height = 100, 60
rect_x = (screen_width - rect_width) // 2
rect_y = (screen_height - rect_height) // 2
rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

# Game loop
running = True
while running:
    screen.fill(WHITE)
    screen.blit(text, (screen_width // 2 - text.get_width() // 2, 50))
    pygame.draw.rect(screen, BLUE, rectangle)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
