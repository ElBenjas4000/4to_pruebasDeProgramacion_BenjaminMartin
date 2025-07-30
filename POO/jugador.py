import pygame, random

width = 700
height = 550
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, posy):
		super().__init__()
		self.image = pygame.image.load("POO/assets/laser1.png")
		self.image.set_colorkey(black)
		self.image = pygame.transform.rotate(self.image, 90)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.centerx = x
		self.rect.centery = posy
		
		self.speedx = -10	

	def update(self):
		self.rect.x += self.speedx
		if self.rect.bottom < 0:
			self.kill()

class Player(pygame.sprite.Sprite):
	def __init__(self, img_jugador, posy, posx, type_moven):
		super().__init__()
		self.image = pygame.image.load(f"POO/img/sprite/personaje{img_jugador}.webp")
		self.image.set_colorkey(black)
		self.image = pygame.transform.scale(self.image, (100, 60))
		self.rect = self.image.get_rect()
		self.rect.centerx = width // 2
		self.rect.bottom = posy
		self.rect.left = posx
		self.shield = 100

		self.type_moven = type_moven

	def update(self):
		self.speed_x = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_a] and self.type_moven == 1:
			self.speed_x = -10
		if keystate[pygame.K_d] and self.type_moven == 1:
			self.speed_x = 10

		if keystate[pygame.K_LEFT] and self.type_moven == 2:
			self.speed_x = -10
		if keystate[pygame.K_RIGHT] and self.type_moven == 2:
			self.speed_x = 10
		self.rect.x += self.speed_x
		if self.rect.right > width:
			self.rect.right = width
		if self.rect.left < 0:
			self.rect.left = 0

	def shoot(self, all_sprites, bullets):
		bullet = Bullet(self.rect.left, self.rect.centery)
		all_sprites.add(bullet)
		bullets.add(bullet)


class Explosion(pygame.sprite.Sprite):
	def __init__(self, center):
		super().__init__()
		self.image = explosion_anim[0]
		self.rect = self.image.get_rect()
		self.rect.center = center 
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 50 #Velocidad de animacion de explosion 
	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1
			if self.frame == len(explosion_anim):
				self.kill()
			else:
				center = self.rect.center
				self.image = explosion_anim[self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center

