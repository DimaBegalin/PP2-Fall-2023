import pygame
import sys
from datetime import datetime

pygame.init()

width, height = 829, 836
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Mouse Clock")

mickey_body = pygame.image.load("./img/main-clock.png")
mickey_right_hand = pygame.image.load("./img/right-hand.png")
mickey_left_hand = pygame.image.load("./img/left-hand.png")

mickey_hand_length = 180
mickey_hand_thickness = 20

def draw_clock(seconds_angle, minutes_angle):
    screen.blit(mickey_body, (width // 2 - mickey_body.get_width() // 2, height // 2 - mickey_body.get_height() // 2))

    rotated_left_hand = pygame.transform.rotate(mickey_left_hand, seconds_angle)
    left_hand_rect = rotated_left_hand.get_rect(center=(width // 2, height // 2))
    screen.blit(rotated_left_hand, left_hand_rect)

    rotated_right_hand = pygame.transform.rotate(mickey_right_hand, minutes_angle)
    right_hand_rect = rotated_right_hand.get_rect(center=(width // 2, height // 2))
    screen.blit(rotated_right_hand, right_hand_rect)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time = datetime.now().time()
    seconds = current_time.second
    minutes = current_time.minute

    seconds_angle = -(seconds / 60) * 360 + 90
    minutes_angle = -(minutes / 60) * 360 + 90

    screen.fill((255, 255, 255))

    draw_clock(seconds_angle, minutes_angle)

    pygame.display.flip()

    clock.tick(60)
