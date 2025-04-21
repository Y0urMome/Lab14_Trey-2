"""
bullet.py

This module defines the Bullet class for managing projectile sprites fired by the player's ship.
Bullets move vertically upward and are rendered on the screen each frame until removed.
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """
    A class representing a bullet fired by the player's ship.

    Attributes:
        screen (pygame.Surface): The game screen to draw the bullet on.
        settings (object): Game settings object with bullet parameters.
        image (pygame.Surface): The bullet image.
        rect (pygame.Rect): The position and size of the bullet.
        y (float): The bullet's vertical position for smooth motion.
    """

    def __init__(self, game: 'AlienInvasion'):
        """
        Initialize the bullet at the ship's current top center position.

        Args:
            game (AlienInvasion): The main game instance providing context and settings.
        """
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(str(self.settings.bullet_file))
        self.image = pygame.transform.scale(
            self.image, (self.settings.bullet_w, self.settings.bullet_h)
        )
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """
        Update the bullet's position by moving it upward.
        """
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """
        Draw the bullet on the screen at its current position.
        """
        self.screen.blit(self.image, self.rect)
