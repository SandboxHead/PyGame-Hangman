import pygame
from frontpage import Frontpage
from gamepage import Gamepage 

class Controller(object):
	def __init__(self):
		pygame.init()
		pygame.font.init()
		self.win = pygame.display.set_mode((1920, 1080))
		pygame.display.set_caption("Hangman")
		self.run = True
		self.start_page = Frontpage()
		

		self.game_mode = 0
		self.run_game()

	def event_front_page(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.run = False
			if(event.type == pygame.MOUSEBUTTONDOWN):
				mouse_pos = event.pos
				response = self.start_page.click(mouse_pos)
				if(response != None):
					self.start_game(response)

	def check_game_response(self, response):


	def event_game_page(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.run = False
			if(event.type == pygame.MOUSEBUTTONDOWN):
				mouse_pos = event.pos
				response = self.game_page.click(self.win, mouse_pos)
				check_game_response(response)

	def run_game(self):
		while self.run:
			pygame.time.delay(30)
			if(self.game_mode == 0):
				self.event_front_page()
			else:
				self.event_game_page()

			self.redraw_game_window()

		pygame.quit()

	def start_game(self, response):
		self.game_mode = 1
		self.game_status = "running"
		self.game_page = Gamepage(response["mode"], response["category"])

	def redraw_game_window(self):
		if(self.game_mode == 0):
			self.start_page.draw(self.win)
		else:
			self.game_page.draw(self.win)
		pygame.display.update()

if __name__ == "__main__":
	game = Controller()