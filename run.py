from world import World

if __name__ == "__main__":
	n = 100
	k = 6 # Each node is joined with its k nearest neighbors in a ring topology
	p = 0.1 # The probability of adding a new edge for each edge
	steps = 5000
	catchRumors = False
	runs = 100

	print("n={} k={} p={}".format(n, k, p))
	print("catchRumors is {}".format(catchRumors))
	print("simulated {} steps per run".format(steps))

	print("simulating {} runs".format(runs))

	numEvents = []
	numRumors = []
	numCaughtRumors = []

	for i in range (runs):

		world = World(n, k, p, log=False, catchRumors=catchRumors)
		world.run(steps)

		# analysis log
		trueEvents = [x for x in world.events.values() if x.isRumor == False]
		rumors = [x for x in world.events.values() if x.isRumor]
		caughtRumors = [x for x in world.events.values() if x.isCaughtRumor]

		numEvents.append(len(trueEvents))
		numRumors.append(len(rumors))
		numCaughtRumors.append(len(caughtRumors))

		# print("{} events".format(len(trueEvents)))
		# print("{} rumors".format(len(rumors)))
		# print("{} caught rumors".format(len(caughtRumors)))
		print("world ran")

	print("numEvents")
	print(numEvents)
	print("numRumors")
	print(numRumors)
	print("numCaughtRumors")
	print(numCaughtRumors)
	

