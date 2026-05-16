from pygame import *

back =(134, 165, 52)
win_wight = 500
win_height = 600

window = display.set_mode((win_height,win_wight))
window.fill(back)
clock = time.Clock()

fps = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, widht, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (widht, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    def reset(self):
        window.blit(self.image, (self.rect.x,  self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed



racket1 = Player('racket.png', 30, 200, 4, 50, 150)
racket2 = Player('racket.png', 520, 200, 4, 50, 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)


font.init()
font = font.Font(None, 23)
losel1 = font.render("Player 1 LOSE", True, (100, 0, 0))
losel2 = font.render("Player 2 LOSE", True, (100, 0, 0))

speed_x = 3
speed_y = 3

game = True
finish  =False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        window.fill(back)
        racket1.update_l()
        racket2.update_r()

        racket1.reset()
        racket2.reset()
        ball.reset()
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y += -1

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x += -1
        
        if ball.rect.x < 0:
            finish = True
            window.blit(losel1, (200, 200))
            game_over = True
        
        if ball.rect.x > win_wight:
            finish = True
            window.blit(losel2, (200, 200))
            game_over = True
    display.update()
    clock.tick(fps)


