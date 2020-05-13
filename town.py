import random

from names import townnames

townnamesdict = {x: 1 for x in townnames}

class Town:

	def __init__(self):
		name = random.choice(townnames)
		self.name = name 
		if townnamesdict[name] > 1:
			self.name += str(townnamesdict[name])
		townnamesdict[name] += 1

		# print("New town: {}".format(self.name))

	def id(self):
		return id(self)
