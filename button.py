"""
button.py

This module defines the Button class used in the game's UI for starting or restarting
the game. The button displays a message and responds to mouse click interactions.
"""

import pygame.font
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Button:
    """
    A class representing a clickable button with a text label.

    Attributes:
        game (AlienInvasion): The main game instance.
        screen (pygame.Surface): The display surface where the button is drawn.
        boundaires (pygame.Rect): The screen boundaries used for centering.
        settings (object): The game's settings.
        font (pygame.font.Font): Font object for rendering button text.
        rect (pygame.Rect): The button’s rectangular area.
        msg_image (pygame.Surface): Rendered image of the button’s text.
        msg_image_rect (pygame.Rect): Rect of the rendered text image.
    """

    def __init__(self, game: 'AlienInvasion', msg):
        """
        Initialize the button with a message.

        Args:
            game (AlienInvasion): The main game instance.
            msg (str): The message text to be displayed on the button.
        """
        self.game = game
        self.screen = game.screen
        self.boundaires = game.screen.get_rect()
        self.settings = game.settings
        self.font = pygame.font.Font(self.settings.font_file,
                                     self.settings.button_font_size)

        self.rect = pygame.Rect(0, 0, self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaires.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """
        Render the button's text message and center it on the button.

        Args:
            msg (str): The message text to render.
        """
        self.msg_image = self.font.render(msg, True, self.settings.text_color, None)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self):
        """
        Draw the button with the text label onto the screen.
        """
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_clicked(self, mouse_pos) -> bool:
        """
        Check if the given mouse position is within the button’s area.

        Args:
            mouse_pos (Tuple[int, int]): The (x, y) position of the mouse click.

        Returns:
            bool: True if the button was clicked, False otherwise.
        """
        return self.rect.collidepoint(mouse_pos)
