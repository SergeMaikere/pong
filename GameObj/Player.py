from settings import *
from pygame.sprite import Group
from Utils.Rectangle import Rectangle

class Player ( Rectangle ):
	def __init__(self, *groups: Group) -> None:
		super().__init__(SIZE['paddle'], COLORS['paddle'], *groups, center = POS['player'])