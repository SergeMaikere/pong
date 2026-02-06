from settings import *

class All_Sprites ( pygame.sprite.Group ):
	def __init__(self):
		super().__init__(self)
		self.screen = pygame.display.get_surface()


	def draw ( self ):
		for sprite in self:
			self.screen.blit( sprite.image, sprite.rect.topleft )
