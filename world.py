import networkx as nx
import random

from town import Town
from event import Event

class World:
	"""a World contains Towns"""
	printLog = True
	events = dict()
	G = None

	k = 6 # Each node is joined with its k nearest neighbors in a ring topology
	p = 0.1 # The probability of adding a new edge for each edge

	def __init__(self, n):
		self.instantiateTowns(n)

	def instantiateTowns(self, n):
		self.G = nx.newman_watts_strogatz_graph(n, self.k, self.p)
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
		newEvent = Event(self.getRandomTown())
		self.events[newEvent.id()] = newEvent # getting id possibly costly + persistence issues

		# spread a random rumor
		event = random.choice(list(self.events.values()))
		self.spreadRumor(event.town, event)

	def spreadRumor(self, town, event):
		neighbors = list(self.G.neighbors(town.id()))
		neighbor = self.G.nodes()[random.choice(neighbors)]['node']
		newEvent = Event(neighbor, upstream=event)
		self.events[newEvent.id()] = newEvent # getting id possibly costly + persistence issues

	def run(self):
		for i in range(10):
			self.step()
		print("World ran!")