import random
#import timestamp module for timestamp in tryPUtInBuffer
#gives epoch time
import time
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
class Agent:

	def __init__(self, nodeid):
		self.id = nodeid
		# the agent should have a buffer of recently-read stories
		# see tryPutInBuffer()
		self.buffer = []
		self.layers = keras.layers
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
			buffer.append((time.time(), message))
		else:
			print("Buffer is full")
			return None

	def pruneBuffer(self):
		# remove stories in the buffer that are too old
		# make the threshold for "too old" a variable so it's easy to tweak
		# any value BEFORE threshold will be deleted
		index_threshold = 4 #subject to change
		if (len(buffer) > index_threshold):
			buffer = buffer[index_threshold:]
		else:
			buffer.clear()

	def tryPopBuffer(self):
		#pops first element in buffer and returns the story that is popped
		#else, returns gracefully

		if (len(buffer) > 0):
			return buffer.pop(0)
		else:
			print("Buffer is empty")
			return None

	def tryPopRandomFromBuffer(self):
		#pops a random element from the buffer
		if (len(buffer) > 0):
			randomIndex = int(random.random()*len(buffer))
			return buffer.pop(randomIndex)
		else:
			print("Buffer is empty")
			return None

	def step(self):
		key = id(self)
		list = World.G.neighbors(key)
		neighbor = random.choice(list)
		story = self.tryPopRandomBuffer()
		if (story != None):
			text = self.storyToText(story)
			self.sendMessage(neighbor, text)
		# Decide the neighbor to spread a message to
		# Choose a story in the buffer to spread
		# return early if there is no story in the buffer
		# Send the story through text-processing to convert to story-text
		# Send story-text to chosen neighbor (call sendMessage)
		pass

	def storyToText(self, story):
		# can use dummy values before a neural network module is set up
		pass

	def textToStory(self, text):
		# sequential model
		url = "URL FOR DATABASE"
		path = tf.keras.utils.get_file(url.split('/')[-1], url)
		model = keras.Sequential()
		model.add(layers.Dense(20, activation = 'relu', input_shape = 10,))
		model.add(layers.Dense(20, activation = 'relu'))
		model.add(layers.Dense(20, activation = 'softmax'))

		model.fit(x, y, epochs = 10, batch_size = 32)
		# can use dummy values before a neural network module is set up
		pass
