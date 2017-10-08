import sys, pygame
from core.character import Character

pygame.init()

size = width, height = 800, 600
FPS = 60
current_frame = 0
MAX_FRAMES = 60
ANIMATION_SPEED = 15

clock = pygame.time.Clock()
character = Character()

screen = pygame.display.set_mode(size)

while True:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # animation
    current_frame += 1
    if current_frame >= MAX_FRAMES + 1:
        current_frame = 0
    if current_frame % ANIMATION_SPEED == 0:
        screen.blit(character.get_sprite(), dest=(0, 0))
    pygame.display.flip()
    clock.tick(FPS)