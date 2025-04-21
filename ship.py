"""
ship.py

This module defines the Ship class, which manages the player's ship in the Alien Invasion game.
It handles rendering, movement, collision detection, and bullet firing using an Arsenal instance.
"""

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    """
    A class representing the player's ship.

    Attributes:
        game (AlienInvasion): The main game instance.
        settings (object): Game settings.
        screen (pygame.Surface): Game display surface.
        boundaries (pygame.Rect): Screen boundaries for movement limits.
        image (pygame.Surface): The ship sprite image.
        rect (pygame.Rect): The position and size of the ship.
        x (float): Floating-point x position for smooth movement.
        moving_right (bool): Whether the ship is moving right.
        moving_left (bool): Whether the ship is moving left.
        arsenal (Arsenal): Object managing bullets fired by the ship.
    """

    def __init__(self, game: 'AlienInvasion', arsenal: "Arsenal"):
        """
        Initialize the Ship object.

        Args:
            game (AlienInvasion): The main game instance.
            arsenal (Arsenal): The ship's bullet manager.
        """
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.ship_w, self.settings.ship_h)
        )

        self.rect = self.image.get_rect()
        self._center_ship()
        self.moving_right = False
        self.moving_left = False
        self.arsenal = arsenal

    def _center_ship(self):
        """
        Center the ship at the bottom of the screen and reset its horizontal position.
        """
        self.rect.midbottom = self.boundaries.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """
        Update the ship’s position and update all bullets in its arsenal.
        """
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """
        Adjust the ship's horizontal position based on movement flags.
        """
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.x = self.x

    def draw(self):
        """
        Draw the ship and all active bullets to the screen.
        """
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self) -> bool:
        """
        Fire a bullet using the ship's arsenal.

        Returns:
            bool: True if a bullet was successfully fired, False if the limit is reached.
        """
        return self.arsenal.fire_bullet()

    def check_collisions(self, other_group) -> bool:
        """
        Check for collisions between the ship and another sprite group (e.g., alien fleet).

        Args:
            other_group (pygame.sprite.Group): The group to check collisions against.

        Returns:
            bool: True if a collision occurred and ship was recentered, False otherwise.
        """
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False
