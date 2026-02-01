"""asteroidfield.py

Handles timed spawning of asteroids from off-screen edges.

The module defines `AsteroidField`, a small manager sprite that periodically
creates new `Asteroid` instances at randomized positions along the screen
edges and gives them an initial velocity pointing into the play area.
"""

import pygame
import random
from asteroid import Asteroid
from constants import *


class AsteroidField(pygame.sprite.Sprite):
    """Sprite that manages when and where to spawn asteroids.

    `edges` contains entries of the form [direction_vector, position_fn]. The
    direction vector indicates the general velocity direction (pointing into
    the screen) and `position_fn` maps a normalized coordinate (0..1) to a
    concrete spawn position along that edge. ASTEROID_MAX_RADIUS is used so
    asteroids are created just off-screen.
    """

    edges = [
        # From the left edge, velocity points right
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        # From the right edge, velocity points left
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        # From the top edge, velocity points down
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        # From the bottom edge, velocity points up
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        """Initialize spawn timer and register sprite containers."""
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        """Create and configure a new `Asteroid`.

        The asteroid is created at `position` with the requested `radius` and
        is given the provided `velocity`. Any group registration is handled
        by the base sprite mechanics or elsewhere in the code.
        """
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        """Advance the spawn timer and spawn a new asteroid when ready.

        - `dt` is the elapsed time since the last update (seconds).
        - When the timer exceeds `ASTEROID_SPAWN_RATE_SECONDS` a random edge
          is selected and an asteroid is spawned with randomized size and
          velocity (speed plus a small random angle offset).
        """
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE_SECONDS:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)

            # pick a random speed and give the edge direction that speed
            speed = random.randint(40, 100)
            velocity = edge[0] * speed

            # add a small random angular variation so asteroid trajectories vary
            velocity = velocity.rotate(random.randint(-30, 30))

            # choose a random location along the selected edge
            position = edge[1](random.uniform(0, 1))

            # choose a size category for the asteroid
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
