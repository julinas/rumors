import copy
import random

from components import TextMain

class Event:
	main = None
	town = None # town to which the event is attributed
	spwantown = None # town in which event spawns
	upstream = None
	isRumor = False

	def __init__(self, town, upstream=None):
		self.spawntown = town

		if upstream != None:
			self.derivedMain(upstream)
			print("{} '{}' spread from {}. {} has new {}: '{}'".format(
				"Rumor" if self.upstream.isRumor else "Event",
				self.upstream.text(), self.upstream.spawntown.name, self.spawntown.name, 
				"rumor" if self.isRumor else "event",
				self.text()))
		else:
			self.randomMain()
			print("{} has new event: '{}'".format(self.spawntown.name, self.text()))

	def derivedMain(self, upstream):
		self.upstream = upstream
		self.main = copy.deepcopy(self.upstream.main)

		# the event might be attributed to the town in the story, 
		# the town the story is heard from, or local town
		self.town = random.choice([self.upstream.town, self.upstream.spawntown, self.spawntown])
		if self.town is not self.upstream.town:
			# mutated location
			self.isRumor = True

		if random.random() > 0.5:
			self.isRumor = True
			self.main.mutate()

	def randomMain(self):
		self.town = self.spawntown
		self.main = TextMain()

	def text(self):
		return "In {}, {}.".format(self.town.name, self.main.text())

	def id(self):
		return id(self)
