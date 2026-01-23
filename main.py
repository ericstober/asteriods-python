import pygame
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    # Print startup message with the current pygame version
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")

    # Initialize all imported pygame modules
    pygame.init()

    # Create a clock to manage frame rate and delta time
    clock = pygame.time.Clock()

    # Delta time (seconds since last frame), used for frame-independent movement
    dt = 0

    # Create the main game window (surface) with configured dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create the player at the center of the screen
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    # Main game loop (runs once per frame)
    while True:
        # Debug logging for inspecting game state
        log_state()

        # Process all pending pygame events
        for event in pygame.event.get():
            # Exit the game when the window close button is pressed
            if event.type == pygame.QUIT:
                return

        # Calculate delta time and cap the frame rate at 60 FPS
        dt = clock.tick(60) / 1000

        # Clear the screen by filling it with black
        screen.fill("black")

        # Update player state (movement and rotation based on input)
        player.update(dt)

        # Draw the player to the screen
        player.draw(screen)

        # Update the full display surface to the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
