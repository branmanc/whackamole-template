import pygame
import random

def drawgrid(screen):
    for x in range (0, 640, 32):
        pygame.draw.line(screen, "black", (x, 0), (x, 512))

    for y in range(0, 512, 32):
        pygame.draw.line(screen, "black", (0, y), (640, y))

def random_position():

    col = random.randrange(0, 20)
    row = random.randrange(0, 16)
    return col *32, row *32
##



def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True

        mole_x, mole_y = 0, 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    mole_rec = mole_image.get_rect(topleft = (mole_x, mole_y))
                    if mole_rec.collidepoint(mouse_x, mouse_y):
                        mole_x, mole_y = random_position()
            screen.fill("light green")
            drawgrid(screen)
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x,mole_y)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
