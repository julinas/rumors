import random
#import timestamp module for timestamp in tryPUtInBuffer
#gives epoch time
import time
#imports sys to access max number used in  tryPopBuffer
import sys

class Agent:

	def __init__(self, nodeid):
		self.id = nodeid
		# the agent should have a buffer of recently-read stories
		# see tryPutInBuffer()
		self.buffer = {}
		# the agent should have a two small neural networks: 
		#  story-to-text and vice versa

	def id(self):
		return self.id

	def perceiveStory(self):
		# Asynchronously receive a story that spawns in the environment
		pass

	def sendMessage(self, message):
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
			print("Buffer is full")
			return None

	def pruneBuffer(self):
		# remove stories in the buffer that are too old
		# make the threshold for "too old" a variable so it's easy to tweak
		#86400 epoch seconds is one day
		old_threshold = time.time() - 86400 #subject to change
		for key in buffer:
			if (key > old_threshold):
				buffer.pop(key)
	
	def tryPopBuffer(self):
		#pops buffer and returns the story that is popped
		#else, returns gracefully

		if (len(buffer) > 0):
			firstKey = sys.float_info.max
			for key in buffer:
				if key < firstKey:
					firstKey = key
			buffer.pop(firstKey)
			return buffer[firstKey]
		else:
			print("Buffer is empty")
			return None

	def tryPopRandomFromBuffer(self):
		#pops a random element from the buffer
		#returns the random element / story
		randomKey = random.choice(list(buffer))
		buffer.pop(randomKey)
		return buffer[randomKey]

	def step(self):
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