from settings import *
import json
from pygame import Event
from typing import Literal
from Utils.All_Sprites import All_Sprites
from Utils.Shape import Shape
from GameObj import Player
from GameObj.Player import Player
from GameObj.Opponent import Opps
from GameObj.Ball import Ball
from GameObj.Middle_line import Middle_Line
from GameObj.Score_Number import Score_Number

class Game ( ):
	def __init__(self) -> None:
		pygame.init()
		pygame.display.set_caption('Pong II: Ball to the Wall')
		self.screen = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT) )

		self.clock = pygame.time.Clock()
 
		self.all_sprites = All_Sprites()
		self.paddle_sprites = pygame.sprite.Group()

		self.score = self.__get_score()
		self.font = pygame.font.Font(None, 160)

		self.running = True


	def __get_score ( self ) -> Score:
		try:
			with open(join('data', 'score.txt')) as score_file:
				return json.load(score_file)
		except:
			return { 'player': 0, 'opponent': 0 }

	def update_score ( self, whom: Literal['player', 'opponent'] ): self.score[whom] += 1

	def get_score ( self ): return self.score

	def __save_score ( self ):
		with open( join('data', 'score.txt'), 'w' ) as score_file:
			json.dump(self.score, score_file)

	def __is_time_to_quit ( self, event: Event ):
		return event.type == pygame.QUIT

	def __event_loop_handler ( self ):
		for event in pygame.event.get():
			if self.__is_time_to_quit(event):
				self.__save_score()
				self.running = False
		
	def __set_background ( self ):
		self.background = Shape('rectangle', (WINDOW_WIDTH, WINDOW_HEIGHT), COLORS['bg'], self.all_sprites, topleft=(0,0))

	def __set_player ( self ):
		self.player = Player(self.all_sprites, self.paddle_sprites)

	def __set_ball ( self ):
		self.ball = Ball(self.update_score, SIZE['ball'], COLORS['ball'], self.all_sprites, self.paddle_sprites)

	def __set_opponent ( self ):
		self.opponent = Opps(self.ball, self.all_sprites, self.paddle_sprites)

	def __set_score ( self ):
		Score_Number(self.score, self.get_score, 'player', self.all_sprites)
		Score_Number(self.score, self.get_score, 'opponent', self.all_sprites)
		Middle_Line(self.all_sprites)


	def run ( self ):

		self.__set_background()
		self.__set_score()
		self.__set_ball()
		self.__set_player()
		self.__set_opponent()

		while self.running:
			dt = self.clock.tick() / 1000

			self.__event_loop_handler()

			self.all_sprites.update(dt)

			self.all_sprites.draw()
			
			pygame.display.update()

		pygame.quit()


if __name__ == '__main__':
	new_game = Game()
	new_game.run()