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
	
	# Cria um alienígena
	alien = Alien(ai_settings, screen)
	
	# Cria um grupo no qual serão armazenados os projéteis bullets = Group()
	bullets = Group()
	aliens = Group()
	
	# Cria uma frota de alienígenas
	gf.create_fleet(ai_settings, screen, ship, aliens)
	
	# Define a cor de fundo
	bg_color = (230, 230, 230)
	
	# Inicia o laço principal do jogo
	while True:
		# Observa eventos 
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
		gf.update_aliens(ai_settings, aliens)
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)
		
run_game()
