from Bullet import Bullet

class Player():
	def __init__(self):
		self.x = 300
		self.y = 450

		self.velx = 0
		self.vely = 0

		self.moving = "No"

		self.bullets = []

	def move(self):
		self.x += self.velx
		self.y += self.vely

	def shoot(self):
		self.bullets.append(Bullet(self.x, self.y-32))

	def update(self):
		if self.moving == "r":
			self.velx = 7
		elif self.moving == "l":
			self.velx = -7
		else:
			self.velx = 0

		self.move()
		for b in self.bullets:
			b.update()