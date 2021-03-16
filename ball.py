import pygame
from pygame.sprite import Sprite
from random import randint, choice
import os


class Ball(Sprite):

	def __init__(self, settings, screen):
		super().__init__()
		self.screen = screen
		self.settings = settings
		self.screenRect = self.screen.get_rect()

		ball_list = [f'ball{i}.png' for i in range(1, 7)]
		ball_path = os.path.join('img', choice(ball_list))
		self.image = pygame.image.load(ball_path).convert_alpha()
		self.rect = self.image.get_rect()

		self.rect.top = 0
		self.rect.x = randint(0, self.settings.screenWidth - self.rect.width)
		self.y = float(self.rect.y)
		self.x = float(self.rect.x)

		self.speedX = self.settings.ballSpeedX
		self.speedY = self.settings.ballSpeedY
		self.directionX = choice([-1, 1])
		self.changeDirection = -1

		self.hw = self.rect.width / 2

	def update(self):
		self.y += self.speedY

		self.x += self.speedX * self.directionX

		self.rect.y = self.y
		self.rect.x = self.x

	def draw(self):
		self.screen.blit(self.image, self.rect)

	def changeDirectionX(self):
		self.speedX *= self.changeDirection

	def changeDirectionY(self):
		self.speedY *= self.changeDirection