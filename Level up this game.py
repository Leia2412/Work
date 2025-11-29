import pygame

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invader")

# Background image
background = pygame.image.load("background.png")  # make sure the file is in your project folder

# Background sound
pygame.mixer.music.load("background.wav")  # use .wav or .mp3
pygame.mixer.music.play(-1)  # -1 means loop forever

# Game loop
running = True
while running:
    # Fill screen with black before drawing
    screen.fill((0, 0, 0))

    # Draw background
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update display
    pygame.display.update()
