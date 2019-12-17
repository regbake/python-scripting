from sys import exit

def gold_room():
	print("This room is full of gold. How much do you take?")

	choice = input("> ")
	if "0" in choice or "1" in choice:
		how_much = int(choice)
	else:
		dead("Man, learn to type a number.")

	if how_much < 50:
		print("Nice, you're not greedy, you win.")
		exit(0)
	else:
		dead('you greedy bb')

def bear_room():
	print("There's a bear here with honey. It's in front of another door, how will you move the beer?")

	bear_moved = False

	while True:
		choice = input("> ")

		if choice == "take honey":
			dead("The bear looks and slaps face")
		elif choice == "taunt bear" and not bear_moved:
			print("The bear has moved from door")
			print("You can go through now")

			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews leg. owie")
		elif choice == "open door" and bear_moved:
			gold_room()
		else:
			print("I got no idea what thaz meens")

def cthulhu_room():
	print("Here you see the evil Cthulhu")
	print("do you flee or eat your head?")

	choice = input("> ")

	if "flee" in choice:
		start()
	elif "head" in choice:
		dead("Well that was tasty")
	else:
		cthulhu_room()

def dead(why):
	print(why, "gg no r-e")
	exit(0)

def start():
	print('you are in a dark room')
	print('you are getting very sleepy. but there is a door to left and right')
	print('...')
	print('... which one will you take?')

	choice = input("> ")

	if choice == "left":
		bear_room()
	elif choice == "right":
		cthulhu_room()
	else:
		dead('you stumble around and starve')

start()



