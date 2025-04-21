"""
settings.py

This module defines the Settings class, which stores all configurable properties
for the Alien Invasion game, including screen dimensions, asset paths, speeds,
sizes, sounds, UI styles, and difficulty scaling logic.
"""

from pathlib import Path

class Settings:
    """
    A class to store and manage all settings for the Alien Invasion game.

    Attributes:
        name (str): The name of the game window.
        screen_w (int): Screen width in pixels.
        screen_h (int): Screen height in pixels.
        FPS (int): Frames per second (frame rate).
        bg_file (Path): File path to the background image.
        difficulty_scale (float): Multiplier to increase difficulty over time.
        scores_file (Path): File path to the saved scores JSON file.

        ship_file (Path): File path to the ship image.
        ship_w (int): Ship width.
        ship_h (int): Ship height.

        bullet_file (Path): File path to the bullet image.
        laser_sound (Path): File path to the laser sound.
        impact_sound (Path): File path to the impact sound.

        alien_file (Path): File path to the alien image.
        alien_w (int): Alien width.
        alien_h (int): Alien height.
        fleet_direction (int): Initial direction of alien fleet movement.

        button_w (int): Button width.
        button_h (int): Button height.
        button_color (tuple): RGB color of the button.
        text_color (tuple): RGB color of the text.
        button_font_size (int): Font size for button text.
        HUD_font_size (int): Font size for HUD text.
        font_file (Path): File path to the font used in HUD and UI.

    Dynamic Settings (set in `initialize__dynamic_settings`):
        ship_speed (float): Speed of the player's ship.
        starting_ship_count (int): Number of lives the player starts with.
        bullet_speed (float): Speed at which bullets travel.
        bullet_w (int): Width of a bullet.
        bullet_h (int): Height of a bullet.
        bullet_amount (int): Maximum number of bullets allowed on screen.
        fleet_speed (float): Speed of the alien fleet.
        fleet_drop_speed (int): Distance aliens drop down when changing direction.
        alien_points (int): Points awarded per alien destroyed.
    """

    def __init__(self):
        """
        Initialize static settings for the game.
        """
        self.name: str = 'Alien Invasion'
        self.screen_w = 1265
        self.screen_h = 625
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'mybackground.png'
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'myship.png'
        self.ship_w = 30
        self.ship_h = 50

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'mybeam.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser6.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'mechanical_explosion.mp3'

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'myalien.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_direction = 1

        self.button_w = 200
        self.button_h = 50
        self.button_color = (0, 0, 250)

        self.text_color = (255, 255, 255)
        self.button_font_size = 40
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'MajorMonoDisplay-Regular.ttf'

    def initialize__dynamic_settings(self):
        """
        Initialize settings that change throughout the game and reset when restarting.
        """
        self.ship_speed = 7
        self.starting_ship_count = 3

        self.bullet_speed = 10
        self.bullet_w = 30
        self.bullet_h = 60
        self.bullet_amount = 5

        self.fleet_speed = 1
        self.fleet_drop_speed = 40
        self.alien_points = 100

    def increase_difficulty(self):
        """
        Increase game difficulty by scaling speeds and adjusting sizes.
        """
        self.ship_speed += self.difficulty_scale
        self.bullet_speed += self.difficulty_scale
        self.bullet_w += self.difficulty_scale
        self.bullet_w += self.difficulty_scale
        self.fleet_speed += self.difficulty_scale
        self.alien_w -= self.difficulty_scale
        self.alien_h -= self.difficulty_scale
