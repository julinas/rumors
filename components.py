import copy
import random

from frames import frames
from names import animalnames, vegetablenames, thingnames

class TextMain:

	frame = None

	def __init__(self):
		self.randomFrame()

	def randomFrame(self):
		self.frame = copy.deepcopy(random.choice(frames))
		for v in self.frame['vars']:
			if v['type'] is 'name':
				namelist = None
				if v['list'] is 'animalnames':
					namelist = animalnames
				elif v['list'] is 'vegetablenames':
					namelist = vegetablenames
				elif v['list'] is 'thingnames':
					namelist = thingnames
				v['name'] = random.choice(namelist)

	def mutate(self):
		pick1 = random.choice(list(range(len(self.frame['vars']))))
		v = self.frame['vars'][pick1]

		if v['type'] is 'num':
			if v['dir'] is 'up':
				v['num'] += 1
		elif v['type'] is 'name':
			namelist = None
			if v['list'] is 'animalnames':
				namelist = animalnames
			elif v['list'] is 'vegetablenames':
				namelist = vegetablenames
			elif v['list'] is 'thingnames':
				namelist = thingnames
			v['name'] = random.choice(namelist)


	def text(self):
		text = self.frame['frame'].copy()
		for v in self.frame['vars']:
			vartext = None
			if v['type'] is 'num':
				vartext = str(v['num'])
			elif v['type'] is 'name':
				vartext = v['name']
			text.insert(v['pos'], vartext)

		text = ''.join(text)
		return text