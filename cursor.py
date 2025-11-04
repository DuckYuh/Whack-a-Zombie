import pygame
from config import window

cursor_img = pygame.image.load("assets/images/HammerCursor.png").convert_alpha()
cursor_img = pygame.transform.scale(cursor_img, (48, 48))

class Cursor:
    def __init__(self):
        self.angle = 0
        self.phase = 0
        self.time = 0
        
    def update(self):
        now = pygame.time.get_ticks()
        if self.phase == 1:
            if now - self.time >= 100:
                self.angle = 0
                self.phase = 0
    
    def draw(self):
        rot = pygame.transform.rotate(cursor_img, self.angle)
        mx, my = pygame.mouse.get_pos()
        window.blit(rot, (mx, my))
        
    def start(self):
        self.angle = 90
        self.phase = 1
        self.time = pygame.time.get_ticks()