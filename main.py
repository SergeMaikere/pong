from settings import *
from pygame import Event
from Utils.Rectangle import Rectangle

class Game ( ):
	def __init__(self) -> None:
		pygame.init()
		pygame.display.set_caption('Pong II: Ball to the Wall')
		self.screen = pygame.display.set_mode( (WINDOW_WIDTH, WINDOW_HEIGHT) )



		self.clock = pygame.time.Clock()

		self.all_sprites = pygame.sprite.Group()

		self.running = True


	def __is_time_to_quit ( self, event: Event ):
		return event.type == pygame.QUIT

	def __event_loop_handler ( self ):
		for event in pygame.event.get():
			self.running = not self.__is_time_to_quit(event)

	def __set_background ( self ):
		Rectangle((0, 0), (WINDOW_WIDTH, WINDOW_HEIGHT), COLORS['bg'], self.all_sprites)

	def run ( self ):
		self.__set_background()

		while self.running:
			dt = self.clock.tick() / 1000

			self.__event_loop_handler()

			self.all_sprites.update(dt)

			self.all_sprites.draw(self.screen)

			pygame.display.update()

		pygame.quit()


if __name__ == '__main__':
	new_game = Game()
	new_game.run()