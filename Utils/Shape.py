from typing import Literal
from settings import *
from pygame import SRCALPHA, FRect, Surface
from pygame.typing import ColorLike
from pygame.sprite import Group
from Utils.Helper import pipe
from functools import partial

ShapeType = Literal[ 'rectangle', 'circle' ]


class Shape ( pygame.sprite.Sprite ):
	def __init__(self, shape_type: ShapeType, dimensions: Dimensions, color: ColorLike, *groups: Group, shadowed: bool = False, **rect_pos: tuple[float, float]) -> None:
		super().__init__(*groups)

		self._dimensions = dimensions
		_key, self._pos = list(rect_pos.items())[0]

		self.shadowed = shadowed
		self.shape_type = shape_type
		
		self.image: Surface = self._set_surface(self._dimensions, color)
		self.rect: FRect = self.image.get_frect(**rect_pos)

		self.shadow_images = [ self._set_shadow_surface(self._dimensions) for _i in range(5) ] if self.shadowed else None
		self.shadow_rect = self.rect.copy() if self.shadowed else None


	def _make_surface ( self, dimensions: Dimensions ): return pygame.Surface(dimensions, pygame.SRCALPHA)

	def _set_surface_color ( self, color: ColorLike, surface: Surface ) -> Surface:
		if self.shape_type == 'circle': return surface

		surface.fill(color)
		return surface

	def _draw_circle ( self, dimensions: Dimensions, color: ColorLike, image: Surface ) -> Surface:
		if self.shape_type == 'rectangle': return image

		pygame.draw.circle(
			image, 
			color, 
			pygame.Vector2(dimensions) / 2,
			dimensions[0] / 2
		)
		return image

	def _draw_rectangle(self, color: ColorLike, surface: Surface) -> Surface:
		pygame.draw.rect( surface, color, ((0, 0), self._dimensions), 0, 6 )
		return surface


	def _set_surface ( self, dimensions: Dimensions, color: ColorLike ) -> Surface:
		return pipe(
			self._make_surface,
			partial(self._set_surface_color, color),
			partial(self._draw_circle, dimensions, color)
		)(dimensions)

	def _set_shadow_surface ( self, dimensions: Dimensions ) -> Surface: 
		return pipe(
			partial(self._set_surface_color, COLORS['shadow']),
			partial(self._draw_circle, dimensions, COLORS['shadow'])
		)(self.image.copy())

	def _set_shadow_pos ( self ):
		if self.shadow_rect: self.shadow_rect = self.rect

	def _get_shadow_data ( self ) -> tuple[list[Surface] | None, FRect | None]:
		self._set_shadow_pos()
		return ( self.shadow_images, self.shadow_rect )