"""
alien_fleet.py

This module defines the AlienFleet class, which manages a group of Alien
instances in a triangular formation. The fleet handles creation, movement,
collision detection, edge checking, and rendering.
"""

import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    """
    Manages a fleet of alien sprites in a triangular layout.

    Attributes:
        game (AlienInvasion): The main game instance.
        settings (object): Game settings including screen and fleet configuration.
        fleet (pygame.sprite.Group): Group of all alien sprites.
        fleet_direction (int): Direction the fleet is currently moving.
        fleet_drop_speed (int): Distance to drop when the fleet hits the edge.
    """

    def __init__(self, game: 'AlienInvasion'):
        """
        Initialize the alien fleet.

        Args:
            game (AlienInvasion): The game instance managing settings and screen.
        """
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):
        """
        Calculate dimensions and initialize a triangular alien fleet formation.
        """
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)
        x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, screen_w, fleet_w, fleet_h)

        self._create_triangle_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    def _create_triangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        """
        Create a triangle-shaped formation of aliens.

        Args:
            alien_w (int): Width of each alien.
            alien_h (int): Height of each alien.
            fleet_w (int): Number of aliens in a row at the widest point.
            fleet_h (int): Number of rows.
            x_offset (int): Horizontal margin offset.
            y_offset (int): Vertical margin offset.
        """
        triangle_base_width = 17  # Maximum aliens in bottom row

        for row in range((triangle_base_width + 1) // 2):
            aliens_in_row = triangle_base_width - 2 * row
            total_width = aliens_in_row * alien_w
            start_x = (self.settings.screen_w - total_width) // 2

            for i in range(aliens_in_row):
                current_x = start_x + i * alien_w
                current_y = y_offset + row * alien_h
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        """
        Calculate horizontal and vertical offsets for centering the fleet.

        Args:
            alien_w (int): Alien width.
            alien_h (int): Alien height.
            screen_w (int): Screen width.
            fleet_w (int): Fleet width in aliens.
            fleet_h (int): Fleet height in rows.

        Returns:
            Tuple[int, int]: x_offset and y_offset
        """
        half_screen = self.settings.screen_h // 2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = (screen_w - fleet_horizontal_space) // 2
        y_offset = (half_screen - fleet_vertical_space) // 2
        return x_offset, y_offset

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        """
        Calculate the number of aliens that can fit on screen.

        Args:
            alien_w (int): Width of an alien.
            screen_w (int): Width of the screen.
            alien_h (int): Height of an alien.
            screen_h (int): Height of the screen.

        Returns:
            Tuple[int, int]: Number of aliens horizontally and vertically.
        """
        fleet_w = screen_w // alien_w
        fleet_h = (screen_h // 2) // alien_h

        fleet_w -= 1 if fleet_w % 2 == 0 else 2
        fleet_h -= 1 if fleet_h % 2 == 0 else 2

        return int(fleet_w), int(fleet_h)

    def _create_alien(self, current_x: int, current_y: int):
        """
        Create a single alien and add it to the fleet.

        Args:
            current_x (int): X-position for the alien.
            current_y (int): Y-position for the alien.
        """
        new_alien = Alien(self, current_x, current_y)
        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        """
        Check if any aliens hit the screen edge and reverse direction if so.
        """
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        """
        Drop the entire fleet downward when hitting the screen edge.
        """
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed

    def update_fleet(self):
        """
        Update fleet position and check for edge collisions.
        """
        self._check_fleet_edges()
        self.fleet.update()

    def draw(self):
        """
        Draw all aliens in the fleet to the screen.
        """
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        """
        Detect and process collisions with another sprite group.

        Args:
            other_group (pygame.sprite.Group): The group to check collisions against.

        Returns:
            dict: Dictionary of collided sprites.
        """
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)

    def check_fleet_bottom(self) -> bool:
        """
        Check if any alien has reached the bottom of the screen.

        Returns:
            bool: True if any alien touches the bottom; False otherwise.
        """
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False

    def check_destroyed_status(self) -> bool:
        """
        Check if the entire fleet has been destroyed.

        Returns:
            bool: True if fleet is empty; False otherwise.
        """
        return not self.fleet
