import pygame
import random
import sys
import pygame_gui
import time
# Khởi tạo Pygame

# Các biến toàn cục
SCREEN_WIDTH = 360
SCREEN_HEIGHT = 640
BIRD_WIDTH = 34
BIRD_HEIGHT = 24
PIPE_WIDTH = 64
PIPE_Y = 412
PIPE_SPEED = 3
GAP = PIPE_Y / 2
GRAVITY = 0.4

COIN_WIDTH = 24
COIN_HEIGHT = 24

SHIELD_WIDTH = 24
SHIELD_HEIGHT = 24

APPLE_WIDTH = 24
APPLE_HEIGHT = 24

# Màu sắc
WHITE = (255, 255, 255)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("NguyenTuanTai_2174802010740 Flappy Bird") 
pygame.display.set_icon(pygame.image.load("./assets/images/bird2.png"))

# Tọa độ của background
# Tọa độ của ground
ground_x = 0
background_x = 0
# Tốc độ ban đầu của background và ground
background_speed = 0.3
ground_speed = 3

flappy_bird_text_x = SCREEN_WIDTH/6 * 5
flappy_bird_text_y = SCREEN_HEIGHT/ 8 

# kiem tra trang thai game bat dau
game_played = False
# Khởi tạo vị trí ban đầu cho đồng xu (ngẫu nhiên)
coin_x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2)
coin_y = random.randint(200, 500)
shield_x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2)
shield_y = random.randint(200, 500)
apple_x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2)
apple_y = random.randint(200, 500)


coin_image = pygame.image.load("./assets/images/coin.png")
coin_image = pygame.transform.scale(coin_image, (COIN_WIDTH, COIN_HEIGHT))


shield_image = pygame.image.load("./assets/images/shield.png")
shield_image = pygame.transform.scale(shield_image, (SHIELD_WIDTH, SHIELD_HEIGHT))


apple_image = pygame.image.load("./assets/images/apple.png")
apple_image = pygame.transform.scale(apple_image, (APPLE_WIDTH, APPLE_HEIGHT))

sshield_avaiable = False
shield_timer = 0  
shield_interval = 700  # Thời gian xuất hiện đồng xu ngẫu nhiên (đơn vị: frame)

coin_timer = 0
coin_interval = 500  # Thời gian xuất hiện đồng xu ngẫu nhiên (đơn vị: frame)

apple_timer = 0
apple_interval = 300



# Tải hình ảnh chim và ống
bird = pygame.image.load("./assets/images/bird2.png")
# bird = pygame.transform.scale(bird, (BIRD_WIDTH, BIRD_HEIGHT))
top_pipe = pygame.image.load("./assets/images/toppipe.png")
top_pipe = pygame.transform.scale(top_pipe, (PIPE_WIDTH, PIPE_Y))
bottom_pipe = pygame.image.load("./assets/images/bottompipe.png")
bottom_pipe = pygame.transform.scale(bottom_pipe, (PIPE_WIDTH, PIPE_Y))
background = pygame.image.load("./assets/images/flappybirdbg.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
ground = pygame.image.load("./assets/images/ground.png")
ground = pygame.transform.scale(ground, (SCREEN_WIDTH, SCREEN_HEIGHT / 6))
flappy_bird_text = pygame.image.load("./assets/images/flappybirdtext.png")
flappy_bird_text = pygame.transform.scale(flappy_bird_text, (flappy_bird_text_x ,flappy_bird_text_y))


# sound
point_sound = pygame.mixer.Sound("./assets/sounds/point.wav")
wing_sound = pygame.mixer.Sound("./assets/sounds/wing.wav")
hit_sound = pygame.mixer.Sound("./assets/sounds/hit.wav")

# cua so quan ly gui pygame
manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))


# Tạo một label để hiển thị điểm số
score_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((10, 10), (100, 30)),
    text="Score: 0",
    manager=manager
)

shield_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((10, 10), (300, 30)),
    text="Shield",
    manager=manager
)


# Điểm số ban đầu
score = 0
pipe_pass = False

bird_images = [ 
    pygame.image.load("./assets/images/bird1.png"),
    pygame.image.load("./assets/images/bird2.png"),
    pygame.image.load("./assets/images/bird3.png")
]

bird_animation_index = 0  # Chỉ số của hình ảnh chim trong danh sách
flapping_time = 0

# Khởi tạo tọa độ và tốc độ  của chim và ống
bird_x = 100
bird_y = SCREEN_HEIGHT // 2
bird_speed = 0
pipe_x = SCREEN_WIDTH
def randomY():
    return -random.randint(100, 400)    
PIPE_Y = randomY()
rotate_deg = 45


# Đếm số frame để tăng tốc độ
frame_count = 0
speed_increase_interval = 500  # Tăng tốc độ mỗi 100 frame

clock = pygame.time.Clock()
running = True



 
def draw_item(screen, item_image, item_x, item_y):
    screen.blit(item_image, (item_x, item_y))


def check_collision_with_coin(bird_x, bird_y, coin_x, coin_y):
    # Kiểm tra khoảng cách của chim và đồng xu
    if bird_x + BIRD_WIDTH > coin_x and bird_x < coin_x + COIN_WIDTH:
        if bird_y + BIRD_HEIGHT > coin_y and bird_y < coin_y + COIN_HEIGHT:
            return True
    return False

def check_collision_with_shield(bird_x, bird_y, shield_x, shield_y):
    # Kiểm tra khoảng cách của chim và đồng xu
    if bird_x + BIRD_WIDTH > shield_x and bird_x < shield_x + COIN_WIDTH:
        if bird_y + BIRD_HEIGHT > shield_y and bird_y < shield_y + COIN_HEIGHT:
            return True
    return False

def check_collision_with_apple(bird_x, bird_y, apple_x, apple_y):
    # Kiểm tra khoảng cách của chim và đồng xu
    if bird_x + BIRD_WIDTH > apple_x and bird_x < apple_x + APPLE_WIDTH:
        if bird_y + BIRD_HEIGHT > apple_y and bird_y < apple_y + APPLE_HEIGHT:
            return True
    return False

# Thêm đoạn mã sau vòng lặp chính để tạo đồng xu và kiểm tra va chạm





def draw_background(screen, background):
    global background_x
    screen.blit(background, (background_x, 0))
    screen.blit(background , (background_x + SCREEN_WIDTH, 0))
    if (background_x + SCREEN_WIDTH < 0):
        background_x = 0
    
def draw_ground(screen, ground):
    global ground_x
    screen.blit(ground, (ground_x, 534))
    screen.blit(ground, (ground_x + SCREEN_WIDTH, 534))
    if(ground_x + SCREEN_WIDTH < 0):
        ground_x = 0


def draw_bird(screen, bird):
    screen.blit(bird, (bird_x, bird_y))

def draw_pipe(screen, top_pipe, bottom_pipe, pipe_x):
    global pipe_pass
    pipe_pass = False
    screen.blit(top_pipe, (pipe_x, PIPE_Y))
    screen.blit(bottom_pipe, (pipe_x, PIPE_Y + 412 + GAP))

def check_collision(bird_x, bird_y, pipe_x, PIPE_Y):
    # Kiểm tra khoảng cách của chim với ống nước  
    if bird_x + BIRD_WIDTH > pipe_x and bird_x < pipe_x + PIPE_WIDTH:
        # Kiểm tra khoảng cách của chim với phần thân ống nước
        if bird_y < PIPE_Y + 412 or bird_y + BIRD_HEIGHT > PIPE_Y + 412 + GAP:
            return True
    return False




def scored():
    global score, pipe_pass
    if(bird_x >= pipe_x + PIPE_WIDTH):
        pipe_pass = True
        score += 1
        point_sound.play()
        pipe_pass = False
    return score

def play_game(screen):
    global bird_speed, bird_y, bird_x, rotate_deg, pipe_x, PIPE_SPEED, frame_count, PIPE_Y, flapping_time, bird_animation_index, score, background_speed,ground_speed,frame_count, running, shield_interval, coin_x, coin_y, coin_image, shield_x, shield_y, shield_image, coin_interval ,shield_timer, coin_timer, count_down, shield_avaiable, apple_timer, apple_interval, apple_x , apple_y, checked_collision, GAP
    
    bird_speed += GRAVITY 
    bird_y += bird_speed
    pipe_x -= PIPE_SPEED
    rotate_deg -= 2
    coin_x -= PIPE_SPEED
    shield_x -= PIPE_SPEED
    apple_x -= PIPE_SPEED
     
    # Nếu đến số frame đã xác định, tăng tốc độ
   
    # if frame_count >= speed_increase_interval:
    #     PIPE_SPEED += 0.1  # Tăng tốc độ của ống
    #     background_speed += 0.001  # Tăng tốc độ background
    #     ground_speed += 0.01  # Tăng tốc độ ground
    #     frame_count = 0

    # Nếu ống đi ra ngoài màn hình, tạo ống mới
    if pipe_x + PIPE_WIDTH < 0:
        pipe_x = SCREEN_WIDTH
        PIPE_Y = randomY()

    # Kiểm tra va chạm
    if checked_collision:
        score = 0
        hit_sound.play()
        running = False

    

    if bird_y + BIRD_HEIGHT >= SCREEN_HEIGHT - (SCREEN_HEIGHT / 6):
        running = False  # Dừng trò chơi nếu chim chạm đất

    flapping_time += 1
    if flapping_time >= 5:
        flapping_time = 0

    if flapping_time == 4:
        bird_animation_index += 1
    if bird_animation_index >= len(bird_images):
        bird_animation_index = 0

    bird = bird_images[bird_animation_index]
    bird = pygame.transform.scale(bird, (BIRD_WIDTH, BIRD_HEIGHT))
    bird = pygame.transform.rotate(bird, rotate_deg)


    shield_timer += 1
    if shield_timer >= shield_interval:
        shield_timer = 0
        shield_x = SCREEN_WIDTH
        shield_y = random.randint(200, 500)

    coin_timer += 1
    if coin_timer >= coin_interval:
        coin_timer = 0
        # coin_x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2)
        coin_x = SCREEN_WIDTH
        coin_y = random.randint(200, 500)

    apple_timer += 1
    if apple_timer >= apple_interval:
        apple_timer = 0 
        # apple_x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2)
        apple_x = SCREEN_WIDTH
        apple_y = random.randint(200, 500)

    if check_collision_with_coin(bird_x, bird_y, coin_x, coin_y):
        score += 10  # Tăng điểm khi va chạm với đồng xu
        coin_x = -SCREEN_WIDTH
        coin_y = -SCREEN_HEIGHT 

    if check_collision_with_shield(bird_x, bird_y, shield_x, shield_y):
        shield_label.set_text("Shield avaiable on: 15s")
        shield_x = -SCREEN_WIDTH
        shield_y = - SCREEN_HEIGHT
    if check_collision_with_apple(bird_x, bird_y, apple_x, apple_y):
        score += 10
        GAP = -PIPE_Y / 0.7
        apple_x = -SCREEN_WIDTH
        apple_y = -SCREEN_HEIGHT
        

    draw_bird(screen, bird) 
    draw_pipe(screen, top_pipe, bottom_pipe, pipe_x) 
    score_label.set_text("Score: " + str(scored()))
    draw_item(screen, coin_image, coin_x, coin_y)
    draw_item(screen, shield_image, shield_x, shield_y)
    draw_item(screen, apple_image, apple_x, apple_y)


    # Cập nhật quản lý giao diện
    manager.update(1.0 / 60.0)
    manager.draw_ui(screen)
 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = -8
                rotate_deg = 45
                wing_sound.play()
     # Cập nhật điểm số 
    background_x -= background_speed
    ground_x -= ground_speed
    checked_collision =  check_collision(bird_x, bird_y, pipe_x, PIPE_Y)


    draw_background(screen, background)


    play_game(screen)

    draw_ground(screen, ground)

    pygame.display.update() 

    clock.tick(60)

pygame.quit()
sys.exit()
