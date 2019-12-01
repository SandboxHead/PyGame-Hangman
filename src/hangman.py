class Hungman(UserGuess):
	'''
	This class is mainly pseudocode for now. I am working to develop an understanding of PyGame and OOP -- will definitely revist this
	'''
	def __init__(self, x, y, width, height, word, letters):
		self.x = x
		self.y = y
		self.word = word
		self.width = width
		self.height = height
	def chooseWord(self):
		chosenword = random.randint(0, self.category-1)
		return self.category[chosenword]
	def setPlatform(self):
		pygame.image.load("assets/platform.png")
		#set position here
	def userGuess(self, redundantChoice):
		if guess in chosenword:
			self.ticked = True
		elif guess is self.ticked:
			print("You already guessed that letter!")
	def drawBody(self):
		pygame.image.load("assets/head.png")
		pygame.image.load("assets/torso.png")
		pygame.image.load("assets/arm1.png")
		pygame.image.load("assets/arm2.png")
		pygame.image.load("assets/leg1.png")
		pygame.image.load("assets/leg2.png")
		if self.difficulty == "easy"
		pygame.image.load("assets/face.png")
		pygame.image.load("assets/hand1.png")
		pygame.image.load("assets/hand2.png")
		#set positions of body parts

