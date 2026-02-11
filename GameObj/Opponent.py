from GameObj.Ball import Ball
from settings import *
from pygame.sprite import Group
from Utils.Paddle import Paddle

class Opps ( Paddle ):
	def __init__(self, ball: Ball, *groups: Group) -> None:
		super().__init__(SIZE['paddle'], COLORS['paddle'], *groups, center = POS['opponent'])

		self.speed = SPEED['opponent']
		self.ball = ball

	def _get_direction(self):
		if self.ball.can_play: 
			self.direction.y = 1 if self.rect.centery < self.ball.rect.centery else -1
		else:
			self.direction.y = 0

