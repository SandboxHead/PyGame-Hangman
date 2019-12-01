import string
import re

class Category(Clickable):
	def __init__(self, difficulty, category):
		self.difficulty = difficulty #EASY AND HARD
		self.category = category #SPORTS,SCIENCE,PEOPLE,WORLD,FOOD

	def chooseDifficulty(self, easy, hard): #DETERMINES THE AMOUNT OF LIVES GIVEN AND COMPLEXITY OF WORD
		if self.difficulty == "easy": #button in 'Class Clickable' will return a string
			chosendifficulty = HangmanObject().easy
			return chosendifficulty
		elif self.difficulty == "hard": #button in 'Class Clickable' will return a string
			chosendifficulty = HangmanObject().hard
			return chosendifficulty
			
	def chooseCategory(self, sports, science, people, world, food): #SIMPLY OPENS TXT, DOES NOT CHOOSE RANDOM WORD YET (Must inherit Clickable)
		if self.category == "sports":
			with open('../assets/data/sports.txt', 'r') as sports:
				sports = sports.read().splitlines() #stores string into list separated by new lines
				self.category = sports
			return self.category
		elif self.category == "science":
			with open('../assets/data/science.txt', 'r') as science:
				science = science.read().splitlines()
				self.category = science
			return self.category
		elif self.category == "people":
			with open('../assets/data/people.txt', 'r') as people:
				people = people.read().splitlines()
				self.category = people
			return self.category
		elif self.category == "world":
			with open('../assets/data/world.txt', 'r') as world:
				world = world.read().splitlines()
				self.category = world
			return self.category
		elif self.category == "food":
			with open('../assets/data/food.txt', 'r') as food:
				food = food.read().splitlines()
				self.category = food
			return self.category
	def wordSelection(self):
		if self.difficulty == "easy":
			wordrange = random.randint(0, 6)
			chosenword = self.category[wordrange]
			return chosenword
		if self.difficulty == "hard":
			wordrange = random.randint(7,12)
			chosenword = self.category[wordrange]
			return chosenword
	def encodeWord(self, chosenword):
		word_encode = re.sub("a-zA-Z", "_", chosenword)
		return word_encode

