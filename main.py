import pygame
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    # Initialize pygame
    pygame.init()

    # Create new clock object
    clock = pygame.time.Clock()

    # Delta time
    dt = 0

    # Get new instance of GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Instantiate player object
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        log_state()
        for event in pygame.event.get():
            # Close window by close window button
            if event.type == pygame.QUIT:
                return

        # Fill screen with solid black
        screen.fill("black")

        # re-render players each frame
        player.draw(screen)

        # Refresh the screen
        pygame.display.flip()

        # Set delta time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
