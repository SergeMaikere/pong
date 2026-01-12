from pygame.key import ScancodeWrapper
from settings import *
from pygame.sprite import Group
from Utils.Rectangle import Rectangle

class Player ( Rectangle ):
	def __init__(self, *groups: Group) -> None:
		super().__init__(SIZE['paddle'], COLORS['paddle'], *groups, center = POS['player'])

		self.direction = pygame.Vector2()

	def __get_direction ( self, keys: ScancodeWrapper ):
		self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])

	def __move ( self, dt: float ):
		self.rect.center += self.direction * SPEED['player'] * dt

	def __stay_inside_boundaries ( self ):
		if self.rect.top < 0: self.rect.top = 0
		if self.rect.bottom > WINDOW_HEIGHT: self.rect.bottom = WINDOW_HEIGHT


	def update ( self, dt: float ):
		self.__get_direction(pygame.key.get_pressed())
		self.__move(dt)
		self.__stay_inside_boundaries()