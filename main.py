import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 900, 700                               # Ye size pixels me hai
WIN = pygame.display.set_mode((WIDTH, HEIGHT))          # Apni gaming window
pygame.display.set_caption("Rain Dodge")                # Would be displayed on TOP - name of the game

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 30
PLAYER_HEIGHT = 50
PLAYER_VEL = 5

STAR_WIDTH = 10
STAR_HEIGHT = 20 
STAR_VEL = 3

WHITE = (255,255,255)
RED = (255,0,0)
BLACK = (0,0,0)


FONT = pygame.font.SysFont("comicsans", 30)
TITLE_FONT = pygame.font.SysFont("comicsans", 60)
BUTTON_FONT = pygame.font.SysFont("comicsans", 40)


def draw_button(text, x, y, width, height, color, hover_color):
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()[0]

    btn_rect = pygame.Rect(x, y, width, height)

    if btn_rect.collidepoint(mouse_pos):
        pygame.draw.rect(WIN, hover_color, btn_rect)
        if click:
            return True    
    else:
        pygame.draw.rect(WIN, color, btn_rect)


    btn_text = BUTTON_FONT.render(text, 1, WHITE)
    WIN.blit(btn_text, (x + (width - btn_text.get_width())//2,
                        y + (height - btn_text.get_height())//2))

    return False


def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "red", player)

    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    pygame.display.update() # This line here - make sure jo img lgai hai - refresh and apply changes


def main_menu():
    run = True

    play_button = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 - 25, 200, 50)

    while run:

        WIN.blit(BG, (0, 0))

        title_text = TITLE_FONT.render("RAIN DODGE", 1, "white")
        WIN.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 150))

       
        pygame.draw.rect(WIN, "red", play_button)

        
        play_text = BUTTON_FONT.render("PLAY", 1, "white")
        WIN.blit(
            play_text,
            (
                play_button.x + (play_button.width - play_text.get_width()) // 2,
                play_button.y + (play_button.height - play_text.get_height()) // 2,
            ),
        )

   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                return  #

            if event.type == pygame.MOUSEBUTTONDOWN:   
                mouse_pos = event.pos                  
                if play_button.collidepoint(mouse_pos):
                    return  

        pygame.display.update()

# For now - on running this program pygame window pops up and then vo disappear hojati hai immediately, that's because maine abhi koi loop nhi lga rkhi so that mera progeam alive rhe.

def main():
    run = True

    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)  #pygame.Rect(x, y, width, height)

    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    star_add_increment = 2000
    star_count = 0

    stars = []
    hit = False

    while run:

        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0

        for event in pygame.event.get():                # Checks har ek event performing in window
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height   >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)

    pygame.quit()  


if __name__ == "__main__":
    main_menu()
    main()