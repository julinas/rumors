import random
class Agent:

	def __init__(self, nodeid):
		self.id = nodeid
		# self == this?
		# the agent should have a buffer of recently-read stories
		# see tryPutInBuffer()
		# the agent should have a two small neural networks:
		#  story-to-text and vice versa

	def id(self):
		return self.id
	def perceiveStory(self):
		# Asynchronously receive a story that spawns in the environment
		pass

	def sendMessage(self, neighbor, message):
		pass

	def receiveMessage(self, message):
		### use dummy version of text-processing
		# Asynchronously receive a story-text from a neighbor
		# process the received message:
		# send the story-text through text-processing,
		# and store resulting story in buffer
		pass

	def tryPutInBuffer(self, message):
		## the buffer should NOT be a "buffer" type (which stores bytes)
		## for this buffer, use a dictionary where the key is timestamp of
		## when the story is processed, and value is the story itself
		## as a buffer, it has a limit to the number of instances that can be stored
		## when it is "full", it will not accept new stories. Should return gracefully
		## with a message, without causing exceptions/errors

	def pruneBuffer(self):
		# remove stories in the buffer that are too old
		# make the threshold for "too old" a variable so it's easy to tweak

	def step(self):
		key = id(self)
		list = World.G.neighbors(key)
		neighbor = random.choice(list)
		story = self.tryPopRandomBuffer()
		if (story != None):
			text = self.storyToText(story)
			self.sendMessage(neighnor, text)
		else:
			return;
		# Decide the neighbor to spread a message to
		# Choose a story in the buffer to spread
		# return early if there is no story in the buffer
		# Send the story through text-processing to convert to story-text
		# Send story-text to chosen neighbor (call sendMessage)
		pass

	def storyToText(self): #shouldn't self be a Story value???
		# can use dummy values before a neural network module is set up
		pass

	def textToStory(self):
		# can use dummy values before a neural network module is set up
		pass
