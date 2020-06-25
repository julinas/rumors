import random

class Agent:

	def __init__(self, nodeid):
		self.id = nodeid
		# the agent should have a buffer of recently-read events (tentative)

	def id(self):
		return self.id

	def perceiveStory(self):
		# Asynchronously receive a story that spawns in the environment
		pass

	def sendMessage(self, message):
		pass

	def receiveMessage(self, message):
		# Asynchronously receive a story-text from a neighbor
		# process the received message:
		# send the story-text through text-processing,
		# and store resulting story in buffer
		pass

	def step(self):
		# Decide the neighbor to spread a message to
		# Choose a story in the buffer to spread
		# return early if there is no story in the buffer
		# Send the story through text-processing to convert to story-text
		# Send story-text to chosen neighbor (call sendMessage)
		pass