import time
# some classes

class my_class():
	def __init__(self, name, color):
		self.name = name
		self.color = color

		print(f'just init the {name} class with a {color} color')

	def say_hello(self, tone: str) -> None:
		print('from say_hello... self.name is: ', self.name)

		if 'mad' in tone:
			print('it is okay do not be mad')
		elif 'sad' in tone or 'sorry' in tone:
			print('you should be glad instead')
		elif 'su-yee' in tone:
			print('oh bb i love your ways')
		else:
			print('haha okay')

	def random_number(self):
		this_time = time.gmtime()

		print('this_time is: ', this_time.tm_hour)

instance = my_class(name="reginaldo", color="cornflowerblue")

instance.say_hello(tone='something thine blah blah but so sorry')
instance.say_hello(tone='hehe haha')
instance.say_hello(tone='love ya su-yee')

instance.random_number()