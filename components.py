import copy
import inflect
import random

from frames import frames
from names import layseggsnames, animalnames, vegetablenames, thingnames, neighbornames

infEngine = inflect.engine()

class TextMain:
	"""
	This class should draw from a database instead of doing rigid selection of frames/variables
	"""

	def __init__(self):
		self.randomFrame()

	def randomFrame(self):
		self.frame = copy.deepcopy(random.choice(frames))
		for v in self.frame['vars']:
			if v['type'] is 'name':
				namelist = None
				if v['list'] is 'layseggsnames':
					namelist = layseggsnames
				elif v['list'] is 'animalnames':
					namelist = animalnames
				elif v['list'] is 'vegetablenames':
					namelist = vegetablenames
				elif v['list'] is 'thingnames':
					namelist = thingnames
				v['name'] = random.choice(namelist)

	def mutate(self, event):
		pick1 = random.choice(list(range(len(self.frame['vars']))))
		v = self.frame['vars'][pick1]

		if v['type'] is 'num':
			if v['dir'] is 'up':
				# try rounding up
				if round(v['num'], -1) > v['num']:
					v['num'] = round(v['num'], -1)
				else:
					v['num'] += 1
				event.isRumor = True
			elif v['dir'] is 'down':
				num = v['num']
				if round(num, -1) < v['num']:
					num = round(num, -1)
				else:
					num = list(str(num))
					random.shuffle(num)
					if num[0] == '0':
						num = v['num'] - 1
					else:
						num = ''.join(num)
					num = int(num)
					if num > v['num']:
						num = v['num'] - 1
				if num > v['min']:
					v['num'] = num
				event.isRumor = True
			else:
				pass
		elif v['type'] is 'name':
			if v['name'] in neighbornames:
				neighborlist = neighbornames[v['name']]
				v['name'] = random.choice(neighborlist)
				event.isRumor = True
			else:
				pass
		else:
			pass


	def text(self):
		text = self.frame['frame'].copy()
		for v in self.frame['vars']:
			if v['type'] is 'num':
				if v['num'] == 1:
					nums = infEngine.a(text[v['pos']]).split()
					text.insert(v['pos'], nums[0])
				else:
					vartext = str(v['num'])					
					text.insert(v['pos'], vartext)
					if len(text) > v['pos']+1:
						text[v['pos']+1] = infEngine.plural(text[v['pos']+1], v['num'])

			elif v['type'] is 'name':
				vartext = v['name']
				text.insert(v['pos'], vartext)
			

		text = ' '.join(text)
		return text