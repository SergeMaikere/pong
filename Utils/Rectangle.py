from settings import *
from typing import Callable
from pygame import FRect, Surface
from pygame.typing import ColorLike
from pygame.sprite import Group
from Utils.Helper import pipe
from functools import partial


class Rectangle ( pygame.sprite.Sprite ):
	def __init__(self, pos: tuple[float, float], dimensions: tuple[int, int], color: ColorLike, *groups: Group) -> None:
		super().__init__(*groups)

		self.image = self.__set_surface(dimensions, color)
		self.rect = self.__set_frect(self.image, pos)

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

	def __get_frect ( self, surface: Surface ) -> FRect:
		return surface.get_frect()

	def __set_frect_pos ( self, pos: tuple[float, float], frect: FRect ) -> FRect:
		frect.topleft = pos
		return frect

	def __set_frect ( self,  surface: Surface, pos: tuple[float, float] ):
		return pipe(
			self.__get_frect,
			partial(self.__set_frect_pos, pos)
		)(surface)
