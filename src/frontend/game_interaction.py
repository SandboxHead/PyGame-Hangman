import pygame
import sys
sys.path.insert(1, '../backend')
from hangman import Hangman

class GameInteraction(object):
	def __init__(self, mode, category):
		letter = pygame.image.load('../../assets/images/letterRectangle.png')
		rounds = pygame.image.load('../../assets/images/RoundRectangle.png')
		self.hangman = Hangman(mode, category)

		self.word_boxes = []
		self.alphabet_boxes = []
		for i in range(len(self.hangman.curr_word)):
			self.word_boxes.append(pygame.transform.scale(letter, (70, 70)))

		for i in range(26):
			self.alphabet_boxes.append(pygame.transform.scale(rounds, (50, 50)))

		self.font = pygame.font.Font('../../assets/fonts/TEXAT BOLD PERSONAL USE___.otf', 32)



	def draw(self, win):
		start_point = 960 - 100*len(self.word_boxes)//2

		for i in range(len(self.word_boxes)):
			win.blit(self.word_boxes[i], (start_point + i*100 + 15, 40))


		start_point = 960 - 60*5
		
		
		for i in range(len(self.alphabet_boxes)):
			text = self.font.render(chr(i + ord('A')) , True, (0, 0, 0))
			if(i < 9):
				win.blit(self.alphabet_boxes[i], (start_point + i*60 + 15, 150))
				win.blit(text, (start_point + i*60 + 28, 155))

			elif(i < 18):
				win.blit(self.alphabet_boxes[i], (start_point + (i-9)*60 + 15, 215))
				win.blit(text, (start_point + (i-9)*60 + 28, 220))

			elif(i < 27):
				win.blit(self.alphabet_boxes[i], (start_point + (i-18)*60 + 15, 280))
				win.blit(text, (start_point + (i-18)*60 + 28, 285))




