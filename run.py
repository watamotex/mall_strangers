import sys, pygame
from core.character import Character
from core.location import Location

pygame.init()

size = width, height = 800, 600
FPS = 60
current_frame = 0
MAX_FRAMES = 60
ANIMATION_SPEED = 15

clock = pygame.time.Clock()
location = Location()
character = Character()
time = 0
FULLTIME = 60

screen = pygame.display.set_mode(size)
    
while True:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYUP:
            character.idle()
    keys = pygame.key.get_pressed()
    if keys[ord('w')]:
        character.move('up')
    elif keys[ord('s')]:
        character.move('down')
    elif keys[ord('d')]:
        character.move('right')
    elif keys[ord('a')]:
        character.move('left')
    # animation
    location.draw(screen)
    character.draw(screen, time)
    pygame.display.flip()
    time += 1
    if time >= 60:
        time = 0
    clock.tick(FPS)