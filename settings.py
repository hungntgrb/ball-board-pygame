from random import randint as rd


class Settings:
	def __init__(self):
		self.screenWidth = 1200
		self.screenHeight = 700
		self.bgColor = (130, rd(0, 255), rd(0, 255))
		self.resetSettings()
		# self.changeDirection = -1

	def resetSettings(self):
		self.boardSpeed = 2
		self.ballSpeedX = 1
		self.ballSpeedY = 1

	def increaseGameSpeed(self):
		self.speedFactor = 1.1