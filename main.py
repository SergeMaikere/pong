from typing import Literal
from settings import *
import json
from GameObj import Player
from pygame import Event
from Utils.Rectangle import Rectangle
from GameObj.Player import Player
from GameObj.Opponent import Opps
from GameObj.Ball import Ball

class Game ( ):
	def __init__(self) -> None:
		pygame.init()
		pygame.display.set_caption('Pong II: Ball to the Wall')
		self.screen = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT) )

		self.clock = pygame.time.Clock()
 
		self.all_sprites = pygame.sprite.Group()
		self.paddle_sprites = pygame.sprite.Group()

		self.score = self.__get_score()
		self.font = pygame.font.Font(None, 160)

		self.running = True


	def __get_score ( self ):
		try:
			with open(join('data', 'score.txt')) as score_file:
				return json.load(score_file)
		except:
			return { 'player': 0, 'opponent': 0 }

	def __is_time_to_quit ( self, event: Event ):
		return event.type == pygame.QUIT

	def __event_loop_handler ( self ):
		for event in pygame.event.get():
			self.running = not self.__is_time_to_quit(event)
		
	def __set_background ( self ):
		self.background = Rectangle((WINDOW_WIDTH, WINDOW_HEIGHT), COLORS['bg'], self.all_sprites, topleft=(0,0))

	def __set_player ( self ):
		self.player = Player(self.all_sprites, self.paddle_sprites)

	def __set_ball ( self ):
		self.ball = Ball(self.all_sprites, self.paddle_sprites)

	def __set_opponent ( self ):
		self.opponent = Opps(self.ball, self.all_sprites, self.paddle_sprites)

	def __display_individual_score ( self, whom: Literal['player', 'opponent'] ):
		score_surface = self.font.render( str(self.score[whom]), True, COLORS['bg details'] )
		score_rect = score_surface.get_frect( center=(WINDOW_WIDTH/2 + (100 if whom == 'player' else -100), WINDOW_HEIGHT/2) )
		self.screen.blit(score_surface, score_rect)

	def __display_line ( self ):
		pygame.draw.line(self.screen, COLORS['bg details'], (WINDOW_WIDTH/2, 0), (WINDOW_WIDTH/2, WINDOW_HEIGHT), 5)

	def __display_score ( self ):
		self.__display_individual_score('player')
		self.__display_individual_score('opponent')
		self.__display_line()


	def run ( self ):

		self.__set_background()
		self.__set_ball()
		self.__set_player()
		self.__set_opponent()

		while self.running:
			dt = self.clock.tick() / 1000

			self.__event_loop_handler()

			self.all_sprites.update(dt)

			self.all_sprites.draw(self.screen)

			self.__display_score()
			
			pygame.display.update()

		pygame.quit()


if __name__ == '__main__':
	new_game = Game()
	new_game.run()