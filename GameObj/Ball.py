from settings import *
from pygame import FRect, Surface
from pygame.sprite import Group
from Utils.Paddle import Paddle
from Utils.Helper import get_random_vector, pipe

class Ball ( pygame.sprite.Sprite ):
	def __init__(self, *groups: Group) -> None:
		super().__init__(*groups)

		self.paddle_sprites = groups[1]

		self.__dimensions = SIZE['ball']
		
		self.image: Surface = pygame.Surface((self.__dimensions), pygame.SRCALPHA)
		self.rect: FRect = pipe( self.__draw_circle, self.__get_rect )(self.image)
		self.old_rect =  self.rect.copy()

		self.direction = get_random_vector()


	def __draw_circle ( self, image: Surface ):
		pygame.draw.circle(
			image, 
			COLORS['ball'], 
			pygame.Vector2(self.__dimensions) / 2,
			self.__dimensions[0] / 2
		)
		return image

	def __get_rect ( self, image: Surface ):
		return image.get_frect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

	def __has_reached_top ( self ): return self.rect.top < 0
	def __has_reached_bottom ( self ): return self.rect.bottom > WINDOW_HEIGHT
	def __has_reached_left ( self ): return self.rect.left < 0
	def __has_reached_right ( self ): return self.rect.right > WINDOW_WIDTH


	def __set_boundaries_bounce ( self ):
		if self.__has_reached_top(): 
			self.rect.top = 0
			self.direction.y *= -1

		if self.__has_reached_bottom(): 
			self.rect.bottom = WINDOW_HEIGHT
			self.direction.y *= -1

		if self.__has_reached_left(): 
			self.rect.left = 0
			self.direction.x *= -1

		if self.__has_reached_right(): 
			self.rect.right = WINDOW_WIDTH
			self.direction.x *= -1

	def __is_on_my_right ( self, paddle: Paddle ):
		return self.rect.right > paddle.rect.left and self.old_rect.right <= paddle.old_rect.left

	def __is_on_my_left ( self, paddle: Paddle ):
		return self.rect.left < paddle.rect.right and self.old_rect.left >= paddle.old_rect.right

	def __is_on_top_of_me ( self, paddle: Paddle ):
		return self.rect.top < paddle.rect.bottom and self.old_rect.top >= paddle.old_rect.bottom

	def __is_under_me ( self, paddle: Paddle ):
		return self.rect.bottom > paddle.rect.top and self.old_rect.bottom <= paddle.old_rect.top


	def __paddle_collision_handler ( self, direction: str ):
		for paddle in self.paddle_sprites:
			if paddle.rect.colliderect(self.rect):
				if direction == 'horizontal':
					if self.__is_on_my_right(paddle):
						self.rect.right = paddle.rect.left
						self.direction.x *= -1

					if self.__is_on_my_left(paddle):
						self.rect.left = paddle.rect.right
						self.direction.x *= -1


				if direction == 'vertical':
					if self.__is_on_top_of_me(paddle):
						self.rect.top = paddle.rect.bottom
						self.direction.x *= -1

					if self.__is_under_me(paddle):
						self.rect.bottom = paddle.rect.top
						self.direction.x *= -1



	def __move ( self, dt: float ):
		self.rect.x += self.direction.x * SPEED['ball'] * dt 
		self.__paddle_collision_handler('horizontal')

		self.rect.y += self.direction.y * SPEED['ball'] * dt 
		self.__paddle_collision_handler('vertical')


	def update ( self, dt: float ):
		self.__set_boundaries_bounce()
		self.__move(dt)