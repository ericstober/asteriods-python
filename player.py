"""player.py

Controls the player-controlled triangular ship.

The `Player` class handles input, movement, rotation, shooting (with a
cooldown), and provides a helper to compute the triangle points used for
rendering the ship.
"""

import pygame
from circleshape import CircleShape
from shot import Shot
from constants import (
    PLAYER_RADIUS,
    PLAYER_SHOOT_SPEED,
    SHOT_RADIUS,
    LINE_WIDTH,
    PLAYER_TURN_SPEED,
    PLAYER_SPEED,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
)


class Player(CircleShape):
    """Player-controlled triangular ship.

    - `rotation` is the current facing angle in degrees.
    - `shot_cooldown_timer` prevents shooting until it reaches zero.
    """

    def __init__(self, x, y):
        """Create a player at (x, y) with configured radius and initial state."""
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0

    def triangle(self):
        """Return three points (Vector2) forming the triangular ship polygon.

        Uses the player's `position`, `rotation`, and `radius` to compute the
        front and rear vertices so the ship renders as a pointing triangle.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]

    def draw(self, screen):
        """Draw the ship as a white outlined triangle on `screen`."""
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        """Rotate the ship by `PLAYER_TURN_SPEED * dt` degrees."""
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        """Handle input each frame and update movement/rotation/shooting state.

        - Uses WASD for movement/rotation and SPACE to shoot.
        - Enforces a cooldown between shots using `shot_cooldown_timer`.
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        # Shooting with cooldown
        if keys[pygame.K_SPACE]:
            if self.shot_cooldown_timer <= 0:
                self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
                self.shoot()

        # Decrease the shoot timer each frame
        self.shot_cooldown_timer -= dt

    def move(self, dt):
        """Move the player forward (or backward if dt < 0) based on rotation."""
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        self.position += rotated_vector * PLAYER_SPEED * dt

    def shoot(self):
        """Spawn and return a `Shot` moving in the player's current direction."""
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        return shot
