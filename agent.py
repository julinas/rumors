import random
#import timestamp module for timestamp in tryPUtInBuffer
#gives epoch time
import time
import numpy as np
import pandas
from tensorflow import keras
from tensorflow.keras import layers
from keras.preprocessing.text import text_to_word_sequence
from keras. preprocessing.text import one_hot
from world import World
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
	# Note to Kelly: I added text, so may not be needed
	def textToStory(self, text):
		# sequential model
		#TODO: Ask if method will take from database, if does, delete 104-6

		### if text not provided
		url = "URL FOR DATABASE"
		path = tf.keras.utils.get_file(url.split('/')[-1], url)
		data = pandas.read_csv(path)
		data = data[pandas.notnull(data['subject'])]
		data = data[pandas.notnull(data['action'])]
		# TODO: add as necessary
		train_size = int(len(data) * .8)
		train_subjects = data['subject'][:train_size]
		train_verbs = data['verb'][:train_size]

		test_subjects = data['subject'][:train_size]
		test_verbs = data['verb'][:train_size]

		tokenize = keras.preprocessing.text.Tokenizer(num_words = 10000, char_level = False)

		###

		### if text is a sentence
		url = "URL FOR DATABASE"
		path = tf.keras.utils.get_file(url.split('/')[-1], url)
		data = pandas.read_csv(path)
		data = data[pandas.notnull(data['Text'])]

		train_size = int(len(data) * .8)

		train_text = data['Text'][:train_size]
		test_text = data['Text'][:train_size]

		tokenize = keras.preprocessing.text.Tokenizer(num_words = 10000, char_level = False)
		tokenize.fit_on_texts()

		text_bow_train = tokenize.texts_to_matrix(train_text)
		text_bow_train = tokenize.texts_to_matrix(test_text)

		encoder = LabelEncoder()
		encoder.fit(train_text)
		train_text = encoder.transform(train_text)
		test_text = encoder.transform(test_text)

		num = np.max(train_text) + 1

		train_text = keras.utils.to_categorical(train_text, num)
		test_text = keras.utils.to_categorical(test_text, num)
		###

		### If text provided
		tokens = text_to_word_sequence(text)
		words = set(text_to_word_sequence(text))
		vocab_size = len(words)
		result = one_hot(text, round(vocab_size * 1.3))

		train_size = int(len(tokens) * .8)
		train_subjects = tokens['subject'][:train_size]
		train_verbs = tokens['verb'][:train_size]

		test_subjects = tokens['subject'][:train_size]
		test_verbs = tokens['verb'][:train_size]
		###


		model = keras.Sequential(
    		[
				keras.Input(shape = len(tokens)),
		        layers.Conv2D(32, 5, strides=2, activation="relu"),
				layers.Conv2D(32, 3, activation="relu")
				layers.Dense(32, activation='relu')
    		]
		)
		model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
		model.fit(tokens, y, epochs = 10, batch_size = 32)
		model = model.evaluate(x_test, y_test, verbose=0)
		node = World.getRandomNode()
		story = Story(World, node, upstream) # What is upstream?
		# can use dummy values before a neural network module is set up
		pass
