import pygame
from frontpage import Frontpage
from gamepage import Gamepage 
from game_over import Failpage
import json

class Controller(object):
	def __init__(self):
		pygame.init()

		pygame.mixer.init()
		pygame.mixer.music.load('../../assets/music/ambient.wav')
		pygame.mixer.music.play(-1)

		self.boo_sound = pygame.mixer.Sound('../../assets/music/boo.wav')
		self.cheer_sound = pygame.mixer.Sound('../../assets/music/cheer.wav')


		pygame.font.init()
		self.win = pygame.display.set_mode((1920, 1080))
		pygame.display.set_caption("Hangman")
		self.run = True
		self.start_page = Frontpage()
		
		self.game_mode = 0
		self.clock = pygame.time.Clock()
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

	def update_json(self, win):
		data = {"streak" : 0, "wins" : 0, "played" : 0, "win_percent" : 0}

		try:
			with open("data_file.json", "r") as read_file:
				data = json.load(read_file)
		except:
			pass
		if win == 1:
			data["streak"] += 1
			data["wins"] += 1

		else:
			data["streak"] = 0

		data["played"] += 1
		data["win_percent"] = round(100*data["wins"]/data["played"])

		with open("data_file.json", "w") as write_file:
			json.dump(data, write_file)


		

	def failed_game(self):
		self.game_mode = 2
		self.last_page = Failpage("game_over_screen")
		self.uddate_json(0)

	def passed_game(self):
		self.update_json(1)
		self.game_mode = 3
		self.last_page = Failpage("win_screen")

	def check_game_response(self, response):
		# print(response)
		if(response == "failed"):
			pygame.mixer.Sound.play(self.boo_sound)
			self.failed_game()
		elif (response == "passed"):
			pygame.mixer.Sound.play(self.cheer_sound)
			self.passed_game()
		elif (response == "wrong"):
			pygame.mixer.Sound.play(self.boo_sound)
			self.game_page.hanged.increase_error()
		elif (response == "retry"):
			self.start_game(self.old_reponse)
		elif (response == "menu"):
			self.game_mode = 0
		elif (response == "right"):
			pygame.mixer.Sound.play(self.cheer_sound)

	def event_game_page(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.run = False
			if(event.type == pygame.MOUSEBUTTONDOWN):
				mouse_pos = event.pos
				response = self.game_page.click(self.win, mouse_pos)
				self.check_game_response(response)

	def event_last_page(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.run = False
			if(event.type == pygame.MOUSEBUTTONDOWN):
				mouse_pos = event.pos
				response = self.last_page.click(mouse_pos)
				self.check_game_response(response)

	def run_game(self):
		while self.run:
			self.clock.tick(30)
			pygame.time.delay(30)
			if self.game_mode == 0 :
				self.event_front_page()
			elif self.game_mode == 1:
				self.event_game_page()
			else:
				self.event_last_page()
			self.redraw_game_window()

		pygame.quit()

	def start_game(self, response):
		self.old_reponse = response
		self.game_mode = 1
		self.game_status = "running"
		self.game_page = Gamepage(response["mode"], response["category"])

	def redraw_game_window(self):
		if(self.game_mode == 0):
			self.start_page.draw(self.win)
		elif(self.game_mode == 1):
			self.game_page.draw(self.win)
		else:
			self.last_page.draw(self.win)
		pygame.display.update()

if __name__ == "__main__":
	game = Controller()