import pygame
import time
import random
import os
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


def load_high_score():
    if not os.path.exists("highscore.txt"):  
        with open("highscore.txt", "w") as f:
            f.write("0")

    with open("highscore.txt", "r") as f:
        return int(f.read())


def save_high_score(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))


def game_over_screen(score, high_score, new_high):
    run = True

    restart_button = pygame.Rect(WIDTH//2 - 120, HEIGHT//2 + 60, 240, 60)

    while run:
        WIN.blit(BG, (0, 0))

        lost_text = TITLE_FONT.render("YOU LOST", 1, WHITE)
        WIN.blit(lost_text, (WIDTH//2 - lost_text.get_width()//2, 150))

        score_text = BUTTON_FONT.render(f"Score:{score}", 1, WHITE)
        WIN.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 250))

        high_text = BUTTON_FONT.render(f"High Score: {high_score}", 1, WHITE)
        WIN.blit(high_text, (WIDTH//2 - high_text.get_width()//2, 310))

        if new_high:
            new_high_text = BUTTON_FONT.render("NEW HIGH SCORE", 1, RED)
            WIN.blit(new_high_text, (WIDTH//2 - new_high_text.get_width()//2, 360))
            
        # Draw Restart Button
        mouse_pos = pygame.mouse.get_pos()

        if restart_button.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            pygame.draw.rect(WIN, (200,0,0), restart_button)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            pygame.draw.rect(WIN, RED, restart_button)

        restart_text = BUTTON_FONT.render("RESTART", 1, WHITE)
        WIN.blit(
            restart_text,
            (
                restart_button.x + (restart_button.width - restart_text.get_width()) // 2,
                restart_button.y + (restart_button.height - restart_text.get_height()) // 2,
            ),
        )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.collidepoint(event.pos):
                    return "restart"
        
        pygame.display.update()


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


def draw(player, elapsed_time, stars, high_score):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "red", player)

    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    # Draw High Score (top-right)
    high_text = FONT.render(f"High Score: {high_score}", 1, "white")
    WIN.blit(high_text, (WIDTH - high_text.get_width() - 20, 10))


    pygame.display.update() # This line here - make sure jo img lgai hai - refresh and apply changes


def main_menu():
    run = True

    play_button = pygame.Rect(WIDTH//2 - 100, HEIGHT//2 - 25, 200, 50)


    while run:

        WIN.blit(BG, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        if play_button.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


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
                return  

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

    high_score = load_high_score()

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

            score = round(elapsed_time)

            new_high = False

            if score > high_score:
                save_high_score(score)
                high_score = score
                new_high = True

            result = game_over_screen(score, high_score, new_high)
            if result == "restart":
                return "restart"

            # lost_text = FONT.render("You Lost!", 1, "white")
            # WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            # pygame.display.update()
            # pygame.time.delay(4000)
            # break

        draw(player, elapsed_time, stars, high_score)

    pygame.quit()  


if __name__ == "__main__":
    main_menu()
    
    while True:
        result = main()
        if result == "restart":
            continue
        else:
            break

# MENU → GAME → GAME OVER → RESTART → GAME → GAME OVER → RESTART ...