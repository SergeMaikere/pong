from pygame import FRect, Surface
from settings import *
from pygame.sprite import Group
from Utils.Helper import get_random_vector

class Ball ( pygame.sprite.Sprite ):
	def __init__(self, *groups: Group) -> None:
		super().__init__(*groups)

		self.__dimensions = SIZE['ball']
		self.image: Surface = pygame.Surface((self.__dimensions), pygame.SRCALPHA)
		self.rect: FRect = self.__get_rect()

		self.direction = get_random_vector()


	def __draw_circle ( self ):
		pygame.draw.circle(
			self.image, 
			COLORS['ball'], 
			pygame.Vector2(self.__dimensions) / 2,
			self.__dimensions[0] / 2
		)

	def __get_rect ( self ):
		self.__draw_circle()
		return self.image.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

	def __has_reached_top ( self ): return self.rect.top < 0
	def __has_reached_bottom ( self ): return self.rect.bottom > WINDOW_HEIGHT
	def __has_reached_left ( self ): return self.rect.left < 0
	def __has_reached_right ( self ): return self.rect.right > WINDOW_WIDTH


	def __set_direction ( self ):
		if self.__has_reached_top(): 
			self.rect.top = 0
			self.direction = self.direction.reflect(pygame.Vector2(0, 1))

		if self.__has_reached_bottom(): 
			self.rect.bottom = WINDOW_HEIGHT
			self.direction = self.direction.reflect(pygame.Vector2(0, -1))

		if self.__has_reached_left(): 
			self.rect.left = 0
			self.direction = self.direction.reflect(pygame.Vector2(1, 0))

		if self.__has_reached_right(): 
			self.rect.right = WINDOW_WIDTH
			self.direction = self.direction.reflect(pygame.Vector2(-1, 0))

	def __move ( self, dt: float ):
		self.rect.center += self.direction * SPEED['ball'] * dt 

	def update ( self, dt: float ):
		self.__set_direction()
		self.__move(dt)