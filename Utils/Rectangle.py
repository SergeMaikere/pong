from settings import *
from pygame import Surface, surface
from pygame.typing import ColorLike
from pygame.sprite import Group

class Rectangle ( pygame.sprite.Sprite ):
	def __init__(self, pos: tuple[float, float], dimensions: tuple[int, int], color: ColorLike, *groups: Group) -> None:
		super().__init__(*groups)

		self.image = self.__get_surface(dimensions, color)
		self.rect = self.__get_frect(self.image, pos)

	def __get_surface ( self, dimensions: tuple[int, int], color: ColorLike ):
		surface = pygame.Surface(dimensions)
		surface.fill(color)
		return surface

	def __get_frect ( self, surface: Surface, pos: tuple[float, float] ):
		frect = surface.get_frect()
		frect.topleft = pos
		return frect
