import pygame.font

class MyButton:
	def __init__(self, screen, msg, x, y, w, h, r, g, b):
		self.screen = screen
		self.screen_rect = self.screen.get_rect()

		self.width, self.height = w, h
		self.button_color = (r, g, b)
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont(None, 48)

		self.rect = pygame.Rect(0, 0, self.width, self.height)
		self.rect.center = (x, y)

		self._prep_msg(msg)

	def _prep_msg(self, msg):
		self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		self.screen.fill(self.button_color, self.rect)
		self.screen.blit(self.msg_image, self.msg_image_rect)