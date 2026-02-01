"""asteroid.py

Lightweight wrapper for asteroid behavior used by the game.

Defines the Asteroid class which draws itself as a circle, updates its
position using a velocity vector, and can split into two smaller asteroids
when destroyed (unless already at the minimum size).
"""

import random  # used to choose a random split angle
import pygame  # used for drawing
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    """A moving circular asteroid.

    Inherits from `CircleShape` which provides basic position/velocity
    behavior. Asteroids can be drawn, updated each frame, and split into
    two smaller asteroids when destroyed.
    """

    def __init__(self, x, y, radius):
        """Create an asteroid at (x, y) with the given radius.

        Position and velocity are provided by the base `CircleShape` class.
        """
        super().__init__(x, y, radius)

    def draw(self, screen):
        """Draw a white circular outline for this asteroid on `screen`."""
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        """Advance the asteroid's position using its velocity.

        `dt` is the time delta in seconds and the velocity is assumed to be
        in units per second, so we multiply to get the position increment.
        """
        self.position += self.velocity * dt

    def split(self):
        """Destroy this asteroid and spawn two smaller ones if possible.

        - Calls `kill()` to remove the current asteroid.
        - If the asteroid is at or below `ASTEROID_MIN_RADIUS`, it will not
          split further.
        - Otherwise, logs the split event, picks a small random angle, and
          creates two new asteroids whose velocities are rotated away from
          the original and slightly boosted.
        """
        # Remove this asteroid from any groups / active lists
        self.kill()

        # Don't create children if already at minimum size
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        # Choose a split angle (degrees) and make two rotated velocity vectors
        angle = random.uniform(20, 50)
        new_vector_one = self.velocity.rotate(angle)
        new_vector_two = self.velocity.rotate(-angle)

        # Child asteroids are slightly smaller
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create the two new asteroids at the current location
        new_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)

        # Give the children their new velocities (slightly faster than parent)
        new_asteroid_one.velocity = new_vector_one * 1.2
        new_asteroid_two.velocity = new_vector_two * 1.2
