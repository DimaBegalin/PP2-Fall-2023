import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Ball")

ball_radius = 25
ball_color = (255, 0, 0)
ball_pos = [width // 2, height // 2]

speed = 5
target_pos = list(ball_pos)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                target_pos[1] = max(ball_radius, target_pos[1] - 20)
            elif event.key == pygame.K_DOWN:
                target_pos[1] = min(height - ball_radius, target_pos[1] + 20)
            elif event.key == pygame.K_LEFT:
                target_pos[0] = max(ball_radius, target_pos[0] - 20)
            elif event.key == pygame.K_RIGHT:
                target_pos[0] = min(width - ball_radius, target_pos[0] + 20)

    direction = [target_pos[0] - ball_pos[0], target_pos[1] - ball_pos[1]]
    distance = min(speed, pygame.math.Vector2(direction).length())
    if direction[0] != 0 or direction[1] != 0:
        normalized_direction = pygame.math.Vector2(direction).normalize()
        ball_pos[0] += normalized_direction[0] * distance
        ball_pos[1] += normalized_direction[1] * distance

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, ball_color, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)
    pygame.display.flip()

    clock.tick(60)
