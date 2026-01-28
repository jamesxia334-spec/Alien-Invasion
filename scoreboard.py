import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.clock = pygame.time.Clock()

        # Font settings for scoring information.
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.small_font = pygame.font.SysFont(None, 32)

        self.prep_images()



    def prep_images(self):
        """Prepare all of the initial score images."""
        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()

        self.prep_level()
        self.prep_ships()



    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20


    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)
        name = getattr(self.stats, "high_score_name", "someone").strip()

        high_score_str = "High Score: " + f"{high_score:,}" + f" ({name})"

        self.high_score_image = self.font.render(
            high_score_str, True,
            self.text_color, self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = "Lv." + str(self.stats.level)

        self.level_image = self.font.render(
            level_str, True,
            self.text_color, self.settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.stats.high_score_name = ''
            self.prep_high_score()


    def show_score(self):
        """Draw scores, level, and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)



    def prompt_high_score_name(self):
        """Ask the player to enter a name in-game and return it as a string."""

        name = ""
        entering = True

        # Show mouse cursor for better user experience
        pygame.mouse.set_visible(True)

        while entering:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Player closed the window directly
                    entering = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Confirm input
                        entering = False
                    elif event.key == pygame.K_ESCAPE:
                        # Cancel input
                        name = ""
                        entering = False
                    elif event.key == pygame.K_BACKSPACE:
                        # Remove last character
                        name = name[:-1]
                    else:
                        # Accept printable characters only and limit input length
                        if event.unicode.isprintable() and len(name) < 20:
                            name += event.unicode
            self._draw_input_screen(name)
            self.clock.tick(60)

        return name.strip()
    
    def _draw_input_screen(self, name):
        """ Draw the input screen."""
        self.screen.fill(self.settings.bg_color)

        title = self.font.render(
            "New High Score!", True, (30, 30, 30), self.settings.bg_color
        )
        tip = self.small_font.render(
            "Enter your name (Enter=OK, Esc=Skip):",
            True, (30, 30, 30), self.settings.bg_color
        )

        # Blinking cursor effect
        cursor = "_" if (pygame.time.get_ticks() // 400) % 2 == 0 else ""
        shown = name + cursor
        text = self.font.render(
            shown, True, (30, 30, 30), self.settings.bg_color
        )

        title_rect = title.get_rect(
            center=(self.settings.screen_width // 2,
                    self.settings.screen_height // 2 - 120)
        )
        tip_rect = tip.get_rect(
            center=(self.settings.screen_width // 2,
                    self.settings.screen_height // 2 - 60)
        )
        text_rect = text.get_rect(
            center=(self.settings.screen_width // 2,
                    self.settings.screen_height // 2 + 10)
        )

        self.screen.blit(title, title_rect)
        self.screen.blit(tip, tip_rect)
        self.screen.blit(text, text_rect)

        pygame.display.flip()


