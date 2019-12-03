import pygame

class Frontpage(object):
	def __init__(self):
		self.difficulties = ["Easy", "Hard"]
		self.categories = ["World", "Sports", "Science", "People", "Food"]
		self.diff_images = [pygame.image.load('assets/images/EASY.png'), pygame.image.load('assets/images/HARD.png')]
		self.categ_images = [
			pygame.image.load('assets/images/WORLD.png'),
			pygame.image.load('assets/images/SPORTS.png'),
			pygame.image.load('assets/images/SCIENCE.png'),
			pygame.image.load('assets/images/PEOPLE.png'),
			pygame.image.load('assets/images/FOOD.png')
		]	
		self.b1_dim = (150, 70)
		self.b2_dim = (210, 150)
		self.start_button = pygame.image.load('assets/images/START.png')

		self.bg = pygame.image.load('assets/images/background1.jpg')
		self.font1 = pygame.font.Font('assets/fonts/Drifttype Solid.ttf', 80)
		self.font2 = pygame.font.Font('assets/fonts/Drifttype Solid.ttf', 30)
		self.mode = "easy"
		self.category = "world"
		self.start_game = False

	def interactive_button(self, win, mouse, topleft, bottomright):
		if(topleft[0] < mouse[0] < bottomright[0] and topleft[1] < mouse[1] < bottomright[1] ):
			width = bottomright[1] - topleft[1]
			height = topleft[0] - bottomright[0]

			pygame.draw.rect(win, (0, 255, 0), (topleft[0], topleft[1], width, height))

	def render_difficulty(self, win, mouse):
		text = self.font2.render("Choose Difficulty", True, (0, 0, 0))
		win.blit(text, (810, 250))
		
		win.blit(self.diff_images[0], (740, 320))
		win.blit(self.diff_images[1], (1020, 320))

		# self.interactive_button(win, mouse, (740, 320), (900, 400))


	def render_category(self, win):
		text = self.font2.render("Choose Category", True, (0, 0, 0))
		
		win.blit(text, (810, 550))
		
		win.blit(self.categ_images[0], (405, 620))
		win.blit(self.categ_images[1], (645, 620))
		win.blit(self.categ_images[2], (885, 620))
		win.blit(self.categ_images[3], (1115, 620))
		win.blit(self.categ_images[4], (1355, 620))
		
	def check_diff_click(self, pos):
		if(740 < pos[0] < 890):
			self.mode = "easy"
		elif(1020 < pos[0] < 1170):
			self.mode = "hard"

	def check_cat_click(self, pos):
		if(405 < pos[0] < 405 + 150):
			self.category = "world"
		elif(645 < pos[0] < 645 + 150):
			self.category = "sports"
		elif(885 < pos[0] < 885 + 150):
			self.category = "science"
		elif(1115 < pos[0] < 1115 + 150):
			self.category = "people"
		elif(1355 < pos[0] < 1355 + 150):
			self.category = "food"

	def check_start_click(self, pos):
		if(855 < pos[1] < 1065):
			self.start_game = True
		else:
			self.start_game = False

	def click(self, pos):
		print("click detected", pos)
		self.start_game = False
		if(320 < pos[1] < 390):
			self.check_diff_click(pos)
		elif(620 < pos[1] < 690):
			self.check_cat_click(pos)
		elif(800 < pos[1] < 950):
			self.check_start_click(pos)

		if(self.start_game):
			print("Game is starting")
			return {"mode" : self.mode, "category" : self.category}
		else:
			return None

	def draw(self, win):
		mouse = pygame.mouse.get_pos()
		win.blit(self.bg, (0, 0))
		text = self.font1.render("HANGMAN", True, (0, 0, 0))
		win.blit(text, (760, 100))
		self.render_difficulty(win, mouse)
		self.render_category(win)

		win.blit(self.start_button, (855, 800))

