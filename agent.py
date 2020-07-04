import random
#import timestamp module for timestamp in tryPUtInBuffer
#gives epoch time
import time

#for the Sequential model
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import pandas as pd
import numpy as np

class Agent:

	def __init__(self, nodeid):
		self.id = nodeid
		# the agent should have a buffer of recently-read stories
		# see tryPutInBuffer()
		self.buffer = []
		# the agent should have a two small neural networks: 
		self.model = keras.Sequential()
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
		# Decide the neighbor to spread a message to
		# Choose a story in the buffer to spread
		# return early if there is no story in the buffer
		# Send the story through text-processing to convert to story-text
		# Send story-text to chosen neighbor (call sendMessage)
		pass

	def storyToText(self, story, frame, variable):
		# can use dummy values before a neural network module is set up

		#data preparation - needs FrameNet
		# the data, split between train and test sets
		data = # the dataset: currently unavailable
		output = # expected output of model 

		#NEW METHOD: assume there's already a trained model that does the conversion
		tensor = turnStoryToInput(story, frame, variable)

		#build neural network
		model.add(tf.keras.Input(shape=(16,)))
		model.add(layers.Dense(10, activation = 'relu'))
		model.add(layers.Dense(10, activation = 'relu'))
		model.add(layers.Dense(3, activation = 'relu'))

		model.compile(optimizer='adam', loss='categorical_crossentropy')

		#NEW METHOD: pre-written train method, includes model.fit() and model.compile()
		trainStoryToText(model, tensor, output)
		
		#returns a numpy array of predictions
		arr = model.predict(tensor)

		#convert numpy array to string
		text = np.array2string(arr)

		return str(text + frame)

	def textToStory(self):
		# can use dummy values before a neural network module is set up
		pass