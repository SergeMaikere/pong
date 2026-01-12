from pygame.key import ScancodeWrapper
from settings import *
from pygame.sprite import Group
from Utils.Paddle import Paddle

class Player ( Paddle ):
	def __init__(self, *groups: Group) -> None:
		super().__init__(SIZE['paddle'], COLORS['paddle'], *groups, center = POS['player'])

		self.speed = SPEED['player']

	def __get_direction ( self, keys: ScancodeWrapper ):
		self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])


	def update ( self, dt: float ):
		self._update_old_rect()
		self.__get_direction(pygame.key.get_pressed())
		self._stay_inside_boundaries()
		self._move(dt)