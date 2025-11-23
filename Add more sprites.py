import pygame
import random

# Initialize pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader Project - Part 1")

# Colors
WHITE = (255, 255, 255)

# Player setup
player = pygame.Rect(370, 480, 40, 40)

# Enemy setup (7 enemies at random positions)
enemies = []
for i in range(7):
    x = random.randint(0, 760)
    y = random.randint(50, 150)
    enemies.append(pygame.Rect(x, y, 40, 40))

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw player
    pygame.draw.rect(screen, (0, 0, 255), player)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)

        # Collision detection
        if player.colliderect(enemy):
            score += 1
            # Reset enemy position
            enemy.x = random.randint(0, 760)
            enemy.y = random.randint(50, 150)

    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
