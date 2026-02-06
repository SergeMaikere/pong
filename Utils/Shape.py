from typing import Literal
from settings import *
from pygame import SRCALPHA, FRect, Surface
from pygame.typing import ColorLike
from pygame.sprite import Group
from Utils.Helper import pipe
from functools import partial

ShapeType = Literal[ 'rectangle', 'circle' ]

Dimensions = tuple[int, int]

class Shape ( pygame.sprite.Sprite ):
	def __init__(self, shape_type: ShapeType, dimensions: Dimensions, color: ColorLike, *groups: Group, **rect_pos: tuple[float, float]) -> None:
		super().__init__(*groups)

		self.shape_type = shape_type
		self.shadowed = True
		
		self.image: Surface = self._set_surface(dimensions, color)
		self.rect: FRect = self.image.get_frect(**rect_pos)


	def __make_surface ( self, dims: Dimensions ) -> Surface: 
		return pygame.Surface(dims, pygame.SRCALPHA)

	def __set_surface_color ( self, color, surface ) -> Surface:
		surface.fill(color)
		return surface

	def __draw_circle ( self, dimensions: Dimensions, image: Surface ) -> Surface:
		pygame.draw.circle(
			image, 
			COLORS['ball'], 
			pygame.Vector2(dimensions) / 2,
			dimensions[0] / 2
		)
		return image

	def __make_image_rectangle ( self, dimensions: Dimensions, color: ColorLike ) -> Surface:
		return pipe( 
			self.__make_surface, 
			partial(self.__set_surface_color, color)
		)(dimensions)

	def __make_image_circle ( self, dimensions: Dimensions, color: ColorLike ) -> Surface:
		return pipe(
			self.__make_surface,
			partial(self.__draw_circle, dimensions)
		)(dimensions)

	def _set_surface ( self, dimensions: Dimensions, color: ColorLike ) -> Surface:
		if self.shape_type == 'rectangle': return self.__make_image_rectangle(dimensions, color)
		if self.shape_type == 'circle': return self.__make_image_circle(dimensions, color)
