"""shot.py

Simple projectile logic for player-fired shots.

`Shot` is a small circular object with position and velocity; it moves in a
straight line and is drawn as a filled white circle.
"""

import pygame
from circleshape import CircleShape


class Shot(CircleShape):
    """Small projectile fired by the player."""

    def __init__(self, x, y, radius):
        """Create a shot at (x, y) with given radius."""
        super().__init__(x, y, radius)

    def draw(self, screen):
        """Render the shot as a white filled circle."""
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        """Advance the shot position by velocity * dt (straight-line motion)."""
        self.position += self.velocity * dt
