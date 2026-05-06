import pygame, sys, random

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("LOGIN")

base_font = pygame.font.Font(None, 28)
min_year = 1900
max_year = 2025
months = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
min_month = 1
max_month = 12
min_day = 1
max_day = 31
day = ''
year = ''
month_num = 0
month = ''
name = ''
email = ''
date = ''
default = 'Name'
default2 = 'Email'
default3 = 'Date of Birth'
button_text = 'Earlier'
button_text2 = 'Later'
button_text3 = 'Right'

input_rect = pygame.Rect(250, 200, 300, 32)
input_rect2 = pygame.Rect(250, 300, 300, 32)
input_rect3 = pygame.Rect(250, 400, 300, 32)
button = pygame.Rect(125, 390, 100, 50)
button2 = pygame.Rect(575, 390, 100, 50)
button3 = pygame.Rect(350, 457, 100, 50)
color = (50, 50, 50)

active = False
active2 = False
active3 = False
waiting = False
all_green = False
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                default = ''
                active = True
                active2 = False
                active3 = False
                if email == '':
                    default2 = 'Email'
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect2.collidepoint(event.pos):
                default2 = ''
                active = False
                active2 = True
                active3 = False
                if name == '':
                    default = 'Name'
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect3.collidepoint(event.pos):
                default3 = ''
                active = False
                active2 = False
                active3 = True
                if name == '':
                    default = 'Name'
                if email == '':
                    default2 = 'Email'

        if active3:
            if not waiting:
                year = str(random.randint(min_year, max_year))
                month_num = random.randint(min_month, max_month)
                month = months.get(month_num)
                if min_month != max_month:
                    if month_num == 1 or month_num == 3 or month_num == 5 or month_num == 7 or month_num == 8 or month_num == 10 or month_num == 12:
                        max_day = 31
                    elif month_num == 2 or month_num == 4 or month_num == 6 or month_num == 9 or month_num == 11:
                        max_day = 30
                    if month_num == 2:
                        if int(year) % 4 == 0:
                            max_day = 29
                        else:
                            max_day = 28
                day = str(random.randint(min_day, max_day))
                waiting = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if min_month == max_month:
                    if button.collidepoint(event.pos):
                        max_day = int(day)
                        waiting = False
                    elif button2.collidepoint(event.pos):
                        min_day = int(day)
                        waiting = False
                elif min_year != max_year:
                    if button.collidepoint(event.pos):
                        max_year = int(year)
                        waiting = False
                    elif button2.collidepoint(event.pos):
                        min_year = int(year)
                        waiting = False
                elif min_year == max_year:
                    if button.collidepoint(event.pos):
                        max_month = month_num
                        waiting = False
                    elif button2.collidepoint(event.pos):
                        min_month = month_num
                        waiting = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button3.collidepoint(event.pos):
                all_green = True
                active3 = False
                waiting = False

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
            if active2:
                if event.key == pygame.K_BACKSPACE:
                    email = email[:-1]
                else:
                    email += event.unicode

    screen.fill((240, 240, 240))

    pygame.draw.rect(screen, color, input_rect, 2)
    pygame.draw.rect(screen, color, input_rect2, 2)
    pygame.draw.rect(screen, color, input_rect3, 2)

    name_text = base_font.render(name, True, (0, 0, 0))
    email_text = base_font.render(email, True, (0, 0, 0))
    day_color = (0, 150, 0) if min_day == max_day or all_green else (0, 0, 0)
    day_text = base_font.render(day, True, day_color)
    month_color = (0, 150, 0) if min_month == max_month or all_green else (0, 0, 0)
    month_text = base_font.render(month, True, month_color)
    year_color = (0, 150, 0) if min_year == max_year or all_green else (0, 0, 0)
    year_text = base_font.render(year, True, year_color)
    text_surface4 = base_font.render(default, True, (100, 100, 100))
    text_surface5 = base_font.render(default2, True, (100, 100, 100))
    text_surface6 = base_font.render(default3, True, (100, 100, 100))

    x = input_rect3.x + 7
    y = input_rect3.y + 7

    screen.blit(name_text, (input_rect.x + 7, input_rect.y + 7))
    screen.blit(email_text, (input_rect2.x + 7, input_rect2.y + 7))
    screen.blit(day_text, (x, y))
    x += day_text.get_width() + 5
    screen.blit(month_text, (x, y))
    x += month_text.get_width() + 5
    screen.blit(year_text, (x, y))
    screen.blit(text_surface4, (input_rect.x + 7, input_rect.y + 7))
    screen.blit(text_surface5, (input_rect2.x + 7, input_rect2.y + 7))
    screen.blit(text_surface6, (input_rect3.x + 7, input_rect3.y + 7))

    if active3:
        pygame.draw.rect(screen, (200, 200, 200), button)
        pygame.draw.rect(screen, (200, 200, 200), button2)
        pygame.draw.rect(screen, (200, 200, 200), button3)
        text_surface7 = base_font.render(button_text, True, (0, 0, 0))
        text_surface8 = base_font.render(button_text2, True, (0, 0, 0))
        text_surface9 = base_font.render(button_text3, True, (0, 0, 0))
        screen.blit(text_surface7, (button.x + 15, button.y + 15))
        screen.blit(text_surface8, (button2.x + 25, button2.y + 15))
        screen.blit(text_surface9, (button3.x + 25, button3.y + 15))

    input_rect.w = max(300, name_text.get_width() + 10)
    input_rect2.w = max(300, email_text.get_width() + 10)

    pygame.display.flip()

pygame.quit()
sys.exit()
