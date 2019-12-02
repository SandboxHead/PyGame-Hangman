import random

class Hangman:
	def __init__(self, mode, category):
		filename = "../../assets/data/" + category + ".txt"
		self.words = self.read_file(filename)
		if mode == "easy":
			self.max_attempts = 9
		else:
			self.max_attempts = 6

		self.reset()

	@staticmethod
	def read_file(filename):	
		with open (filename, 'r') as file:
			return file.read().splitlines()

	def insert_letter(self, c):
		if(len(c) != 1):
			return -1
		if(ord(c) < ord('a') or ord(c) > ord('z')):
			return -1

		if c in self.correct_letters:
			return -2
		if c in self.incorrect_letters:
			return -2

		flag = 0
		for i in range(self.word_size):
			if self.curr_word[i] == c:
				self.predicted_word[i] = 1
				self.predicted_word_count += 1
				flag = 1

		if(flag == 0):
			self.num_attempts += 1
			self.incorrect_letters.add(c)

			if (self.num_attempts == self.max_attempts):
				return 0
			return 2
		else:
			self.correct_letters.add(c)
			if self.check_win():
				return 1
			return 3

	def check_win(self):
		return self.predicted_word_count == self.word_size

	def already_checked(self, c):
		return c in self.correct_letters or c in self.incorrect_letters


	def reset(self):
		self.curr_word = random.choice(self.words).lower()
		# print(self.curr_word)
		self.word_size = len(self.curr_word)
		self.predicted_word = [0]*self.word_size
		self.correct_letters = set()
		self.incorrect_letters = set()
		self.predicted_word_count = 0
		self.num_attempts = 0

if __name__ == "__main__":
	man = Hangman("easy", "sports")