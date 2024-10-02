import pygame
import random

import pygame.draw

pygame.init()

screen = pygame.display.set_mode([800, 1000])
running = True

playerX = 375
playerY = 200



enemyX1 = random.randrange(30,148)
enemyX2 = random.randrange(148,296)
enemyX3 = random.randrange(296,444)
enemyX4 = random.randrange(444,592)
enemyX5 = random.randrange(592,740)

enemyY = 1000



clock = pygame.time.Clock()
fps = 120
more = False

nums = ["three","four","five"]
CurEnemies = random.choice(nums)

while running:
    
    

    clock.tick(fps)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if playerY > 0:
        if pressed[pygame.K_w]: playerY -= 3
    if playerY < 1000 - 25:
        if pressed[pygame.K_s]: playerY += 3
    if playerX > 0:
        if pressed[pygame.K_a]: playerX -= 3
    if playerX < 800 - 25:
        if pressed[pygame.K_d]: playerX += 3
    
    screen.fill((255, 255, 255))
    player = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(playerX, playerY, 25, 25))

    enemyY -=1
    
    
    """

    if enemyY1 == -50:

        enemyY1 = 1000
        enemyX1 = random.randrange(730)
        more = True
        print(more)

    if more == True:
        pygame.draw.rect(screen, (0,0,0), enemy2)
        enemyY2 -=1
   """
        
    

    if CurEnemies == "three":
        enemy1 = pygame.draw.rect(screen, (0,0,255), pygame.Rect(enemyX1, enemyY, 50, 50))
        enemy2 = pygame.draw.rect(screen, (255,0,0), pygame.Rect(enemyX2, enemyY, 50, 50))
        enemy3 = pygame.draw.rect(screen, (0,255,0), pygame.Rect(enemyX3, enemyY, 50, 50))

    elif CurEnemies == "four":

        enemy1 = pygame.draw.rect(screen, (0,0,255), pygame.Rect(enemyX1, enemyY, 50, 50))
        enemy2 = pygame.draw.rect(screen, (255,0,0), pygame.Rect(enemyX2, enemyY, 50, 50))
        enemy3 = pygame.draw.rect(screen, (0,255,0), pygame.Rect(enemyX3, enemyY, 50, 50))
        enemy4 = pygame.draw.rect(screen, (255,192,203), pygame.Rect(enemyX4, enemyY, 50, 50))
        
    elif CurEnemies == "five":

        enemy1 = pygame.draw.rect(screen, (0,0,255), pygame.Rect(enemyX1, enemyY, 50, 50))
        enemy2 = pygame.draw.rect(screen, (255,0,0), pygame.Rect(enemyX2, enemyY, 50, 50))
        enemy3 = pygame.draw.rect(screen, (0,255,0), pygame.Rect(enemyX3, enemyY, 50, 50))
        enemy4 = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(enemyX4, enemyY, 50, 50))
        enemy5 = pygame.draw.rect(screen, (255,192,203), pygame.Rect(enemyX5, enemyY, 50, 50))

    if enemyY == -50:
        enemyY = 1000
        enemyX1 = random.randrange(730)
        enemyX2 = random.randrange(730)
        enemyX3 = random.randrange(730)
        enemyX4 = random.randrange(730)
        enemyX5 = random.randrange(730)

        print(CurEnemies)
        CurEnemies = random.choice(nums)

    pygame.display.flip()
