import pygame
import sys
from Checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE
from Checkers.game import Game
from minimax.algorithm import minimax
from pygame.locals import *
from PvP.gamepvp import Gamepvp

pygame.init()

font = pygame.font.SysFont(None, 40)
font_2 = pygame.font.SysFont(None, 60, bold=True)
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    click = False
    clock = pygame.time.Clock()
    while True:

        clock.tick(FPS)

        WIN.fill((64, 64, 64))

        mx, my = pygame.mouse.get_pos()

        draw_text('CHECKERS', font_2, (255, 255, 255), WIN, 265, 200)

        button_1 = pygame.Rect(275, 290, 250, 50)
        butt_1 = pygame.Rect(270, 285, 260, 60)
        pygame.draw.rect(WIN, (32, 32, 32), butt_1)
        pygame.draw.rect(WIN, (109, 109, 98), button_1)
        draw_text('Player vs AI', font, (255, 255, 255), WIN, 320, 300)
        button_2 = pygame.Rect(275, 350, 250, 50)
        butt_2 = pygame.Rect(270, 345, 260, 60)
        pygame.draw.rect(WIN, (32, 32, 32), butt_2)
        pygame.draw.rect(WIN, (109, 109, 98), button_2)
        draw_text('Player vs Player', font, (255, 255, 255), WIN, 295, 360)
        button_3 = pygame.Rect(275, 410, 250, 50)
        butt_3 = pygame.Rect(270, 405, 260, 60)
        pygame.draw.rect(WIN, (32, 32, 32), butt_3)
        pygame.draw.rect(WIN, (109, 109, 98), button_3)
        draw_text('Quit', font, (255, 255, 255), WIN, 370, 420)
        if button_1.collidepoint((mx, my)):
            if click:
                ai()
        if button_2.collidepoint((mx, my)):
            if click:
                pvp()
        if button_3.collidepoint((mx, my)):
            if click:
                pygame.quit()

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()


def ai():
    click = False
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)

        if game.winner() is not None:
            print(game.winner())
            main_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()

        game.update()

    pygame.quit()


def pvp():
    run = True
    clock = pygame.time.Clock()
    game = Gamepvp(WIN)

    while run:
        clock.tick(FPS)

        if game.winner() is not None:
            print(game.winner())
            main_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    main_menu()

        game.update()

    pygame.quit()


main_menu()
