from settings import *

class All_Sprites ( pygame.sprite.Group ):
	def __init__(self):
		super().__init__(self)
		self.screen = pygame.display.get_surface()


	def draw ( self ):
		for sprite in self:
			if hasattr(sprite, 'shadowed') and sprite.shadowed: 
				shadow_image, shadow_rect = sprite._get_shadow_data()
				self.screen.blit(shadow_image, shadow_rect.topleft)

			self.screen.blit( sprite.image, sprite.rect.topleft )
