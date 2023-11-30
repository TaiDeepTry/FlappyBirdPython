import pygame
from pygame.locals import *
import random

pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
fps = 60

screen_width = 648
screen_height = 702

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("NguyenTuanTai_2174802010740 Flappy Bird") 
pygame.display.set_icon(pygame.image.load("./assets/images/bird2.png"))

font = pygame.font.SysFont("04b19", 60)
expressionfont = pygame.font.SysFont("04b19", 30)
score_display = pygame.font.SysFont("04b19", 40)
text_display = pygame.font.SysFont("04b19", 20)

white = (255, 255, 255)
black = (0, 0, 0)


# game variable
ground_scroll = 0
scroll_speed = 4
flying = False
gameover = False
pipe_gap = 150
pipe_freequency = 3000
item_frequency = 7000
last_pipe_time = pygame.time.get_ticks() - pipe_freequency
last_item_time = pygame.time.get_ticks()
item_collide_time = pygame.time.get_ticks()
score = 0
pass_pipe = False
pass_item = False
higest_score = 0
excute = False
shield_active = False
apple_active = False
heart_active = False
dead_rotate = 0
lives = 1
plus_score = False
MAIN_MENU = 0
GAMEPLAY = 1
SETTING = 2
SELECT_MODE = 3
SETTING = 4
game_state = MAIN_MENU

CLASSIC = 0
ADVENTURE = 1
MATH = 2
game_mode = CLASSIC


bird_choosed = "yellow"
bg_choosed = "day"
# load image
bg = pygame.image.load("./assets/images/daybg.png")
bg = pygame.transform.scale(bg,(648,702))
ground_img = pygame.image.load("./assets/images/ground.png")
ground_img = pygame.transform.scale(ground_img, (648, 216))
button_img = pygame.image.load("./assets/images/restartbutton.png")
button_img = pygame.transform.scale(button_img, ( 142, 50))
gameover_img = pygame.image.load("./assets/images/gameovertext.png") 
gameover_img = pygame.transform.scale(gameover_img, (518, 113))
flappybirdtext_img = pygame.image.load("./assets/images/flappybirdtext.png")
flappybirdtext_img = pygame.transform.scale( flappybirdtext_img, (466, 126))
board_img = pygame.image.load("./assets/images/board.png")
board_img = pygame.transform.scale(board_img, (screen_width * 50 / 100, screen_width * 50 / 100 * 513 / 1017))
shield_img = pygame.image.load("./assets/images/shield.png")
shield_img = pygame.transform.scale(shield_img, (30, 30))
coin_img = pygame.image.load("./assets/images/coin.png")
coin_img = pygame.transform.scale(coin_img, (30, 30))
apple_img = pygame.image.load("./assets/images/apple.png")
apple_img = pygame.transform.scale(apple_img, (30, 30))
heart_img = pygame.image.load("./assets/images/heart.png")
heart_img = pygame.transform.scale(heart_img, (30, 30))
scoreplus_img = pygame.image.load("./assets/images/+1.png")
scoreplus_img = pygame.transform.scale( scoreplus_img,(30, 23))
liveplus_img = pygame.image.load("./assets/images/+heart.png") 
liveplus_img = pygame.transform.scale( liveplus_img,(41.1, 23))
playbutton_img = pygame.image.load("./assets/images/playbutton.png")
playbutton_img = pygame.transform.scale(playbutton_img, (190, 106))

homebutton_img = pygame.image.load("./assets/images/homebutton.png")
homebutton_img = pygame.transform.scale(homebutton_img, (142, 50))

classicbutton_img = pygame.image.load("./assets/images/classicmode.png")
classicbutton_img = pygame.transform.scale(classicbutton_img, (142, 50))

adventurebutton_img = pygame.image.load("./assets/images/adventuremode.png")
adventurebutton_img = pygame.transform.scale(adventurebutton_img, (142, 50))

mathbutton_img = pygame.image.load("./assets/images/mathmode.png")
mathbutton_img = pygame.transform.scale(mathbutton_img, (142, 50 ))

gear_img = pygame.image.load("./assets/images/gear.png")
gear_img = pygame.transform.scale(gear_img, (30, 30))

yellow_bird = pygame.image.load("./assets/images/bird2.png")
yellow_bird = pygame.transform.scale(yellow_bird, (93, 66))
red_bird = pygame.image.load("./assets/images/red_bird2.png")
red_bird = pygame.transform.scale(red_bird, (93, 66))
blue_bird = pygame.image.load("./assets/images/blue_bird2.png")
blue_bird = pygame.transform.scale(blue_bird, (93, 66))

# load sound
point_sound = pygame.mixer.Sound("./assets/sounds/point.wav")
wing_sound = pygame.mixer.Sound("./assets/sounds/wing.wav")
hit_sound = pygame.mixer.Sound("./assets/sounds/hit.wav")

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def reset_game():
    global pass_pipe, excute, pipe_gap, lives, apple_active, heart_active, now , shield_active
    pipe_group.empty()
    item_group.empty()
    flappy.rect.x = 100
    flappy.rect.y = int(screen_height / 2)
    score = 0
    pass_pipe = False
    excute = False
    pipe_gap = 150
    shield_active = False
    heart_active = False
    apple_active = False
    now = pygame.time.get_ticks()
    lives = 1
    return score
def playgame():
    global game_state
    game_state = SELECT_MODE
    flappy.rect.x = 100
    flappy.rect.y = int(screen_height / 2)
def turnhome():
    global game_state, gameover
    game_state = MAIN_MENU
    gameover = False
    reset_game()

def classic_mode():
    global game_mode,game_state
    reset_game()
    game_mode = CLASSIC
    game_state = GAMEPLAY
def adventure_mode():
    global game_mode, game_state
    reset_game()
    game_mode = ADVENTURE
    game_state = GAMEPLAY
def math_mode():
    global game_mode, game_state
    reset_game()
    game_mode = MATH
    game_state = GAMEPLAY
def setting():
    global game_state
    game_state = SETTING

def choose_redbird():
    global bird_choosed
    bird_choosed = "red"
    choosed_bird()

def choose_yellowbird():
    global bird_choosed
    bird_choosed = "yellow"
    choosed_bird()

def choose_bluebird():
    global bird_choosed
    bird_choosed = "blue"
    choosed_bird()
def choosed_bird():
    if bird_choosed == "blue":
        return "blue_bird"
    elif bird_choosed == "yellow":
        return "bird"
    else:
        return "red_bird"
    
def choose_day():
    global bg_choosed
    bg_choosed = "day"
    
def choose_night():
    global bg_choosed
    bg_choosed = "night"
def choosed_bg():
    if bg_choosed == "day":
        return "day"
    else:
        return "night"
def generate_random_expression(correct_position):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(['+', '-'])
    expression = f"{num1} {operator} {num2}"

    if operator == '+':
        correct_result = num1 + num2
        incorrect_result = correct_result + random.randint(1, 5)
    else:
        correct_result = num1 - num2
        incorrect_result = correct_result + random.randint(1, 5)



    if correct_position == 0:
        return f"{expression} = {correct_result}", f"{expression} = {incorrect_result}"
    else:
        return f"{expression} = {incorrect_result}", f"{expression} = {correct_result}"
    

def draw_expression(expression1, expression2):
    text1 = expressionfont.render(expression1, True, black)
    text2 = expressionfont.render(expression2, True, black)

    screen.blit(text1, (mdl_pipe.rect.x, mdl_pipe.rect.y - 100))
    screen.blit(text2, (mdl_pipe.rect.x, mdl_pipe.rect.y + 165 + 70 ))

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.index=0
        self.counter = 0
        for num in range(1, 4):
            original_image = pygame.image.load(f"./assets/images/{choosed_bird()}{num}.png")
            img = pygame.transform.scale(original_image, (38.25, 27))
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False
    
    def update(self):
        if flying == True:
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 576:
                self.rect.y += int(self.vel)
        if gameover == False:
            if pygame.key.get_pressed()[K_SPACE] and self.clicked == False:
                self.clicked = True
                self.vel = -10
                # wing_sound.play()
            if pygame.key.get_pressed()[K_SPACE] == 0:
                self.clicked = False

            self.counter += 1
            flap_cooldown = 5

            if self.counter > flap_cooldown:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]
            if flying:
                self.image = pygame.transform.rotate(self.images[self.index], self.vel * -3)
        elif gameover == True:
            self.image = pygame.transform.rotate(self.images[self.index], -70)
        elif game_state == MAIN_MENU:
            self.image = pygame.transform.rotate(self.images[self.index], 0)
    # def draw_hit_box(self, screen):
    #     pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)
    def check_collision_with_expression(self, expression_rect):
        return self.rect.colliderect(expression_rect)


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./assets/images/bottompipe.png")
        self.image = pygame.transform.scale(self.image, (58.5, 420))
        self.rect = self.image.get_rect()
        self.rect.center = [x ,y]
        #position 1 is from the top, -1 is from the bottom
        if game_mode == ADVENTURE or game_mode == CLASSIC:
            if position == 1:
                self.image = pygame.transform.flip(self.image, False, True)
                self.rect.bottomleft = [x, y - int(pipe_gap / 2)]
            if position == -1:
                self.rect.topleft = [x, y + int(pipe_gap / 2)]
        else:
            if position == 1:
                self.image = pygame.transform.flip(self.image, False, True)
                self.rect.bottomleft = [x, y - int(300 / 2) - 165 / 2]
            if position == -1:
                self.rect.topleft = [x, y + int(300 / 2) + 165 / 2]
            if position == 0:
                # self.image = pygame.transform.flip(self.image, False, True)
                self.image = pygame.image.load("./assets/images/midlepipe.png")
                self.image = pygame.transform.scale(self.image, (58.5, 165))
                self.rect = self.image.get_rect()
                self.rect.bottomleft = [x, y + 165 / 2 ]

    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()
    # def draw_hit_box(self, screen):
    #     # Draw a red rectangle around the pipe's hit box
    #     pygame.draw.rect(screen, (255, 0, 0), self.rect, 2)

class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, image, name):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.name = name
    def update(self):
        self.rect.x -= scroll_speed
        if self.rect.right < 0:
            self.kill()
    
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

class Button_click():
    def __init__(self, x, y, image, function):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.click_function = function  # Store the function
    def draw(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.click_function()  

        screen.blit(self.image, (self.rect.x, self.rect.y))

run = True
bird_group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()
item_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 2))
bird_group.add(flappy)
reset_button = Button(253, 468, button_img)
num = 1



while run:

    clock.tick(fps)
    screen.blit(bg, (0,0))
    images=[]
    index=0
    num += 1.2
    if num <= 10:
        original_image = pygame.image.load(f"./assets/images/{choosed_bird()}1.png")
    elif num <= 20:
        original_image = pygame.image.load(f"./assets/images/{choosed_bird()}2.png")
    elif num <= 30:
        original_image = pygame.image.load(f"./assets/images/{choosed_bird()}3.png")
        num = 1
    img = pygame.transform.scale(original_image, (38.25, 27))
    images.append(img)
    bird_group.sprites()[0].image = images[index]
    if game_state == GAMEPLAY and (game_mode == CLASSIC or game_mode == ADVENTURE):
        pipe_freequency = 1500
        bird_group.draw(screen)
        bird_group.update()
        pipe_group.draw(screen)
        item_group.draw(screen)

        if lives == 0:
                gameover = True
                # hit_sound.play()

        if lives >= 3:
            lives = 3
        if len(pipe_group) > 0:
            if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left and  bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right and pass_pipe == False: 
                pass_pipe = True
            if pass_pipe == True:
                screen.blit(scoreplus_img, (bird_group.sprites()[0].rect.x + 50, bird_group.sprites()[0].rect.y - 50))
                if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:    
                    score += 1
                    pass_pipe = False
                    # point_sound.play()
        if apple_active == False:
            pipe_gap = 150

        draw_text(str(score), font, black, 24, 20)
        draw_text(str(score), font, white, 20, 16)
        if game_mode == ADVENTURE:
            for i in range(lives):
                screen.blit(heart_img, (20 + i * 35, 80))

        # check collide with pipe
        if shield_active == False:
            if lives > 1:
                if pygame.sprite.groupcollide(bird_group, pipe_group, False, True) or flappy.rect.top < 0:
                    lives -= 1
            else:
                if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
                    lives -= 1


        # check collition width item
        if pygame.sprite.groupcollide(bird_group, item_group, False, True):
            item_collide_now = pygame.time.get_ticks()
            excute = True
            plus_score = True

        if excute == True and choose.name == "shield":
            now = pygame.time.get_ticks()
            shield_active = True
            draw_text(f"shield active in {round( 5 -(now - item_collide_now)/1000)}", text_display, black, 72, 22)
            draw_text(f"shield active in {round( 5 -(now - item_collide_now)/1000)}", text_display, white, 70, 20)
            screen.blit(shield_img, (bird_group.sprites()[0].rect.x + 50, bird_group.sprites()[0].rect.y - 30))
            item_group.empty()
            if excute == True and now - item_collide_now >= 5050:
                shield_active = False
                excute = False
                item_collide_now = now
        
        elif excute == True and choose.name == "coin":
            score += 1
            excute = False

        elif excute == True and choose.name == "heart":
            if plus_score:
                lives += 1
                plus_score = False
            now = pygame.time.get_ticks()
            heart_active = True
            screen.blit(liveplus_img, (bird_group.sprites()[0].rect.x + 50, bird_group.sprites()[0].rect.y - 30))
            if excute and now - item_collide_now >= 550:
                excute = False
                heart_active = False
                plus_score = False
                item_collide_now = now

        elif excute == True and choose.name == "apple":
            now = pygame.time.get_ticks()
            apple_active = True
            draw_text(f"apple active in {round( 5 -(now - item_collide_now)/1000)}", text_display, black, 72, 22)
            draw_text(f"apple active in {round( 5 -(now - item_collide_now)/1000)}", text_display, white, 70, 20)
            item_group.empty()
            if excute == True and now - item_collide_now >= 5050:
                excute = False
                apple_active = False
                item_collide_now = now
        
        if flappy.rect.bottom >= 575:
            gameover = True 
            flying = False
            
        if gameover == False and flying == True:

            timepipe_now = pygame.time.get_ticks()
            timeitem_now = pygame.time.get_ticks()

            if timepipe_now - last_pipe_time > pipe_freequency:
                pipe_height = random.randint(-100, 100)
                shield_height = pipe_height + screen_height // 2
                top_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, 1)
                btm_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1)
                pipe_group.add(btm_pipe)
                pipe_group.add(top_pipe)
                last_pipe_time = timepipe_now
        
            if timeitem_now - last_item_time > item_frequency:
            
                shield = Item(screen_width, random.randint(shield_height , shield_height + pipe_gap - 50),shield_img, "shield")
                coin = Item(screen_width, random.randint(shield_height , shield_height + pipe_gap - 50),coin_img, "coin")
                apple = Item(screen_width, random.randint(shield_height , shield_height + pipe_gap - 50),apple_img, "apple")
                heart = Item(screen_width, random.randint(shield_height , shield_height + pipe_gap - 50),heart_img, "heart")
                if game_mode == CLASSIC:
                    list_choose = []
                elif game_mode == ADVENTURE:
                    list_choose = [ coin, apple, heart, shield]
                    choose = random.choice(list_choose) 
                    item_group.add(choose)
                    last_item_time = timeitem_now

            ground_scroll -= scroll_speed
            if ground_scroll + 648  < 0 :
                ground_scroll = 0

            if apple_active:
                pipe_gap = 300
            item_group.update()
            pipe_group.update()
    elif game_state == GAMEPLAY and game_mode == MATH:
            pipe_freequency = 3000
            bird_group.draw(screen)
            bird_group.update()
            # for bird in bird_group:
            #     bird.draw_hit_box(screen)
            pipe_group.draw(screen)
            # for pipe in pipe_group:
            #     pipe.draw_hit_box(screen)
            item_group.draw(screen)
            if len(pipe_group) > 0:
                if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.left and  bird_group.sprites()[0].rect.right < pipe_group.sprites()[0].rect.right and pass_pipe == False: 
                    pass_pipe = True
                if pass_pipe == True:
                    screen.blit(scoreplus_img, (bird_group.sprites()[0].rect.x + 50, bird_group.sprites()[0].rect.y - 50))
                    if bird_group.sprites()[0].rect.left > pipe_group.sprites()[0].rect.right:    
                        score += 1
                        pass_pipe = False

            draw_text(str(score), font, black, 24, 20)
            draw_text(str(score), font, white, 20, 16)

            if pygame.sprite.groupcollide(bird_group, pipe_group, False, False) or flappy.rect.top < 0:
                gameover = True

            if flappy.rect.bottom >= 575:
                gameover = True 
                flying = False
                
            if gameover == False and flying == True:

                timepipe_now = pygame.time.get_ticks()
                timeitem_now = pygame.time.get_ticks()

                if timepipe_now - last_pipe_time > pipe_freequency:
                    global mdl_pipe
                    pipe_height = -50
                    shield_height = pipe_height + screen_height // 2
                    top_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, 1)
                    btm_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, -1)
                    mdl_pipe = Pipe(screen_width, int(screen_height / 2) + pipe_height, 0)
                    pipe_group.add(btm_pipe)
                    pipe_group.add(mdl_pipe)
                    pipe_group.add(top_pipe)    
                
                    correct_position = random.choice([0, 1])
                    expression1, expression2 = generate_random_expression(correct_position)
                    last_pipe_time = timepipe_now

                ground_scroll -= scroll_speed
                if ground_scroll + 648  < 0 :
                    ground_scroll = 0
                draw_expression(expression1, expression2)
                expression1_rect = expressionfont.render(expression1, True, black).get_rect(topleft=(mdl_pipe.rect.x, mdl_pipe.rect.y - 100))
                expression2_rect = expressionfont.render(expression2, True, black).get_rect(topleft=(mdl_pipe.rect.x, mdl_pipe.rect.y + 165 + 70))
                for bird in bird_group:
                    if correct_position == 0:
                        if any(bird.check_collision_with_expression(expression_rect) for expression_rect in [expression2_rect]) :
                        # Collision with the expression
                            gameover = True
                    else:
                        if any(bird.check_collision_with_expression(expression_rect) for expression_rect in [expression1_rect]) :
                        # Collision with the expression
                            gameover = True
                item_group.update()
                pipe_group.update()
    elif game_state == MAIN_MENU:
        screen.blit(flappybirdtext_img, (91,40))
        flappy.rect.x = 305
        flappy.rect.y = 230
        bird_group.draw(screen)
        bird_group.update() 
        Button_click(229, 372,playbutton_img, playgame).draw()
        Button_click(229, 372,playbutton_img, playgame).draw()
        Button_click(601, 10,gear_img, setting).draw()
    elif game_state == SELECT_MODE:
        screen.blit(flappybirdtext_img, (91,40))
        flappy.rect.x = 305
        flappy.rect.y = 230
        bird_group.draw(screen)
        bird_group.update() 
        Button_click(253, 300,classicbutton_img, classic_mode).draw()
        Button_click(253, 370,adventurebutton_img, adventure_mode).draw()
        Button_click(253, 440,mathbutton_img, math_mode).draw()
    elif game_state == SETTING:
        screen.blit(flappybirdtext_img, (91,40))
        flappy.rect.x = 305
        flappy.rect.y = 230
        Button_click(18, 284, playbutton_img, choose_yellowbird).draw()
        screen.blit(yellow_bird, (64, 310))
        Button_click(230, 284, playbutton_img, choose_redbird).draw()
        screen.blit(red_bird, (279, 310))
        Button_click(445, 284, playbutton_img, choose_bluebird).draw()
        screen.blit(blue_bird, (494, 310))
        bird_group.draw(screen)
        bird_group.update() 
        Button_click(253, 530,homebutton_img, turnhome).draw()

    screen.blit(ground_img, (ground_scroll,576))
    screen.blit(ground_img, (ground_scroll + 648 ,576)) 

    if gameover == True and game_state == GAMEPLAY:
        screen.blit(gameover_img, (int(screen_width // 2) - gameover_img.get_width() // 2,int( screen_height / 5 )))
        screen.blit(board_img, (int(screen_width // 2) - board_img.get_width() // 2,int( screen_height / 2.5 )))
        draw_text(str(score), score_display, black, 418, 326)
        draw_text(str(score), score_display, white, 414, 322)
        draw_text(str(higest_score), score_display, black, 418, 390)
        draw_text(str(higest_score), score_display, white, 414, 386)
        Button_click(253, 530,homebutton_img, turnhome).draw()
        if score >= higest_score:
            higest_score = score
        if reset_button.draw() == True:
            gameover = False
            score = reset_game() 
            

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE and flying == False and gameover == False and game_state == GAMEPLAY:
                flying = True


    pygame.display.update()


pygame.quit()