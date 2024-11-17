import pygame
import random

mole_position = (0, 0)

def move_mole():
    global mole_position
    mole_position = (random.randrange(0, 640, 32), random.randrange(0, 512, 32))

def check_event(position):
    global mole_position
    x, y = position
    column = x // 32
    row = y // 32
    if (column * 32, row * 32) == mole_position:
        move_mole()



#made a comment
def main():
    global mole_position
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        mole_rect = mole_image.get_rect()
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            screen.fill("light blue")
            for i in range(0,640,32):
                pygame.draw.line(screen, "black", (i, 0),(i,512))
            for i in range(0,512,32):
                pygame.draw.line(screen, "black", (0,i), (640,i))
            mole_rect.topleft = mole_position
            screen.blit(mole_image, mole_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    check_event(event.pos)

            pygame.display.flip()
            clock.tick(60)

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
