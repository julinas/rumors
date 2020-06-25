import copy
import random

from components import TextMain

class Story:
	def __init__(self, world, node, upstream):

		self.main = None
		self.node = node
		self.upstream = upstream
		self.isRumor = False
		self.isCaughtRumor = False
		self.impactFactor = -1
		self.downstream = [] # use only for log

		if upstream != None:
			self.derivedMain(upstream)

			if world.catchRumors:
				# do some things to catch rumors...
				pass
		else:
			self.randomMain()

		self.id = id(self)

	# derivedMain would be obselete once we set up 
	# neural networks for story/text translation
	def derivedMain(self, upstream):
		# static way of mutating a story
		self.main = copy.deepcopy(upstream.main)
		self.impactFactor = upstream.impactFactor

		self.main.mutate(self)

	# TextMain which lives in components.py
	def randomMain(self):
		self.main = TextMain()

	def text(self):
		return self.main.text()

	def id(self):
		return self.id
