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
	def __init__(self, shape_type: ShapeType, dimensions: Dimensions, color: ColorLike, *groups: Group, shadowed: bool = False, **rect_pos: tuple[float, float]) -> None:
		super().__init__(*groups)

		self.shadowed = shadowed
		self.shape_type = shape_type
		
		self.image: Surface = self._set_surface(dimensions, color)
		self.rect: FRect = self.image.get_frect(**rect_pos)

		self.shadow_image = self.__set_shadow_surface(dimensions) if self.shadowed else None
		self.shadow_rect = self.rect.copy() if self.shadowed else None

	def __make_surface ( self, dims: Dimensions ) -> Surface: return pygame.Surface(dims, pygame.SRCALPHA)

	def __set_surface_color ( self, color: ColorLike, surface: Surface ) -> Surface:
		if self.shape_type == 'circle': return surface

		surface.fill(color)
		return surface

	def __draw_circle ( self, dimensions: Dimensions, color: ColorLike, image: Surface ) -> Surface:
		if self.shape_type == 'rectangle': return image

		pygame.draw.circle(
			image, 
			color, 
			pygame.Vector2(dimensions) / 2,
			dimensions[0] / 2
		)
		return image


	def _set_surface ( self, dimensions: Dimensions, color: ColorLike ) -> Surface:
		return pipe(
			self.__make_surface,
			partial(self.__set_surface_color, color),
			partial(self.__draw_circle, dimensions, color)
		)(dimensions)

	def __set_shadow_surface ( self, dimensions: Dimensions ) -> Surface: 
		return pipe(
			self.__make_surface,
			partial(self.__set_surface_color, COLORS['paddle shadow']),
			partial(self.__draw_circle, dimensions, COLORS['ball shadow'])
		)(dimensions)

	def __set_shadow_pos ( self ):

		if self.shadow_rect:
			self.shadow_rect.x = self.rect.x + 5
			self.shadow_rect.y = self.rect.y + 5

	def _get_shadow_data ( self ) -> tuple[Surface | None, FRect | None]:
		self.__set_shadow_pos()
		return ( self.shadow_image, self.shadow_rect )