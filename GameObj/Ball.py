from settings import *
from typing import Callable, Literal
from pygame import FRect, Surface
from pygame.typing import ColorLike
from pygame.sprite import Group
from Utils.Paddle import Paddle
from Utils.Shape import Shape
from Utils.Helper import get_random_vector, pipe

UpdateScore = Callable[[Literal['player', 'opponent']], None]

class Ball ( Shape ):
	def __init__(self, update_score: UpdateScore, dimensions: tuple[int, int], color: ColorLike, *groups: Group) -> None:
		super().__init__('circle', dimensions, color, groups[0], shadowed = True, center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2) )

		self.paddle_sprites = groups[1]
		
		self.old_rect =  self.rect.copy()

		self.direction = get_random_vector()

		self.update_score = update_score
		
		self.can_play = False
		self.cooldown = 1000
		self.start_cooldown = pygame.time.get_ticks()


	def __has_reached_top ( self ): return self.rect.top < 0
	def __has_reached_bottom ( self ): return self.rect.bottom > WINDOW_HEIGHT
	def __has_reached_left ( self ): return self.rect.left < 0
	def __has_reached_right ( self ): return self.rect.right > WINDOW_WIDTH


	def __set_boundaries_bounce ( self ):
		if self.__has_reached_top(): 
			self.rect.top = 0
			self.__bounce('y')

		if self.__has_reached_bottom(): 
			self.rect.bottom = WINDOW_HEIGHT
			self.__bounce('y')

		if self.__has_reached_left(): 
			self.rect.left = 0
			self.__scoring_handler('player')

		if self.__has_reached_right(): 
			self.rect.right = WINDOW_WIDTH
			self.__scoring_handler('opponent')

	def __bounce ( self, direction: Literal[ 'x', 'y' ] ):
		if direction == 'x': self.direction.x *= -1
		if direction == 'y': self.direction.y *= -1

	def __scoring_handler ( self, whom: Literal[ 'player', 'opponent' ] ):
		self.can_play = False
		self.start_cooldown = pygame.time.get_ticks()
		self.rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
		self.update_score(whom)

	def __is_right_paddle ( self, paddle: Paddle ):
		return self.rect.right >= paddle.rect.left and self.old_rect.right <= paddle.old_rect.left

	def __is_left_paddle ( self, paddle: Paddle ):
		return self.rect.left <= paddle.rect.right and self.old_rect.left >= paddle.old_rect.right

	def __is_on_top_of_paddle ( self, paddle: Paddle ):
		return self.rect.top <= paddle.rect.bottom and self.old_rect.top >= paddle.old_rect.bottom

	def __is_bottom_of_paddle ( self, paddle: Paddle ):
		return self.rect.bottom >= paddle.rect.top and self.old_rect.bottom <= paddle.old_rect.top

	def __paddle_collision_handler ( self, direction: str ):
		for paddle in self.paddle_sprites:
			if paddle.rect.colliderect(self.rect):
				if direction == 'horizontal':
					if self.__is_right_paddle(paddle):
						self.rect.right = paddle.rect.left
						self.__bounce('x')

					if self.__is_left_paddle(paddle):
						self.rect.left = paddle.rect.right
						self.__bounce('x')


				if direction == 'vertical':
					if self.__is_on_top_of_paddle(paddle):
						self.rect.top = paddle.rect.bottom
						self.__bounce('y')

					if self.__is_bottom_of_paddle(paddle):
						self.rect.bottom = paddle.rect.top
						self.__bounce('y')

	def __yes_you_can_play_now ( self, current: int ): return current - self.start_cooldown >= self.cooldown

	def __can_i_play_now ( self ):
		if self.__yes_you_can_play_now(pygame.time.get_ticks()):
			self.can_play = True
			self.direction = get_random_vector()


	def __move ( self, dt: float ):
		self.rect.x += self.direction.x * SPEED['ball'] * dt 
		self.__paddle_collision_handler('horizontal')

		self.rect.y += self.direction.y * SPEED['ball'] * dt 
		self.__paddle_collision_handler('vertical')


	def __update_old_rect ( self ): self.old_rect = self.rect.copy()


	def update ( self, dt: float ):
		if not self.can_play: return self.__can_i_play_now()
		self.__set_boundaries_bounce()
		self.__move(dt)
		self.__update_old_rect()