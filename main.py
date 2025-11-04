import pygame
import random
from config import window, HEIGH, WIDTH, font, deadSound, smashSound
from cursor import Cursor

#mouse
pygame.mouse.set_visible(False)
cursor = Cursor()

#load images/sounds/font
zombie = pygame.image.load("assets/images/zombie_head.png").convert_alpha()
zombie = pygame.transform.scale(zombie, (128, 128))
flashlight = pygame.image.load("assets/images/flashlight.png").convert_alpha()
flashlight = pygame.transform.scale(flashlight, (128, 128))
clock = pygame.time.Clock()

#set colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (67, 0, 144)
RED = (255, 0, 0)

#set circle and COORDINATE
CIRCLE_RADIUS = 100
CIRCLE_WIDTH = 3
COORDINATE = [(150,200),(400,200),(650,200),(150,450),(400,450),(650,450)]

#create spawn and remove event
SPAWN_EVENT = pygame.USEREVENT + 1
REMOVE_EVENT = pygame.USEREVENT + 2

def main():
    current_image = None
    current_pos = None
    
    HIT = 0
    MISS = 0

    pygame.time.set_timer(SPAWN_EVENT, 2000, 1)

    start_time = pygame.time.get_ticks()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            
            #pointer click
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("Clicked at:", event.pos)
                cursor.start()
                smashSound.play()
                if current_pos is not None:
                    if current_pos.collidepoint(event.pos):
                        HIT = HIT + 1
                        print(HIT)
                        current_image = flashlight
                        deadSound.play()
                        pygame.time.set_timer(REMOVE_EVENT, 100, loops=1)
                    else:
                        MISS = MISS + 1
                        print(MISS)
                        pygame.time.set_timer(REMOVE_EVENT, 100, loops=1)
                
            #handle spawn event
            if event.type == SPAWN_EVENT:
                current_pos = zombie.get_rect(center=(random.choice(COORDINATE)))
                current_image = zombie
                pygame.time.set_timer(REMOVE_EVENT, 1000, loops=1)

            #handle remove event
            if event.type == REMOVE_EVENT:
                current_image = None
                current_pos = None
                pygame.time.set_timer(SPAWN_EVENT, 2000, loops=1)
                
        cursor.update()
        
        #draw field
        window.fill(PURPLE)    
        for pos in COORDINATE:
            pygame.draw.circle(window,WHITE,pos,CIRCLE_RADIUS)
            pygame.draw.circle(window,BLACK,pos,CIRCLE_RADIUS,CIRCLE_WIDTH)
        
        #draw zombie    
        if current_image and current_pos:
            window.blit(current_image, current_pos)
        
        #draw scoreboard    
        SCORE = font.render(f"Hit: {HIT}  Miss: {MISS}", True, WHITE)
        window.blit(SCORE, (10, 10))
        
        #end game
        end_time = (pygame.time.get_ticks() - start_time) / 1000
        if end_time >= 30:
            pygame.draw.rect(window,WHITE,(100,200,600,200),border_radius = 5)
            pygame.draw.rect(window,BLACK,(100,200,600,200),3,border_radius = 5)
            game_over_text = font.render("Game Over!", True, RED)
            window.blit(game_over_text, (WIDTH // 2 - 100, HEIGH // 2 - 50))
            SCORES = font.render(f"SCORE: {max(HIT - MISS, 0)} ACCURATE: {int((HIT/(HIT + MISS))*100) if (HIT + MISS) > 0 else 0}%", True, BLACK)
            window.blit(SCORES, (WIDTH // 2 - 200, HEIGH // 2))
            pygame.display.flip()
        
        #draw timer
        time_left = max(0, int(30 - end_time))
        TIMER = font.render(f"Time Left: {time_left}s", True, WHITE)
        window.blit(TIMER, (WIDTH - 250, 10))

        cursor.draw()
        pygame.display.flip()
        clock.tick(60)
            
if __name__ == "__main__":
    main()