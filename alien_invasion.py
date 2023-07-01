import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall call to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop of the game"""
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # redraw screen during each pass through the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # make recently drawn scree visible
            pygame.display.flip()


if __name__ == "__main__":
    # make game instance and run game
    ai = AlienInvasion()
    ai.run_game()
