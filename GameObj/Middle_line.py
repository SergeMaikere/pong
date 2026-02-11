from pygame.sprite import Group
from settings import *

class Middle_Line ( pygame.sprite.Sprite ):

	def __init__(self, *groups: Group) -> None:
		super().__init__(*groups)

		self.image = pygame.Surface((10, WINDOW_HEIGHT), pygame.SRCALPHA)
		pygame.draw.line(self.image, COLORS['bg details'], (5, 0), (5, WINDOW_HEIGHT), 5)
		self.rect = self.image.get_frect( center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2) )
