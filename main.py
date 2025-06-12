from constants import *
import pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
def main():
    while True:
        # With this loop, we can handle events like quitting the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        # Here you would typically update game state and draw everything
        # For now, we will just fill the screen with black
        screen.fill((0, 0, 0))  # Fill the screen with black
        pygame.display.flip() # Update the display



if __name__ == "__main__":
    main()