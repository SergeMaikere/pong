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
		self.rect: FRect = self.__get_frect(self.image, **rect_pos)

	def __get_surface (self, dimensions: tuple[float, float]): 
		return pygame.Surface(dimensions)

	def __set_surface_color ( self, color, surface ):
		surface.fill(color)
		return surface

	def __set_surface ( self, dimensions: tuple[float, float], color ) -> Surface:
		return pipe( 
			self.__get_surface, 
			partial(self.__set_surface_color, color)
		)(dimensions)

	def __get_frect ( self, surface: Surface, **rect_pos: tuple[float, float] ) -> FRect:
		return surface.get_frect(**rect_pos)

