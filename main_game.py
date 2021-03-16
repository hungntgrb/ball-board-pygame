import pygame
from settings import Settings
from ball import Ball
from board import Board
from pygame.sprite import Group
import game_functions as gf

def main():

        pygame.init()

        settings = Settings()
        screen = pygame.display.set_mode((settings.screenWidth, settings.screenHeight))
        pygame.display.set_caption('Ball Board Game 01 2019.06.03')
        # ball = Ball(settings, screen)
        balls = Group()
        board = Board(screen, settings)

        run = True
        while run:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                run = False

                gf.updateBoard(board)
                gf.updateBalls(settings, screen, balls, board, 4)

                gf.updateScreen(screen, settings, board, balls)


        pygame.quit()

if __name__ == '__main__':
        main()
