from settings import *
import pygame

def pause_screen():
    run = True

    
    resume_button = pygame.Rect(WIDTH//2 - 120, HEIGHT//2 - 30, 240, 60)
    restart_button = pygame.Rect(WIDTH//2 - 120, HEIGHT//2 + 50, 240, 60)
    menu_button = pygame.Rect(WIDTH//2 - 120, HEIGHT//2 + 130, 240, 60)

    while run:
        WIN.blit(BG, (0, 0))

        pause_text = TITLE_FONT.render("PAUSED", 1, WHITE)
        WIN.blit(pause_text, (WIDTH//2 - pause_text.get_width()//2, 150))

        mouse_pos = pygame.mouse.get_pos()

        # RESUME button
        if resume_button.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            pygame.draw.rect(WIN, (200,0,0), resume_button)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            pygame.draw.rect(WIN, RED, resume_button)

        resume_text = BUTTON_FONT.render("RESUME", 1, WHITE)
        WIN.blit(resume_text, (
            resume_button.x + (resume_button.width - resume_text.get_width())//2,
            resume_button.y + (resume_button.height - resume_text.get_height())//2
        ))

        # RESTART button
        if restart_button.collidepoint(mouse_pos):
            pygame.draw.rect(WIN, (200,0,0), restart_button)
        else:
            pygame.draw.rect(WIN, RED, restart_button)

        restart_text = BUTTON_FONT.render("RESTART", 1, WHITE)
        WIN.blit(restart_text, (
            restart_button.x + (restart_button.width - restart_text.get_width())//2,
            restart_button.y + (restart_button.height - restart_text.get_height())//2
        ))

        # MENU button
        if menu_button.collidepoint(mouse_pos):
            pygame.draw.rect(WIN, (200,0,0), menu_button)
        else:
            pygame.draw.rect(WIN, RED, menu_button)

        menu_text = BUTTON_FONT.render("MENU", 1, WHITE)
        WIN.blit(menu_text, (
            menu_button.x + (menu_button.width - menu_text.get_width())//2,
            menu_button.y + (menu_button.height - menu_text.get_height())//2
        ))

        # EVENTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if resume_button.collidepoint(event.pos):
                    return "resume"
                if restart_button.collidepoint(event.pos):
                    return "restart"
                if menu_button.collidepoint(event.pos):
                    return "menu"

        pygame.display.update()