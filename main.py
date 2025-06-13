from constants import *
import pygame
from player import Playerls

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Create a player instance
def main():
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
        # Here you would typically update game state and draw everything
        # For now, we will just fill the screen with black
        screen.fill((0, 0, 0))
        player.draw(screen)  # Fill the screen with black
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