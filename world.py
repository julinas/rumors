import math
import networkx as nx
import random

from agent import Agent
from story import Story

def sigmoid(x):
	return 1 / (1 + math.exp(-x))

class World:
	"""a World contains Towns"""

	def __init__(self, n, k, p, log=False, catchRumors=True):
		# self.G = None
		# self.instantiateTowns(n, k, p)
		self.instantiateAgents(n, k, p)
		self.stories = dict()
		self.printLog = log
		self.catchRumors = catchRumors

	def instantiateAgents(self, n, k, p):
		self.G = nx.newman_watts_strogatz_graph(n, k, p)
		for node in self.G.nodes():
			agent = Agent(node)
			self.G.nodes[node]['node'] = agent

	def getRandomNode(self):
		node = random.choice(self.G.nodes())
		return node

	def getRandomAgent(self):
		node = random.choice(self.G.nodes())
		agent = self.G.nodes[node]['node']
		return agent

	def step(self):
		# Create an event in a random node
		# Allow nearby agents to perceive the event (distance = 0, 1, 2?)
		# We want to set up the frequency of world.step() so that the world is 
		# not swarmed with new stories ... relative frequencey of world.step() to agent.step()
		# needs to be tweaked
		newStory = Story(self, self.getRandomNode(), None)
		self.stories[story.id()] = newStory

	def recursivePrint(self, story, indent=0):
		if len(story.downstream) > 0 or (story.upstream is not None and story.isCaughtRumor is not True): #suppress storys that did not spread for now
			print("{} {}{}".format("\t"*indent,  
				"(Caught Rumor!) " if story.isCaughtRumor else "", story.text()))
		for e in story.downstream:
			self.recursivePrint(e, indent=indent+1)

	def doPrintLog(self):
		for story in self.stories.values():
			if story.upstream is None:
				self.recursivePrint(story)

	def run(self, n):
		for i in range(n):
			self.step()

		if self.printLog:
			self.doPrintLog()

		# print("World ran!")