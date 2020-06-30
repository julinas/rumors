import random
#import timestamp module for timestamp in tryPUtInBuffer
#gives epoch time
import time
class Agent:

	def __init__(self, nodeid):
		self.id = nodeid
		# the agent should have a buffer of recently-read stories
		# see tryPutInBuffer()
		# the agent should have a two small neural networks:
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
		limit = 6 #subject to change
		if (len(buffer) < limit):
			buffer[time.time()] = message
		else:
			return "Sorry, buffer is full"

	def pruneBuffer(self):
		# remove stories in the buffer that are too old
		# make the threshold for "too old" a variable so it's easy to tweak
		#86400 epoch seconds is one day
		old_threshold = time.time() - 86400 #subject to change
		for key in buffer:
			if (key > old_threshold):
				buffer.pop(key)

	def step(self):
		key = id(self)
		list = World.G.neighbors(key)
		neighbor = random.choice(list)
		story = self.tryPopRandomBuffer()
		if (story != None):
			text = self.storyToText(story)
			self.sendMessage(neighbor, text)
		else:
			return
		# Decide the neighbor to spread a message to
		# Choose a story in the buffer to spread
		# return early if there is no story in the buffer
		# Send the story through text-processing to convert to story-text
		# Send story-text to chosen neighbor (call sendMessage)
		pass

	def storyToText(self):
		# can use dummy values before a neural network module is set up
		pass

	def textToStory(self):
		# can use dummy values before a neural network module is set up
		pass
