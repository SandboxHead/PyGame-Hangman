import pygame
import random

# Class responsible to show mob on the screen. Updates comment as well on guesses.
class Mob(object):
	def __init__(self):
		self.people = pygame.image.load('assets/images/mob.png')
		self.bubble = pygame.image.load('assets/images/bubble.png')

		self.bubble = pygame.transform.scale(self.bubble, (300, 300))

		with open("assets/data/insults.txt") as file:
			self.insults = file.read().splitlines()  

		with open("assets/data/compliments.txt") as file:
			self.compliments = file.read().splitlines()

		self.font = pygame.font.Font('assets/fonts/Steampuff.otf', 24)

		self.comment = ""

	def positive(self):
		self.comment = random.choice(self.compliments)

	def negative(self):
		self.comment = random.choice(self.insults)

	def draw(self, win):
		win.blit(self.people, (900, 580))
		win.blit(self.bubble, (1150, 335))

		text = self.font.render(self.comment, True, (0, 0, 0))
		win.blit(text, (1190, 430))


