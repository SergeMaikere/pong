from pygame import Surface
from settings import *
from pygame.sprite import Group
from pygame.typing import ColorLike
from Utils.Helper import pipe

class Ball ( pygame.sprite.Sprite ):
	def __init__(self, *groups: Group) -> None:
		super().__init__(*groups)

		self.__radius = SIZE['ball']
		self.image: Surface = pygame.Surface((self.__radius), pygame.SRCALPHA)
		self.rect = self.__get_rect()


	def __draw_circle ( self ):
		pygame.draw.circle(
			self.image, 
			COLORS['ball'], 
			pygame.Vector2(self.__radius) / 2,
			self.__radius[0] / 2
		)

	def __get_rect ( self ):
		self.__draw_circle()
		return self.image.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))