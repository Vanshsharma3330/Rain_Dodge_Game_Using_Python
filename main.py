from settings import *
from utils import *
from screens.menu import main_menu
from screens.pause import pause_screen
from screens.game_over import game_over_screen

import pygame
import time
import random

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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    result = pause_screen()
                    if result == "resume":
                        continue
                    elif result == "restart":
                        return "restart"
                    elif result == "menu":
                        return "menu"
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
    # main_menu()
    
    # while True:
    #     result = main()
    #     if result == "restart":
    #         continue
    #     else:
    #         break

    while True:
        main_menu()
        result = main()

        if result == "restart":
            continue
        elif result == "menu":
            continue
        else:
            break
# MENU → GAME → GAME OVER → RESTART → GAME → GAME OVER → RESTART ...