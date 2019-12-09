# first python script
# scripting and general

first_array = ['first entry', 'second', 'third']
second_array = ['first', 'second', 'third']

obj_first = {
	'one': 1,
	'two': 2,
	'three': 3,
	'four': 4
}

obj_second = {
	'one': 1,
	#'first_array': first_array,
	#'second_array': second_array,
	'four': 4
}


# 1. find the common entries between first and second
# 2. find the differences between the first and second

common = obj_first.keys() & obj_second.keys()
different_first = obj_first.keys() - obj_second.keys()
different_second = obj_second.keys() - obj_first.keys()

common_pairs = obj_first.items() & obj_second.items()
diff_second_pairs = obj_second.items() - obj_first.items()


# print('common is: ', common)
# print('different_first is: ', different_first)
# print('different_second is: ', different_second)

print('common_pairs are: ', common_pairs)
