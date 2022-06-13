class Settings():
	"""Uma classe para armanezar as configurações do jogo. """
	
	def __init__(self):
		""" Inicializa as configurações do jogo. """
		# configurações da tela
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)
		# Configurações da espaçonave
		self.ship_speed_factor = 1.5
		
		# Configurações dos projéteis
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3
		
		# Configurações dos alienígenas
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		# fleet_direction igual 1 representa a direita; -1 representa a esquerda
		self.fleet_direction = 1
