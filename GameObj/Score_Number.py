from pygame import FRect, Surface
from settings import *
from typing import Callable, Literal
from pygame.sprite import Group

class Score_Number ( pygame.sprite.Sprite ):
	def __init__(self, score: Score, get_score: Callable[[], Score], whom: Literal[ 'player', 'opponent' ], *groups: Group) -> None:
		super().__init__(*groups)
		
		self.whom = whom
		self.score = score
		self.get_score = get_score

		self.font = pygame.font.Font(None, 160)
		self.image: Surface = self.__update_image()
		self.rect: FRect = self.__get_frect()

	def __update_image ( self ): 
		return self.font.render( str(self.score[self.whom]), True, COLORS['bg details'] )
	
	def __get_frect ( self ): 
		return self.image.get_frect( center=(WINDOW_WIDTH/2 + (100 if self.whom == 'player' else -100), WINDOW_HEIGHT/2) )


	def update ( self, dt: float ): 
		self.score = self.get_score()
		self.image = self.__update_image()
