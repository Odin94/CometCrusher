import random

class Bullet():
	def __init__(self, x, y):
		self.x = x
		self.y = y

		self.vely = -10
		self.velx = random.uniform(0.7, -0.7)

	def move(self):
		self.y += self.vely
		self.x += self.velx

	def update(self):
		self.move()