townnames = ["Leanssephtown", "Hopemillshill", "Brixbournemen Park", "Saint Dowtuck", "Bayridge", "Victoria", "Southbay", "Burghhor", "Genesis", "Spoons"]
layseggsnames = ["chicken", "duck"]
catnames = ["cat", "tiger"]
otheranimalnames = ["dog"]
animalnames = layseggsnames + catnames + otheranimalnames
fruitnames = ["watermelon", "apple"]
vegetablenames = ["pumpkin", "squash", "tomato", "cucumber"]
plantnames = vegetablenames + fruitnames
thingnames = animalnames + vegetablenames

neighbornames = {
	"chicken": ["duck"],
	"duck": ["chicken"],
	"cat": ["tiger", "dog", "cucumber"],
	"dog": ["cat"],
	"tiger": ["cat"],
	"pumpkin": ["squash"],
	"squash": ["pumpkin", "cucumber"],
	"cucumber": ["squash", "tomato", "cat", "watermelon"],
	"tomato": ["cucumber", "apple"],
	"watermelon": ["cucumber", "apple"],
	"apple": ["tomato", "watermelon"]
}