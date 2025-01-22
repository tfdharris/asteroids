import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circle import CircleShape

class Asteroid(CircleShape):
	def __init__(self, x, y, radius, velocity):
		super().__init__(x, y, radius)
		self.velocity = velocity
	def draw(self, screen):
		pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, 2)
	def update(self, dt):
		self.position += self.velocity * dt
	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return
		random_angle = random.uniform(20, 50)
		velocity_vector_1 = self.velocity.rotate(random_angle)
		velocity_vector_2 = self.velocity.rotate(-random_angle)
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		x, y = self.position.x, self.position.y
		new_asteroid_1 = Asteroid(x, y, new_radius, velocity_vector_1 * 1.2)
		new_asteroid_2 = Asteroid(x, y, new_radius, velocity_vector_2 * 1.2)
		for group in self.groups():
			group.add(new_asteroid_1, new_asteroid_2)		