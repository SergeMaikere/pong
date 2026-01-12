from settings import *
from pygame.sprite import Group
from Utils.Paddle import Paddle

class Opps ( Paddle ):
	def __init__(self, *groups: Group) -> None:
		super().__init__(SIZE['paddle'], COLORS['paddle'], *groups, center = POS['opponent'])

		self.speed = SPEED['opponent']