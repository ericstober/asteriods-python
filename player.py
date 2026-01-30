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
    ## Represents the player-controlled ship in the Asteriods game.

    def __init__(self, x, y):
        # Initialize the base CircleShape with a position and radius
        super().__init__(x, y, PLAYER_RADIUS)

        # Current rotation angle of the player
        self.rotation = 0

        # Create shot cooldown timer
        self.shot_cooldown_timer = 0

    def triangle(self):
        ## Calculates the three points of the triangular ship shape based on the player's position and rotation.

        # Forward direction vector (rotated to match player orientation)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)

        # Right direction vector, used to give the triangle its width
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5

        # Front point of the ship
        a = self.position + forward * self.radius

        # Back-left point of the ship
        b = self.position - forward * self.radius - right

        # Back-right point of the ship
        c = self.position - forward * self.radius + right

        # Return the three points as a list
        return [a, b, c]

    def draw(self, screen):
        ## Draws the player ship as a white outlined triangle.
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        ## Rotates the player ship dt (delta time) ensures rotation speed is frame-rate independent.
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        ## Handles player input and updates movement/rotation each frame.
        keys = pygame.key.get_pressed()

        # Move forward
        if keys[pygame.K_w]:
            self.move(dt)

        # Move backward
        if keys[pygame.K_s]:
            self.move(-dt)

        # Rotate left
        if keys[pygame.K_a]:
            self.rotate(-dt)

        # Rotate right
        if keys[pygame.K_d]:
            self.rotate(dt)

        # Shoot
        if keys[pygame.K_SPACE]:
            if self.shot_cooldown_timer > 0:
                return
            else:
                self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
                self.shoot()

        # Decrease the shoot timer
        self.shot_cooldown_timer -= dt

    def move(self, dt):
        ## Moves the player in the direction it is currently facing.

        # Base forward unit vector
        unit_vector = pygame.Vector2(0, 1)

        # Rotate vector to match player orientation
        rotated_vector = unit_vector.rotate(self.rotation)

        # Apply movement speed and delta time
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt

        # Update player position
        self.position += rotated_with_speed_vector

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        return shot
