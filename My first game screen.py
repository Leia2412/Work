import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
window_size = (500, 500)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("My first game screen")

# Define colors
grey = (58, 58, 58)

# Load and scale the image
image = pygame.image.load("your_image.png")  # Replace with your image filename
image = pygame.transform.scale(image, (300, 300))

# Get image position (centered)
image_rect = image.get_rect(center=(window_size[0] // 2, window_size[1] // 2))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.