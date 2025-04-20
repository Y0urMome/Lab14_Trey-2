from pathlib import Path

class Settings:
    
    def __init__(self):
        self.name: str = 'Alien Invasion'
        self.screen_w  = 1265
        self.screen_h  = 625
        self.FPS       = 60
        self.bg_file   = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'
        self.difficulty_scale = 1.1
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        self.ship_file  = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w     = 30
        self.ship_h     = 50
        

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'
        
        
        

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        
        self.alien_w = 30
        self.alien_h = 30
        self.fleet_direction = 1
        

        self.button_w = 200
        self.button_h = 50
        self.button_color = (0,0,250)

        self.text_color = (255,255,255)
        self.button_font_size = 40
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'

    def initialize__dynamic_settings(self):
        self.ship_speed = 7
        self.starting_ship_count = 3

        self.bullet_speed = 10
        self.bullet_w = 20
        self.bullet_h = 50
        self.bullet_amount = 5

        self.fleet_speed = 1
        self.fleet_drop_speed = 30
        self.alien_points = 50

    def increase_difficulty(self):
        self.ship_speed += self.difficulty_scale
        self.bullet_speed += self.difficulty_scale
        self.fleet_speed += self.difficulty_scale