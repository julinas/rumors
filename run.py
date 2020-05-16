from world import World

if __name__ == "__main__":
	n = 50
	k = 6 # Each node is joined with its k nearest neighbors in a ring topology
	p = 0.1 # The probability of adding a new edge for each edge
	steps = 5000
	catchRumors = True

	world = World(n, k, p, log=True, catchRumors=catchRumors)
	world.run(steps)

	# analysis log
	trueEvents = [x for x in world.events.values() if x.isRumor == False]
	rumors = [x for x in world.events.values() if x.isRumor]
	caughtRumors = [x for x in world.events.values() if x.isCaughtRumor]

	print("n={} k={} p={}".format(n, k, p))
	print("catchRumors is {}".format(catchRumors))
	print("simulated {} steps".format(steps))
	print("{} events".format(len(trueEvents)))
	print("{} rumors".format(len(rumors)))
	print("{} caught rumors".format(len(caughtRumors)))
	

