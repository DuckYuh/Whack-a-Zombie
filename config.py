import pygame

pygame.init()
pygame.mixer.init()
pygame.font.init()

WIDTH = 800
HEIGH = 600

window = pygame.display.set_mode((WIDTH,HEIGH))

font = pygame.font.SysFont(None, 48)

#set icon and caption
icon = pygame.image.load("assets/images/big-zombie-face.png")
pygame.display.set_caption("Super Zombies Smash")
pygame.display.set_icon(icon)

smashSound = pygame.mixer.Sound("assets/sounds/smash.mp3")
deadSound = pygame.mixer.Sound("assets/sounds/Zombie_death.ogg")

#set sound
pygame.mixer.music.load("assets/sounds/background.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
smashSound.set_volume(0.3)
deadSound.set_volume(0.2)