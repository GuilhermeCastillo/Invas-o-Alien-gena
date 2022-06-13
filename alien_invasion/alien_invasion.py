import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien

def run_game():
	# Inicializa o jogo e cria um objeto para a tela
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# Cria uma espaçonave
	ship = Ship(ai_settings, screen)
	
	# Cria um grupo no qual serão armazenados os projéteis bullets = Group()
	bullets = Group()
	aliens = Group()
	
	# Define a cor de fundo
	bg_color = (230, 230, 230)
	
	# Cria uma frota de alienígenas
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	# Cria um alienígena
	# ~alien = Alien(ai_settings, screen)
	
	# Inicia o laço principal do jogo
	while True:
		# Observa eventos 
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)
		
run_game()
