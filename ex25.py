# will import later and act as API

def break_words(str):
	split_words = str.split(' ')

	return split_words

def sort_words(words):
	return sorted(words)

def reverse_sort_words(words):
	return sorted(words, reverse=True)	

def print_first_word(words):
	word = words.pop(0)
	print(word)

def print_last_word(words):
	words = words.pop(-1)	

def sort_sentence(sentence):
	words = break_words(sentence)

	return sort_words(words)