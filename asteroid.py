from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        
    def draw(self, screen):
        pygame.draw.circle(
        screen,
        (255, 255, 255),
        (int(self.position.x), int(self.position.y)),
        int(self.radius),
        2
    )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        v1 = self.velocity.rotate(angle) * 1.2
        v2 = self.velocity.rotate(-angle) * 1.2
        Asteroid(self.position.x, self.position.y, new_radius).velocity = v1
        Asteroid(self.position.x, self.position.y, new_radius).velocity = v2

    
class Shot(CircleShape):
    def __init__(self, x, y, radius, velocity):
        super().__init__(x, y, radius)
        self.velocity = velocity
        
    def draw(self, screen):
        pygame.draw.circle(
        screen,
        (255, 255, 255),
        (int(self.position.x), int(self.position.y)),
        int(self.radius),
        2
    )
    def update(self, dt):
        self.position += self.velocity * dt