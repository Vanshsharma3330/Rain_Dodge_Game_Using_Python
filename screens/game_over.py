from settings import *
import pygame

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