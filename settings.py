from pathlib import Path

class Settings:
    
    def __init__(self):
        self.name: str = 'Alien Invasion'
        self.screen_w  = 1265
        self.screen_h  = 625
        self.FPS       = 60
        self.bg_file   = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        self.ship_file  = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w     = 30
        self.ship_h     = 50
        self.ship_speed = 7

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed = 10
        self.bullet_w = 20
        self.bullet_h = 50
        self.bullet_amount = 5

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.fleet_speed = 5
        self.alien_w = 30
        self.alien_h = 30
        self.fleet_direction = 1
        self.fleet_drop_speed = 30