import pygame
from pygame.sprite import Sprite
from pygame.locals import *


class Board(Sprite):

	def __init__(self, screen, settings):
		super().__init__()
		self.screen = screen
		self.settings = settings
		self.screenRect = self.screen.get_rect()

		self.image = pygame.image.load('board.png').convert_alpha()
		self.rect = self.image.get_rect()

		self.rect.centerx = self.screenRect.centerx
		self.rect.bottom = self.screenRect.bottom - 10
		self.x = float(self.rect.x)

	def update(self):
		k = pygame.key.get_pressed()
		if k[K_RIGHT] and self.rect.right < self.screenRect.right:
			self.x += self.settings.boardSpeed
		elif k[K_LEFT] and self.rect.left > 0:
			self.x -= self.settings.boardSpeed

		self.rect.x = self.x

	def draw(self):
		self.screen.blit(self.image, self.rect)
