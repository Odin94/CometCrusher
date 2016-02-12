import random




class Particles():
	def __init__(self, x, y, color):
		self.removepls = False
		self.color = color

		self.particles = []

		self.age = 0
		self.agecap = random.randint(30, 90) 

		for i in range(random.randint(12, 24)):
			self.particles.append(Particle(x, y))


	def move(self):
		for p in self.particles:
			p.move()

	def update(self):
		self.move()
		self.age += 1

		if self.age >= self.agecap:
			self.removepls = True

class Particle():
	def __init__(self, x, y):
		self.x = x
		self.y = y

		self.velx = random.randint(-16, 16)
		self.vely = random.randint(-16, 16)


	def move(self):
		self.x += self.velx
		self.y += self.vely