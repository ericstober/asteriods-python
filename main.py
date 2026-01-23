import pygame
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    # Initialize pygame
    pygame.init()

    # Get new instance of GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Game loop
    while True:
        log_state()
        for event in pygame.event.get():
            # Close window by close window button
            if event.type == pygame.QUIT:
                return

        # fill screen with solid black
        screen.fill("black")

        # refresh the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()
