"""circleshape.py

Lightweight base for circular game objects used by the game.

Provides `position`, `velocity`, and `radius` fields and a simple
circle-vs-circle collision helper. Subclasses should override `draw`
and `update` to implement rendering and per-frame behavior.
"""

import pygame


class CircleShape(pygame.sprite.Sprite):
    """Base class for circular sprites.

    Subclasses should override `draw` and `update`. Position and velocity are
    stored as `pygame.Vector2` instances, and `radius` is used for collision
    checks.
    """

    def __init__(self, x, y, radius):
        """Initialize position, a zero velocity vector, and the radius.

        If `containers` is defined on the class (set from `main.py`), the
        sprite constructor will add this instance to those groups.
        """
        # Add to any pre-configured sprite groups if present
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        """Draw this object onto `screen`. Must be implemented by subclasses."""
        pass

    def update(self, dt):
        """Update the object's state. `dt` is the frame time in seconds."""
        pass

    def collides_with(self, other):
        """Return True if this circle intersects `other` circle.

        Collision is detected by comparing the distance between centers to the
        sum of radii.
        """
        distance = (self.position - other.position).length()
        r1 = self.radius
        r2 = other.radius
        if distance <= r1 + r2:
            return True
        return False
