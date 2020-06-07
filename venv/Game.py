import pygame
import random
import math
from pygame import mixer
pygame.init()

vision = pygame.display.set_mode((700, 700))

#Giving the the title and icon
pygame.display.set_caption("Earth Defenders Elite")
icon = pygame.image.load("spaceship.png")

#Background Image
background = pygame.image.load("backimg.jpg")
pygame.display.set_icon(icon)

#Friend Shooter Spacehip
friend = pygame.image.load("spaceshuttle1.png")
friend_x = 318
friend_y = 550
friend_xchange = 0


#Background Music
mixer.music.load("Backg.wav")
mixer.music.play(100)

#Score Board
score=0
font_type=pygame.font.Font("stocky.ttf",30)
font_locx=20
font_locy=20

#Showing the score
def show_score():
    global font_locx
    global font_locy
    score_value=font_type.render("Score :"+str(score),True,(105,255,25))
    vision.blit(score_value,(font_locx,font_locy))

endx_font=270
endy_font=350
game_font_end=pygame.font.Font("Strong Brain.otf",300)


#End Game Display
def end_game():
    global endx_font
    global endy_font
    Final_score=font_type.render("Game Over",True,(0,255,0))
    vision.blit(Final_score,(endx_font,endy_font))

#Initialising the diffent enemies
m0=pygame.image.load("beetle.png")
m1=pygame.image.load("monster1.png")
m2=pygame.image.load("monster2.png")
m3=pygame.image.load("monster3.png")
m4=pygame.image.load("monster4.png")
m5=pygame.image.load("monster5.png")
m6=pygame.image.load("monster6.png")
m7=pygame.image.load("monster7.png")
m8=pygame.image.load("monster8.png")
m9=pygame.image.load("monster9.png")
m10=pygame.image.load("monster10.png")
m11=pygame.image.load("monster11.png")
mlist=[m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11]

#Creating multiple alien
alien=[]
alien_x=[]
alien_y=[]
change_alien_x=[]
change_alien_y=[]
aliens=10
for i in range(10):
    alien.append(random.choice(mlist))
    alien_x.append(random.randint(0, 636))
    alien_y.append(random.randint(0, 300))
    change_alien_x.append(1.5)
    change_alien_y.append(30)

#Bullet For Hitting
bullet = pygame.image.load("bullet.png")
bullet_x = friend_x
bullet_y = friend_y
flag = 1

#Friend
def show_friend(friend_x, friend_y):
    vision.blit(friend, (friend_x, friend_y))

#Alien
def show_alien(alien_x, alien_y,i):
    vision.blit(alien[i], (alien_x, alien_y))


flag_bullet = 0


#Bullet Movement
def show_bullet(bullet_x, bullet_y):
    global flag_bullet
    flag_bullet = 1
    vision.blit(bullet, (bullet_x + 16, bullet_y + 16))

#Calculating Ditance Between Bullet And Alien
def calculate_distance(a, b, c, d):
    distance = math.sqrt(math.pow((a - c), 2) + math.pow((b - d), 2))
    if distance < 50:
        return True
    else:
        return False



place_x = 0
place_y = 0


running = True
while running:
    vision.fill((255, 0, 0))
    vision.blit(background, (0, 0))
    for event in pygame.event.get():
        #For Quitting the game
        if event.type == pygame.QUIT:
            running = False
        #For Different movements of spaceship
        if event.type == pygame.KEYDOWN:
            #Right Movement
            if event.key == pygame.K_RIGHT:
                friend_xchange = 1.5
            #Left Movement
            if event.key == pygame.K_LEFT:
                friend_xchange = -1.5
            #Shooting Bullet
            if (event.key == pygame.K_SPACE and flag_bullet == 0):
                #Bullet Sound
                bsound=mixer.Sound("bull.wav")
                bsound.play()
                place_x = friend_x
                place_y = friend_y
                show_bullet(friend_x, friend_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                friend_xchange += 0
    #Bullet Movement
    if (flag_bullet == 1):
        place_y -= 5
        show_bullet(place_x, place_y)
        if (place_y < 0):
            flag_bullet = 0


    #Setting Limits For Spaceship
    friend_x += friend_xchange
    if (friend_x < 0):
        friend_x = 0
    if (friend_x > 636):
        friend_x = 636


    for j in range(aliens):
        if alien_y[j]>500:
            for r in range(aliens):
                alien_y[r]=1000
                end_game()
            break

        #Changing Enemy Movements
        alien_x[j] += change_alien_x[j]
        if (alien_x[j] > 625):
            change_alien_x[j]=-1.5
            alien_y[j] = alien_y[j] + change_alien_y[j]


        if (alien_x[j] < 0):
            change_alien_x[j]=1.5
            alien_y[j] = alien_y[j] + change_alien_y[j]





        #Hitting Alien Function
        distance = calculate_distance(place_x, place_y, alien_x[j], alien_y[j])
        if distance:
            #Hitsound
            col=mixer.Sound("coll.wav")
            col.play()
            place_y = 700
            flag_bullet = 0
            score = score + 1
            alien[j]=random.choice(mlist)
            alien_x[j] = random.randint(0, 636)
            alien_y[j] = random.randint(0, 300)
            spawn=mixer.Sound("spawn.wav")
            spawn.play()

        show_alien(alien_x[j], alien_y[j],j)


    show_score()
    show_friend(friend_x, friend_y)
    pygame.display.update()
