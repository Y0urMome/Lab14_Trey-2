"""
arsenal.py

This module defines the Arsenal class, which manages a group of bullets fired
by the player. It handles bullet creation, updating, rendering, and cleanup
when bullets go off-screen.
"""

import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    """
    A class to manage the player's arsenal of bullets.

    Attributes:
        game (AlienInvasion): Reference to the main game instance.
        settings (object): Game settings object.
        arsenal (pygame.sprite.Group): Group of active bullet sprites.
    """

    def __init__(self, game: 'AlienInvasion'):
        """
        Initialize the arsenal.

        Args:
            game (AlienInvasion): The main game instance.
        """
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """
        Update all bullets in the arsenal and remove any off-screen bullets.
        """
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """
        Remove bullets that have moved off the top of the screen.
        """
        for bullet in self.arsenal.copy():
            if bullet.rect.bottom <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        """
        Draw all bullets in the arsenal on the screen.
        """
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self) -> bool:
        """
        Fire a new bullet if the maximum number hasn't been reached.

        Returns:
            bool: True if a bullet was fired, False otherwise.
        """
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False
