from settings import *
from pygame.sprite import Group
from Utils.Paddle import Paddle

class Player ( Paddle ):
	def __init__(self, *groups: Group) -> None:
		super().__init__(SIZE['paddle'], COLORS['paddle'], *groups, center = POS['player'])

		self.speed = SPEED['player']

	def _get_direction ( self ):
		keys = pygame.key.get_pressed()
		self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

