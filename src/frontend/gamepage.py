import pygame
from mob import Mob
from hanged import Hanged
from game_interaction import GameInteraction

# Class responsible for Game screen. It uses mob, hanged and game as subpart to show in it.
class Gamepage(object):
	def __init__(self, mode, category):
		self.bg = pygame.image.load('assets/images/background2.jpg')
		self.bg = pygame.transform.scale(self.bg, (1920, 1080))
		self.mob = Mob()
		self.hanged = Hanged()
		self.game = GameInteraction(mode, category)

	def click(self, win, mouse_pos):
		response = self.game.click(win, mouse_pos)
		if(response == "wrong"):
			self.mob.negative()
		elif(response == "right"):
			self.mob.positive()
		if(response == "pass"):
			return self.hanged.click(mouse_pos)

		return response

	def draw(self, win):
		win.blit(self.bg, (0, 0))
		self.mob.draw(win)
		self.hanged.draw(win)
		self.game.draw(win)
