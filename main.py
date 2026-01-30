import sys
import pygame
from constants import SCREEN_HEIGHT
from constants import SCREEN_WIDTH
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


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

    # Create empty group to hold all the objects that can be updated
    updatable = pygame.sprite.Group()

    # Create empty group to hold all the object that can be drawn
    drawable = pygame.sprite.Group()

    # Create empty group to hold all the asteriods
    asteroids = pygame.sprite.Group()

    # Add the Player class to the updatable and drawable groups
    Player.containers = (updatable, drawable)

    # Add the Asteriod class to the asteriods, updatable, and drawable groups
    Asteroid.containers = (asteroids, updatable, drawable)

    # Add the AsteriodField class to the updatable group
    AsteroidField.containers = updatable

    # Create the player at the center of the screen
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    # Create the asteroid field
    asteroid_field = AsteroidField()

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

        # Update all updatable objects state (movement and rotation based on input)
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        # Draw all of the drawable objects
        for object in drawable:
            object.draw(screen)

        # Update the full display surface to the screen
        pygame.display.flip()


if __name__ == "__main__":
    main()
