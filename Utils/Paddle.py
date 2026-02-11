from settings import *
from functools import partial
from pygame import Surface
from pygame.sprite import Group
from pygame.typing import ColorLike
from Utils.Shape import Shape
from Utils.Helper import pipe

class Paddle ( Shape ):
	def __init__(self, dimensions: tuple[int, int], color: ColorLike, *groups: Group, **rect_pos: tuple[float, float]) -> None:
		super().__init__('rectangle', dimensions, color, *groups, shadowed = True, **rect_pos)
		
		self.direction = pygame.Vector2()
		self.speed = 100
		self.old_rect = self.rect.copy()

	def _set_surface(self, dimensions: tuple[int, int], color: ColorLike) -> Surface:
		return pipe(
			self._make_surface,
			partial(self._draw_rectangle, color)
		)(dimensions)

	def _set_shadow_surface ( self, dimensions: Dimensions ) -> Surface: 
		return self._draw_rectangle( COLORS['shadow'], self.image.copy() )

	def _update_old_rect ( self ): self.old_rect.y = self.rect.y

	def _get_direction ( self ):
		pass

	def _move ( self, dt: float ):
		self.rect.center += self.direction * self.speed * dt

	def _stay_inside_boundaries ( self ):
		if self.rect.top < 0: self.rect.top = 0
		if self.rect.bottom > WINDOW_HEIGHT: self.rect.bottom = WINDOW_HEIGHT

	def update ( self, dt: float ):
		self._get_direction()
		self._stay_inside_boundaries()
		self._move(dt)
		self._update_old_rect()