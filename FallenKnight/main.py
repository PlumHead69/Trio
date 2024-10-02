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

enemyX6 = random.randrange(30,148)
enemyX7 = random.randrange(148,296)
enemyX8 = random.randrange(296,444)
enemyX9 = random.randrange(444,592)
enemyX0 = random.randrange(592,740)

enemyY = 1000
enemyY2 = 1000

jumping = False
ygravity = 0.2
jumheight = 12
yvelocity = jumheight



clock = pygame.time.Clock()
fps = 120
more = False

athalf = False
dead = False
once = False
enemyspeed = 2

nums = ["three","four","five"]
CurEnemies = random.choice(nums)
CurEnemies2 = random.choice(nums)

font = pygame.font.Font('freesansbold.ttf', 20)


while running:

    enemy1 = pygame.Rect(enemyX1, enemyY, 50, 4)
    enemy2 = pygame.Rect(enemyX2, enemyY, 50, 4)
    enemy3 = pygame.Rect(enemyX3, enemyY, 50, 4)
    enemy4 = pygame.Rect(enemyX4, enemyY, 50, 4)
    enemy5 = pygame.Rect(enemyX5, enemyY, 50, 4)
    enemy6 = pygame.Rect(enemyX6, enemyY2, 50, 4)
    enemy7 = pygame.Rect(enemyX7, enemyY2, 50, 4)
    enemy8 = pygame.Rect(enemyX8, enemyY2, 50, 4)
    enemy9 = pygame.Rect(enemyX9, enemyY2, 50, 4)
    enemy0 = pygame.Rect(enemyX0, enemyY2, 50, 4)

    enemies = [enemy1,enemy2,enemy3,enemy4,enemy5,enemy6,enemy7,enemy8,enemy9,enemy0]
    collided = False
    pygame.time.get_ticks()
    clock.tick(fps)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()
    if playerX > 0:
        if pressed[pygame.K_a]: playerX -= 1
    if playerX < 800 - 25:
        if pressed[pygame.K_d]: playerX += 1
    if pressed[pygame.K_SPACE]:
        jumping = True
        


    if jumping:
        shotgunblast = pygame.draw.circle(screen, (255, 0, 0), [playerX+34, playerY+50], 10)
        playerY -= yvelocity
        yvelocity -= ygravity
        if yvelocity < -jumheight:
            yvelocity = jumheight
    
        


    if playerY > 1100 or playerY < -10:
        dead = True
    
    

    if dead == False:
        points = round(pygame.time.get_ticks()/10)
        text = font.render(f"Points: {str(points)}", True, (0,0,0))
        textRect = text.get_rect()
        textRect.center = (700, 20)
        screen.fill((255, 255, 255))
    else:
        
        
        font = pygame.font.Font('freesansbold.ttf', 60)
        text = font.render(f"ALL POINTS    :   {str(round(points))}", True, (255,0,0))
        textRect = text.get_rect()
        textRect.center = (380, 400)
        
        """if round(points) > 600:
            text2 = font.render(f"Nyertel egy matricat!", True, (255,0,0))
            textRect2 = text2.get_rect()
            textRect2.center = (380, 500)
            
            screen.fill((0,0,0))"""


    player = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(playerX, playerY, 25, 25))
    shotgun = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(playerX+30, playerY, 7, 40))
    
    
    
    if enemyY < 500:
        athalf = True
    
    if player.collidelist(enemies) != -1:
        collided = True


    if collided:
        once = True
        jumping = False
        playerY -= enemyspeed
    elif collided == False:
        playerY +=3
        

    #wave 1
    if CurEnemies == "three":
        pygame.draw.rect(screen, (0,0,0),enemy1 )
        pygame.draw.rect(screen, (0,0,0),enemy2 )
        pygame.draw.rect(screen, (0,0,0),enemy3 )

    elif CurEnemies == "four":

        pygame.draw.rect(screen, (0,0,0),enemy1 )
        pygame.draw.rect(screen, (0,0,0),enemy2 )
        pygame.draw.rect(screen, (0,0,0),enemy3 )
        pygame.draw.rect(screen, (0,0,0),enemy4 )
        
    elif CurEnemies == "five":

        pygame.draw.rect(screen, (0,0,0),enemy1 )
        pygame.draw.rect(screen, (0,0,0),enemy2 )
        pygame.draw.rect(screen, (0,0,0),enemy3 )
        pygame.draw.rect(screen, (0,0,0),enemy4 )
        pygame.draw.rect(screen, (0,0,0),enemy5 )

    #wave 2
    if athalf == True:
        enemyY2 -= enemyspeed
        if CurEnemies2 == "three":
            pygame.draw.rect(screen, (0,0,0), enemy6)
            pygame.draw.rect(screen, (0,0,0), enemy7)
            pygame.draw.rect(screen, (0,0,0), enemy8)

        elif CurEnemies2 == "four":

            pygame.draw.rect(screen, (0,0,0), enemy6)
            pygame.draw.rect(screen, (0,0,0), enemy7)
            pygame.draw.rect(screen, (0,0,0), enemy8)
            pygame.draw.rect(screen, (0,0,0), enemy9)
            
        elif CurEnemies2 == "five":

            pygame.draw.rect(screen, (0,0,0), enemy6)
            pygame.draw.rect(screen, (0,0,0), enemy7)
            pygame.draw.rect(screen, (0,0,0), enemy8)
            pygame.draw.rect(screen, (0,0,0), enemy9)
            pygame.draw.rect(screen, (0,0,0), enemy0)

    
    
    enemyY -= enemyspeed

    if enemyY == -50:
        CurEnemies = random.choice(nums)
        enemyY = 1000
        enemyX1 = random.randrange(730)
        enemyX2 = random.randrange(730)
        enemyX3 = random.randrange(730)
        enemyX4 = random.randrange(730)
        enemyX5 = random.randrange(730)
        
       
        
        
    if enemyY2 == -50:
        CurEnemies2 = random.choice(nums)
        enemyY2 = 1000
        enemyX6 = random.randrange(730)
        enemyX7 = random.randrange(730)
        enemyX8 = random.randrange(730)
        enemyX9 = random.randrange(730)
        enemyX0 = random.randrange(730)



        if enemyY == 400:
            athalf = False

    screen.blit(text, textRect)
    pygame.display.flip()
    