import copy
import random

from components import TextMain

class Event:

	def __init__(self, world, town, upstream):
		self.main = None
		self.town = None # town to which the event is attributed
		self.spawntown = town # town in which event spawns
		self.upstream = upstream
		self.isRumor = False
		self.isCaughtRumor = False
		self.impactFactor = -1
		self.downstream = [] # use only for log

		if upstream != None:
			for e in upstream.downstream:
				if e.spawntown is self.spawntown:
					raise Exception('same event has already spread here')
			if upstream.spawntown is self.spawntown: # not sure what causes this but prevent it
				raise Exception('upstream spawntown is the same as current spawntown')
			if upstream.isCaughtRumor is True:
				raise Exception('upstream is a known rumor')
			self.derivedMain(upstream)
			# print("{} '{}' spread from {}. {} has new {}: '{}'".format(
			# 	"Rumor" if self.upstream.isRumor else "Event",
			# 	self.upstream.text(), self.upstream.spawntown.name, self.spawntown.name, 
			# 	"rumor" if self.isRumor else "event",
			# 	self.text()))

			# this is expensive... 
			for e in world.events.values():
				if e.spawntown == self.spawntown:
					if e.text() == self.text():
						return Exception('same event was already heard of in this location')

			if world.catchRumors:
				# get all townnames associated with the original event
				# ensure that this town is not already in the event tree
				ancestor = upstream
				while ancestor.upstream is not None:
					ancestor = ancestor.upstream
				tempevents = [ancestor]
				knowntowns = set([ancestor.spawntown.name])

				while len(tempevents) > 0:
					nexttempevents = []
					for tempevent in tempevents:
						knowntowns.add(tempevent.spawntown.name)
						nexttempevents += tempevent.downstream
					tempevents = nexttempevents

				if self.spawntown.name in knowntowns:
					self.isCaughtRumor = True
		else:
			self.randomMain()
			# print("{} has new event: '{}'".format(self.spawntown.name, self.text()))

			# this is expensive... placeholder check while there aren't enough different frames
			for e in world.events.values():
				if e.isRumor is False and e.text() == self.text():
					return Exception('same event already happened in this location')

		self.upstream = upstream

	def derivedMain(self, upstream):
		self.main = copy.deepcopy(upstream.main)

		# the event might be attributed to the town in the story, 
		# the town the story is heard from, or local town
		self.town = random.choice([self.upstream.town, self.upstream.spawntown])
		if self.town is not self.upstream.town:
			# mutated location
			self.isRumor = True

		# if random.random() > 0.5:
		# always mutate
		# self.isRumor = True # set isRumor inside mutate
		self.main.mutate(self)

	def randomMain(self):
		self.town = self.spawntown
		self.main = TextMain()

	def addDownstream(self, event):
		self.downstream.append(event)

	def text(self):
		return "In {}, {}.".format(self.town.name, self.main.text())

	def id(self):
		return id(self)
