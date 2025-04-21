import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    
    def __init__(self, game: 'AlienInvasion'):
        
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):
        
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)
        x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, screen_w, fleet_w, fleet_h)

        self._create_triangle_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    def _create_triangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        
        triangle_base_width = 17  

        for row in range((triangle_base_width + 1) // 2):
            aliens_in_row = triangle_base_width - 2 * row
            total_width = aliens_in_row * alien_w
            start_x = (self.settings.screen_w - total_width) // 2

            for i in range(aliens_in_row):
                current_x = start_x + i * alien_w
                current_y = y_offset + row * alien_h
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        
        half_screen = self.settings.screen_h // 2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = (screen_w - fleet_horizontal_space) // 2
        y_offset = (half_screen - fleet_vertical_space) // 2
        return x_offset, y_offset

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        
        fleet_w = screen_w // alien_w
        fleet_h = (screen_h // 2) // alien_h

        fleet_w -= 1 if fleet_w % 2 == 0 else 2
        fleet_h -= 1 if fleet_h % 2 == 0 else 2

        return int(fleet_w), int(fleet_h)

    def _create_alien(self, current_x: int, current_y: int):
        
        new_alien = Alien(self, current_x, current_y)
        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed

    def update_fleet(self):
        
        self._check_fleet_edges()
        self.fleet.update()

    def draw(self):
        
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)

    def check_fleet_bottom(self):
        
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False

    def check_destroyed_status(self):
        
        return not self.fleet