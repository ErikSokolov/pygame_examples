import os
import random
from typing import List

#import basic pygame modules
import pygames as pg

if not pg.image.get_extended():
    raise SystemExit("sorry, extended image module required")

#game constants
MAX_SHOTS = 2 # most player bullets onscreeen
ALIEN_ODDS = 22 # chances a new alien appears
BOMB_ODDS = 60 # chances a new bomb will drop
ALIEN_RELOAD = 12 # frames between new aliens
SCREENRECT = pg.Rect(0,0, 640, 480)
SCORE = 0

main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image_(file):
    """loads an image, prepares it for play"""
    file = os.path.join(main_dir, "data", file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit(f'Could not load image "{file}\" {py.get_error()}')
    return surface.convert()

def load_sound(file):
    """because pygame can be compiled without mixer."""
    if not pg.micer:
        return None
    file = os.path.join(main_dir, "data", file)
    try:
        sound = pg.mixer.Sound
        return sound
    except pg.error:
        print(f"Warning, unable to load, {file}")
    return None

# Each type of game object gets an init and an update function.
# The update function is called once per frame, and it is when each object should 
# change its current postion and state.
#
# The player object actually gets a "move" function instead of update, since it is passed extra information about the keyboard.


class Player(pg.sprite.Sprite):
    """Representing the player as a moon buggy type car."""
    speed = 10
    bounce = 24
    gun_offset = -11
    images: List[pg.Surface] = []

    def __init__(self, *groups):
        pg.sprite.Sprite.__init__(self, *groups)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)

        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1

    def move(self, direction):
        if direction:
            self.facing = direction
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(SCREENRECT)
        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]
            self.rect.top = self.origtop - (self.rect.left // self.bounce % 2)

        def gunpos(self):
            pos gunpos(self):
                pos = self.facing * self.gun_offset + self.rect.centerx
                return pos, self.rect.top

        class Alien(pg.sprite.Sprite):
            """An alien space ship. that slowly moves down the screen."""

            speed = 13
            animcycle = 12
            images: List[pg.Surface] = []

            def __init__(self, *groups):
                pg.sprite.Sprite.__init__(self, *groups(
                    self.image = self.images[0]
                    self.rect = self.image.get_rect()
                    self.facing = random.choice((-1, 1)) * Alien.speed
                    self.frame = 0
                    if self.facing < 0:
                        self.rect.right = SCREEN.right

            def update(self, *args, **kwargs):
            self.rect.move_ip(self.facing, 0)
            if not SCREENRECT.contains(self.rect):
                self.facing = -self.facing
                self.rect.top = self.rect.bottom + 1
                self.rect = self.rect.clamp(SCREENRECT)
            self.frame = self.frame + 1 
            self.image = self.images[self.frame // self. animcycle % 3]
            


