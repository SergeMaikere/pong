from settings import *
from pygame import FRect, Surface
from pygame.typing import ColorLike
from pygame.sprite import Group
from Utils.Helper import pipe
from functools import partial


class Rectangle ( pygame.sprite.Sprite ):
	def __init__(self, dimensions: tuple[int, int], color: ColorLike, *groups: Group, **rect_pos: tuple[float, float]) -> None:
		super().__init__(*groups)

		self.image: Surface = self.__set_surface(dimensions, color)
		self.rect: FRect = self.image.get_frect(**rect_pos)


	def __set_surface_color ( self, color, surface ):
		surface.fill(color)
		return surface

	def __set_surface ( self, dimensions: tuple[float, float], color ) -> Surface:
		return pipe( 
			lambda dims: pygame.Surface(dims), 
			partial(self.__set_surface_color, color)
		)(dimensions)

