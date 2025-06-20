from constants import *
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  
#Create groups
updatable = pygame.sprite.Group() # A group for updatable objects
drawable = pygame.sprite.Group() # A group for drawable objects
asteroids = pygame.sprite.Group() # A group for asteroids

# Set containers 
Player.containers = (updatable, drawable)
Asteroid.containers = (updatable, drawable, asteroids)
AsteroidField.containers = (updatable)  

# Create objects
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
asteroid_field = AsteroidField()

def main():
    asteroidfield = AsteroidField()  # Create an instance of the AsteroidField
    running = True  # Variable to control the main loop
    clock = pygame.time.Clock()  # Create a clock to manage frame rate
    dt = 0  # Initialize delta  time
    while True:
        # With this loop, we can handle events like quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
        if not running:
            break
        # Filling the screen with black
        screen.fill((0, 0, 0))
        # Update all updatables
        updatable.update(dt)
        # Draw all drawables
        for obj in drawable:
            obj.draw(screen) 
        pygame.display.flip() # Update the display
        dt = clock.tick(60) / 1000  # Limit the frame rate to 60 FPS

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # This block will catch the Ctrl+C interruption
        print("\nGame interrupted by user (Ctrl+C). Exiting gracefully.")
    finally:
        # This ensures pygame.quit() is called whether the game loop ends normally
        # or is interrupted by Ctrl+C.
        pygame.quit()