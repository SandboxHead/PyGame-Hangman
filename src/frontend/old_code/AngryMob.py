

class AngryMob(UserGuess):
	def __init__(self, comment, noise):
		self.comment = comment

	def __str__(self):
		return self.comment 

	def visualInsults(self):
		with open("../../assets/data/insults.txt") as file:
			insults = file.read()
		lines = insults.splitlines() #split lines is used to put string in list without breaks, perfect for phrases
		line_location = random.randrange(0,len(insults))
		self.comment = insults[line_location]

	def visualCompliments(self):
		with open("../../assets/data/compliments.txt") as file:
			compliments = file.read()
		lines = compliments.splitlines()
		line_location = random.randrange(0,len(compliments)) 
		self.comment = compliments[line_location]
		
	def insultSounds(self):
		pygame.mixer.music.stop() #stops ambient music
		pygame.mixer.music.load("../../assets/music/angry.mp3")
		pygame.mixer.music.play()
		pygame.mixer.music.play("../../assets/music/ambient.mp3")
	def complimentSounds(self):
		pygame.mixer.music.stop() #stops ambient music
		pygame.mixer.music.load("../../assets/music/cheer.mp3")
		pygame.mixer.music.play()
		pygame.mixer.music.play("../../assets/music/ambient.mp3")