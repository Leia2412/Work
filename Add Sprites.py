import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Sprite Movement")
clock = pygame.time.Clock()
# Rectangles: x, y, width, height
sprite1 = pygame.Rect(50, 50, 60, 60)   # Controlled sprite
sprite2 = pygame.Rect(200, 200, 80, 80) # Static sprite

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        sprite1.y -= 5
    if keys[pygame.K_DOWN]:
        sprite1.y += 5
    if keys[pygame.K_LEFT]:
        sprite1.x -= 5
    if keys[pygame.K_RIGHT]:
        sprite1.x += 5

    screen.fill((255, 255, 255))  # White background
    pygame.draw.rect(screen, (0, 0, 255), sprite1)  # Blue
    pygame.draw.rect(screen, (255, 0, 0), sprite2)  # Red
    pygame.display.flip()
    clock.tick(30)

pygame.quit()