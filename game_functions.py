import pygame
from pygame import sprite
import time
from ball import Ball


def updateScreen(screen, settings, board, balls):
	screen.fill(settings.bgColor)
	board.draw()
	balls.draw(screen)
	pygame.display.update()


def updateBoard(board):
	board.update()


def updateBalls(settings, screen, balls, board, nofBalls):

	createBalls(settings, screen, balls, nofBalls)
	checkBallBoard(balls, board)
	checkBallEdges(balls)
	balls.update()


def checkBallBoard(balls, board):
	for ball in balls:
		if checkBallBetweenBoard(ball, board):
			ball.changeDirectionY()



def checkBallEdges(balls):
	for ball in balls:
		if ball.rect.top < 0:
			ball.changeDirectionY()
		elif ball.rect.right > ball.screenRect.right:
			ball.changeDirectionX()
		elif ball.rect.left < 0:
			ball.changeDirectionX()
		elif ball.rect.top > ball.screenRect.bottom:
			ball.remove(balls)


def createBalls(settings, screen, balls, nofBalls):
	"""Create multiple balls"""
	if len(balls) < nofBalls:
		ball = Ball(settings, screen)
		balls.add(ball)


def checkBallBetweenBoard(ball, board):
	if (ball.rect.right > (board.rect.left - ball.hw) and
		ball.rect.left < (board.rect.right + ball.hw) and
		ball.rect.bottom == board.rect.top):
		return True
	else:
		return False

