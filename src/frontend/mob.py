import pygame

class Mob(object):
	def __init__(self):
		self.people = pygame.image.load('../../assets/images/mob.png')
		self.bubble = pygame.image.load('../../assets/images/bubble.png')

		self.bubble = pygame.transform.scale(self.bubble, (300, 300))

		with open("../../assets/data/insults.txt") as file:
			self.insults = file.read().splitlines()  

		with open("../../assets/data/compliments.txt") as file:
			self.compliments = file.read().splitlines()

	def draw(self, win):
		# win.blit(self.bg, (0, 0))
		win.blit(self.people, (900, 580))
		win.blit(self.bubble, (1150, 335))
