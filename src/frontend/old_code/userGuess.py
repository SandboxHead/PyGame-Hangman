import string

class UserGuess(Category):
	def __init__(self, chosenword, word_encode):
		self.chosenword = chosenword
		self.word_encode = word_encode #same as chosenword, but displayed with underscores
		self.incorrectLetters = []
		self.correctLetters = []
		self.guessedLetters = []
		self.conclude = False
		self.match = False
	def guessLetterError(self):
		while not self.conclude: #while True
			guess = input("").upper()
			if len(guess) != 1:
				print("You must enter a single character!")
				continue
			elif guess in guessedLetter:
				print("You have already guessed that letter!")
				continue
			elif guess not in string.ascii_uppercase:
				print("You must enter a character in the alphabet!")
			else:
				return guess
	def guessLetter(self):
		if guess in self.chosenword:
			self.match = True
			for i in range(0, len(self.chosenword)):
				if chosenword[i] == guess: #if character appears in a given iteration
					self.word_encode = self.word_encode[0:i] + guess + self.word_encode[i+1:len(self.word_encode)]
					#slices the word at the index in which the character appears, then "appends" to that index
		return self.word_encode