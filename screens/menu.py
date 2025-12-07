from settings import *
import pygame

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