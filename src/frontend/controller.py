import pygame
from frontpage import Frontpage
from gamepage import Gamepage 
from game_over import Lastpage
import json

# Main frontend class which connects all the game modules. Runs and manage pygame display
class Controller(object):
	def __init__(self):
		pygame.init()

		pygame.mixer.init()
		pygame.mixer.music.load('assets/music/ambient.wav')
		pygame.mixer.music.play(-1)

		self.boo_sound = pygame.mixer.Sound('assets/music/boo.wav')
		self.cheer_sound = pygame.mixer.Sound('assets/music/cheer.wav')


		pygame.font.init()
		self.win = pygame.display.set_mode((1920, 1080))
		pygame.display.set_caption("Hangman")
		self.run = True
		self.start_page = Frontpage()
		
		self.game_mode = 0
		self.clock = pygame.time.Clock()
		self.run_game()

	# Function to manage events when screen is on frontpage.
	def event_front_page(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.run = False
			if(event.type == pygame.MOUSEBUTTONDOWN):
				mouse_pos = event.pos
				response = self.start_page.click(mouse_pos)
				if(response != None):
					self.start_game(response)

	# Updates data_file. Called everytime a game is finished.
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


		
	# Switch to fail_game mode by changing game_mode to 2. Loads game over screen. 
	def failed_game(self):
		self.game_mode = 2
		self.last_page = Lastpage("game_over_screen")
		self.update_json(0)
	# Switch to pass_game mode by changing game_mode to 3. Loads win Screen. 
	def passed_game(self):
		self.update_json(1)
		self.game_mode = 3
		self.last_page = Lastpage("win_screen")

	# A function to check the click response while playing game.
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
		elif (response == "right"):
			pygame.mixer.Sound.play(self.cheer_sound)
		elif (response == "retry"):
			self.start_game(self.old_reponse)
		elif (response == "menu"):
			self.game_mode = 0
		
	# A function to manage events when on game page
	def event_game_page(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.run = False
			if(event.type == pygame.MOUSEBUTTONDOWN):
				mouse_pos = event.pos
				response = self.game_page.click(self.win, mouse_pos)
				self.check_game_response(response)

	# A function to manage events when on last page reached either after win or lose
	def event_last_page(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.run = False
			if(event.type == pygame.MOUSEBUTTONDOWN):
				mouse_pos = event.pos
				response = self.last_page.click(mouse_pos)
				self.check_game_response(response)

	# This is a loop running infinetly refreshing the game display.
	def run_game(self):
		while self.run:
			self.clock.tick(30)
			if self.game_mode == 0 :
				self.event_front_page()
			elif self.game_mode == 1:
				self.event_game_page()
			else:
				self.event_last_page()
			self.redraw_game_window()

		pygame.quit()

	# Function called on clicking Start on frontpage
	def start_game(self, response):
		self.old_reponse = response
		self.game_mode = 1
		self.game_status = "running"
		self.game_page = Gamepage(response["mode"], response["category"])

	# Refresh the game display after changes
	def redraw_game_window(self):
		if(self.game_mode == 0):
			self.start_page.draw(self.win)
		elif(self.game_mode == 1):
			self.game_page.draw(self.win)
		else:
			self.last_page.draw(self.win)
		pygame.display.update()

# if __name__ == "__main__":
# 	game = Controller()