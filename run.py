import sys, pygame
from core.character import Character
from core.location import Location
from core.walkman import Walkman

pygame.init()

size = width, height = 800, 600
FPS = 60
current_frame = 0
MAX_FRAMES = 60
ANIMATION_SPEED = 15

clock = pygame.time.Clock()
location = Location()
character = Character()
walkman = Walkman(character.get_tapes())
walkman.load_songs()

time = 0
FULLTIME = 60

screen = pygame.display.set_mode(size)
    
while True:
    
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
    if walkman.is_open():
        walkman.draw(screen)
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYUP:
            character.idle()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                walkman.open()
            if walkman.is_open():
                if event.key == pygame.K_o:
                    walkman.close()
                if event.key == pygame.K_i:
                    walkman.play()
    pygame.display.flip()
    time += 1
    if time >= 60:
        time = 0
    clock.tick(FPS)