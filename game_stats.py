"""
game_stats.py

This module defines the GameStats class, which tracks and manages the player's
score, level, lives, and high scores throughout the game session. It handles
saving/loading persistent high scores using a JSON file.
"""

import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats:
    """
    Track statistics for Alien Invasion, including current score, high score,
    remaining ships, and current level. Also manages persistent score storage.

    Attributes:
        game (AlienInvasion): The main game instance.
        settings (object): Game settings object.
        max_score (int): Maximum score in the current session.
        hi_score (int): All-time highest score loaded from file.
        ships_left (int): Number of remaining ships.
        score (int): Current score in the session.
        level (int): Current level of the game.
        path (Path): Path to the saved score file.
    """

    def __init__(self, game: 'AlienInvasion'):
        """
        Initialize game statistics and load saved scores if available.

        Args:
            game (AlienInvasion): The main game instance.
        """
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self):
        """
        Load the high score from a file if it exists and is valid.
        Otherwise, initialize the file with a score of 0.
        """
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.__sizeof__() > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()

    def save_scores(self):
        """
        Save the current high score to the designated file.
        """
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')

    def reset_stats(self):
        """
        Reset statistics for a new game session.
        """
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions):
        """
        Update the score based on collisions, and update max/hi scores.

        Args:
            collisions (dict): Dictionary of sprite groups representing hits.
        """
        self._update_score(collisions)
        self._update_max_score()
        self._update_hi_score()

    def _update_score(self, collisions):
        """
        Increment score based on the number of alien collisions.

        Args:
            collisions (dict): The collision result from sprite groups.
        """
        for alien in collisions.values():
            self.score += self.settings.alien_points

    def _update_max_score(self):
        """
        Update the session's maximum score if the current score exceeds it.
        """
        if self.score > self.max_score:
            self.max_score = self.score

    def _update_hi_score(self):
        """
        Update the persistent high score if the current score exceeds it.
        """
        if self.score > self.hi_score:
            self.hi_score = self.score

    def update_level(self):
        """
        Increment the current game level.
        """
        self.level += 1
        print(self.level)
