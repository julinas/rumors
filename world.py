import math
import networkx as nx
import random

from town import Town
from event import Event

def sigmoid(x):
	return 1 / (1 + math.exp(-x))

class World:
	"""a World contains Towns"""

	def __init__(self, n, k, p, log=False, catchRumors=True):
		self.G = None
		self.instantiateTowns(n, k, p)
		self.events = dict()
		self.printLog = log
		self.catchRumors = catchRumors

	def instantiateTowns(self, n, k, p):
		self.G = nx.newman_watts_strogatz_graph(n, k, p)
		for node in self.G.nodes():
			town = Town()

			self.G = nx.relabel_nodes(self.G, {node: town.id()})
			self.G.nodes[town.id()]['node'] = town

		self.townList = list(self.G.nodes())

	def getRandomTown(self):
		node = random.choice(self.townList) # costly
		town = self.G.nodes[node]['node']
		return town

	def step(self):

		# create an event in a random town
		try:
			if random.random() < 0.1:
				newEvent = Event(self, self.getRandomTown(), None)
				self.events[newEvent.id()] = newEvent # getting id possibly costly + persistence issues
		except Exception: 
			# do nothing
			pass

		# try spread a random rumor
		if len(self.events) > 0:
			event = random.choice(list(self.events.values()))
			self.spreadRumor(event)

	def spreadRumor(self, event):
		# probability of actually spreading the rumor is higher if impact factor is higher
		# if a rumor has spread before, it is more likely to spread again
		if random.random() < sigmoid(event.impactFactor):
			neighbors = list(self.G.neighbors(event.town.id()))
			neighbor = self.G.nodes()[random.choice(neighbors)]['node']

			try:
				newEvent = Event(self, neighbor, event)
				self.events[newEvent.id()] = newEvent # getting id possibly costly + persistence issues
				if self.printLog:
					event.addDownstream(newEvent)
				newEvent.impactFactor += 0.5
				event.impactFactor += 0.5
			except Exception:
				# do nothing
				pass

	def recursivePrintEvent(self, event, indent=0):
		if len(event.downstream) > 0 or (event.upstream is not None and event.isCaughtRumor is not True): #suppress events that did not spread for now
			print("{}({}) {}{}".format("\t"*indent, event.spawntown.name, 
				"(Caught Rumor!) " if event.isCaughtRumor else "", event.text()))
		for e in event.downstream:
			self.recursivePrintEvent(e, indent=indent+1)


	def doPrintLog(self):
		for event in self.events.values():
			if event.upstream is None:
				self.recursivePrintEvent(event)

	def run(self, n):
		for i in range(n):
			self.step()

		if self.printLog:
			self.doPrintLog()

		print("World ran!")