import random

class Enemy():
	def __init__(self):
		self.x = random.randint(100, 800)
		
		if random.randint(0,1) == 1:
			self.y = -16
		else:
			self.y = 16

		self.vely = random.randint(1, 2)
		self.velx = random.randint(4, 8)

		self.radius = random.randint(12, 20)

		self.color = (random.randint(50, 200), random.randint(0, 200), random.randint(0, 200))

	def move(self):
		self.x += self.velx
		self.y += self.vely

	def update(self):
		if self.x >= 750:
			if self.velx > 0:
				self.velx = -self.velx
		elif self.x <= 50:
			if self.velx < 0:
				self.velx = -self.velx

		self.move()