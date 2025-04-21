"""
alien.py

This module defines the Alien class for an alien sprite in the game.
Aliens are part of an AlienFleet and move across the screen, checking for
edge collisions and redrawing themselves.
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """
    Represents a single alien in the fleet.

    Attributes:
        fleet (AlienFleet): The fleet to which this alien belongs.
        screen (pygame.Surface): The game screen where the alien is rendered.
        boundaries (pygame.Rect): The screen boundaries for edge detection.
        settings (object): Game settings containing alien image, size, and speed.
        image (pygame.Surface): The alien's image.
        rect (pygame.Rect): The position and size of the alien sprite.
        x (float): Horizontal position of the alien (float for smooth movement).
        y (float): Vertical position of the alien.
    """

    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        """
        Initialize a new alien.

        Args:
            fleet (AlienFleet): The fleet managing this alien.
            x (float): Initial horizontal position.
            y (float): Initial vertical position.
        """
        super().__init__()

        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        self.image = pygame.image.load(str(self.settings.alien_file))
        self.image = pygame.transform.scale(self.image,
                (self.settings.alien_w, self.settings.alien_h)
                )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """
        Update the alien's position based on fleet direction and speed.
        """
        temp_speed = self.settings.fleet_speed
        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self) -> bool:
        """
        Check if the alien has hit the edge of the screen.

        Returns:
            bool: True if the alien has reached the screen's edge, False otherwise.
        """
        return (self.rect.right >= self.boundaries.right or
                self.rect.left <= self.boundaries.left)

    def draw_alien(self):
        """
        Draw the alien at its current location on the screen.
        """
        self.screen.blit(self.image, self.rect)
