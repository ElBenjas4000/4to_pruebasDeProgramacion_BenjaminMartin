import pygame, random, jugador


width = 700
height = 550
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shooter")
clock = pygame.time.Clock()

def draw_text(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, white)
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

def draw_shield_bar(surface, x, y, porcentage, color):
	bar_lenght = 100
	bar_height = 20 
	fill = (porcentage / 100) * bar_lenght
	border = pygame.Rect(x, y, bar_lenght, bar_height)
	fill = pygame.Rect(x, y, fill, bar_height)
	pygame.draw.rect(surface, color, fill)
	pygame.draw.rect(surface, white, border, 2)

def show_chus_player():
	screen.blit(background [0, 0])
	draw_text(screen, "SHOOTER 2v2", 65, width // 2, height // 5)
	draw_text(screen, "Elige tu jugador", 27, width // 2, height // 2)
	draw_text(screen, "Presiona Enter", 20, width // 2, height * 3/4)

	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					waiting = False
def show_go_screen():
	screen.blit(background, [0, 0])
	draw_text(screen, "SHOOTER 2v2", 65, width // 2, height // 2)
	draw_text(screen, "Para moverte preciona las teclas w, a, s, d y espacio para disparar", 27, width // 2, height // 2)
	draw_text(screen, "Presiona Enter", 20, width // 2, height * 3/4)
	pygame.display.flip()
	waiting = True 
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					waiting = False


def show_game_over_screen():
	screen.blit(background, [0, 0])
	draw_text(screen, f"Consguiste {score} puntos", 20, width // 2, 10)

	draw_text(screen, "Game Over", 65, width // 2, height // 4)
	draw_text(screen, "Para moverte preciona A y D y espacio para disparar", 27, width // 2, height // 2)
	draw_text(screen, "Press W", 20, width // 2, height * 3/4)
	pygame.display.flip()
	waiting = True 
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w:
					waiting = False

explosion_anim = []
for i in range(9):
	file = "POO/img/explo/regularExplosion0{}.png".format(i)
	img = pygame.image.load(file).convert()
	img.set_colorkey(black)
	img_scale = pygame.transform.scale(img, (70,70))
	explosion_anim.append(img_scale)


background = pygame.image.load("POO/img/background/background_1.jpg").convert()


comenzar = True
game_over = False
running = True

Can_vida = 4

while running:


	if comenzar:
		show_chus_player()
		comenzar = False
		all_sprites = pygame.sprite.Group()
		bullets = pygame.sprite.Group()

		player = jugador.Player(2, (height - 42), (width -100), 1)
		player2 = jugador.Player(1, (height - 42), (width -400), 2)
		all_sprites.add(player, player2)

		score = 0
		Can_vida = 4

	if game_over == True:
		show_game_over_screen()
		game_over = False
		all_sprites = pygame.sprite.Group()
		bullets = pygame.sprite.Group()

		player = jugador.Player(2, (height - 42))
		all_sprites.add(player)
		score = 0
		puntos = 0
		Can_vida = 4

	clock.tick(60)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player.shoot(all_sprites, bullets)

	all_sprites.update()

	# colisiones - meteoro - laser
	#hits = pygame.sprite.groupcollide(all_sprites, bullets, True, True)
	#for hit in hits:
	#	score += 1
	#	puntos = score
	#	explosion = Explosion(hit.rect.center)
	#	all_sprites.add(explosion)
	#	meteor = Meteor()
	#	all_sprites.add(meteor)
	#	meteor_list.add(meteor)	

	
			

	screen.blit(background, [0, 0])

	all_sprites.draw(screen)

	# Marcador
	draw_text(screen, str(score), 25, width // 2, 10)

	draw_text(screen, str(Can_vida), 25, 120, 2)

	draw_text(screen, str(Can_vida), 25, 580, 2)

	# Vida
	draw_shield_bar(screen, 5, 5, player.shield, red)

	draw_shield_bar(screen, 595, 5, player.shield, green)

	pygame.display.flip()
pygame.quit() 
