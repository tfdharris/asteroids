import pygame
from circle import CircleShape
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN
from shot import Shot

class Player(CircleShape):
	def __init__(self, x, y, shots_group):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shots_group = shots_group
		self.cooldown_timer = 0
	def triangle(self):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
		a = self.position + forward * self.radius
		b = self.position - forward * self.radius - right
		c = self.position - forward * self.radius + right
		return [a, b, c]
	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), 2)
	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt
	def update(self, dt):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
 			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_SPACE]:
			self.shoot()
		if self.cooldown_timer > 0:
			self.cooldown_timer -= dt
	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt
	def shoot(self):
		if self.cooldown_timer <= 0:
			velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
			new_shot = Shot(self.position.x, self.position.y, velocity)
			self.shots_group.add(new_shot)
			self.cooldown_timer += PLAYER_SHOOT_COOLDOWN