class Clickable:
	'''
	A lot of effort was spent trying to understand this part too prematurely, this should come after the other classes as it is more design oriented than it is logic.
	'''
	def __init__(self, button, letter, color, position, width, height, text, variation=0, size = 65):
		self.button = button
		self.variation = variation #0 is play game, 1 is difficulty, 2 is category, 3 is letters
		self.ticked = False #for letters on screen
		self.mouseOn = False #for all
		self.letter = letter
		self.color = color
		self.position = position
		self.width = width
		self.height = height
		self.text = text
		self.subsurface = pygame.Surface((self.width, self.height))
		self.subsurface.fill(self.color)
		self.text = self.font.render(self.letter, True, (255,255,255))
	def mouseOver(self, surface):
		if self.variation == 0:
			if self.mouseOn:
				self.subsurface.set_alpha(250) #APPEARANCE WHEN MOUSE IS ON THE BUTTON
			else:
				self.subsurface.set_alpha(300) #WHEN MOUSE NOT ON BUTTON
		if self.variation == 1:
			if self.mouseOn:
				self.subsurface.set_alpha(250) #APPEARANCE WHEN MOUSE IS ON THE BUTTON
			else:
				self.subsurface.set_alpha(300) #WHEN MOUSE NOT ON BUTTON
		if self.variation == 2:
			if self.mouseOn:
				self.subsurface.set_alpha(250) #APPEARANCE WHEN MOUSE IS ON THE BUTTON
			else:
				self.subsurface.set_alpha(300) #WHEN MOUSE NOT ON BUTTON
		if self.variation == 3:
			if self.mouseOn:
				self.subsurface.set_alpha(250) #APPEARANCE WHEN MOUSE IS ON THE BUTTON
			else:
				self.subsurface.set_alpha(300) #WHEN MOUSE NOT ON BUTTON
			if self.ticked is False:
				surface.blit(self.subsurface, self.position)
				self.subsurface.blit(self.text, (self.width/6,self.height/6)) #RANDOM VALUES -- CHANGE WITH EXPERIMENTATION
	def startGame(self):
		pass
	def endGame(self):
		pass
	def difficultyEasy(self):
		pass
	def difficultyHard(self):
		pass
	def categorySports(self):
		pass
	def categoryScience(self):
		pass
	def categoryPeople(self):
		pass
	def categoryFood(self):
		pass
	def categoryWorld(self):
		pass
