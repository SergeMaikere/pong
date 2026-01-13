from settings import *
from pygame.sprite import Group
from pygame.typing import ColorLike
from Utils.Rectangle import Rectangle

class Paddle ( Rectangle ):
	def __init__(self, dimensions: tuple[int, int], color: ColorLike, *groups: Group, **rect_pos: tuple[float, float]) -> None:
		super().__init__(dimensions, color, *groups, **rect_pos)

		self.direction = pygame.Vector2()
		self.speed = 100
		self.old_rect = self.rect.copy()

	def _update_old_rect ( self ):
		self.old_rect = self.rect.copy()

	def _get_direction ( self ):
		pass

	def _move ( self, dt: float ):
		self.rect.center += self.direction * self.speed * dt

	def _stay_inside_boundaries ( self ):
		if self.rect.top < 0: self.rect.top = 0
		if self.rect.bottom > WINDOW_HEIGHT: self.rect.bottom = WINDOW_HEIGHT

	def update ( self, dt: float ):
		self._update_old_rect()
		self._get_direction()
		self._stay_inside_boundaries()
		self._move(dt)