class GameStats():
	"""Armazena dados estatíticos na Invasão Alienígena."""
	
	def __init__(self, ai_settings):
		"""Inicializa os dados estatíticos"""
		self.ai_settings = ai_settings
		self.reset_stats()
		
		# Inicia a Invasão Alienígena em um estado ativo
		self.game_active = False
		
		# Pontuação máxima
		self.high_score = 0
	
	def reset_stats(self):
		"""Inicializa os dados estatíticos que podem mudar durante o 
		jogo."""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
