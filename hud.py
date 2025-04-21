"""
hud.py

This module defines the HUD (Heads-Up Display) class responsible for rendering
game statistics such as score, high score, max score, level, and remaining lives
on the screen during gameplay.
"""

import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class HUD:
    """
    A class to manage and draw the heads-up display (HUD) elements on the screen.

    Attributes:
        game (AlienInvasion): The main game instance.
        settings (object): Game settings including text size, colors, etc.
        screen (pygame.Surface): The main game screen.
        boundaires (pygame.Rect): The screen boundary for layout reference.
        game_stats (GameStats): Tracks current game statistics.
        font (pygame.font.Font): Font used for rendering text.
        padding (int): Padding between HUD elements.
    """

    def __init__(self, game: 'AlienInvasion'):
        """
        Initialize the HUD and prepare all display elements.

        Args:
            game (AlienInvasion): The main game instance.
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaires = game.screen.get_rect()
        self.game_stats = game.game_stats
        self.font = pygame.font.Font(self.settings.font_file,
                                     self.settings.HUD_font_size)
        self.padding = 20
        self.update_scores()
        self._setup_life_image()
        self.update_level()

    def _setup_life_image(self):
        """
        Load and scale the ship image to be used for representing lives.
        """
        self.life_image = pygame.image.load(self.settings.ship_file)
        self.life_image = pygame.transform.scale(
            self.life_image, (self.settings.ship_w, self.settings.ship_h)
        )
        self.life_rect = self.life_image.get_rect()

    def update_scores(self):
        """
        Update all score-related text elements: max score, current score, and high score.
        """
        self._update_max_score()
        self._update_score()
        self._update_hi_score()

    def _update_score(self):
        """
        Render and position the current score text.
        """
        score_str = f'Score: {self.game_stats.score: ,.0f}'
        self.score_image = self.font.render(score_str, True, self.settings.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaires.right - self.padding
        self.score_rect.top = self.max_score_rect.bottom + self.padding

    def _update_max_score(self):
        """
        Render and position the max score text.
        """
        max_score_str = f'MAX SCORE: {self.game_stats.max_score: ,.0f}'
        self.max_score_image = self.font.render(max_score_str, True, self.settings.text_color, None)
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaires.right - self.padding
        self.max_score_rect.top = self.padding

    def _update_hi_score(self):
        """
        Render and center the high score text at the top of the screen.
        """
        hi_score_str = f'HI-SCORE: {self.game_stats.hi_score: ,.0f}'
        self.hi_score_image = self.font.render(hi_score_str, True, self.settings.text_color, None)
        self.hi_score_rect = self.hi_score_image.get_rect()
        self.hi_score_rect.midtop = (self.boundaires.centerx, self.padding)

    def update_level(self):
        """
        Render and position the current level text on the screen.
        """
        level_str = f'LEVEL: {self.game_stats.level: ,.0f}'
        self.level_image = self.font.render(level_str, True, self.settings.text_color, None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.top = self.life_rect.bottom + self.padding

    def _draw_lives(self):
        """
        Draw icons for the remaining ships (lives) on the screen.
        """
        current_x = self.padding
        current_y = self.padding
        for _ in range(self.game_stats.ships_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x += self.life_rect.width + self.padding

    def draw(self):
        """
        Draw all HUD elements to the screen: scores, level, and lives.
        """
        self.screen.blit(self.hi_score_image, self.hi_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self._draw_lives()
