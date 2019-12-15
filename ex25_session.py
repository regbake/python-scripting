import ex25

print('all good in session')

sentence = 'this is a test sentence and yadaadayada'
words = ex25.break_words(sentence)

sorted_words = ex25.sort_words(words)
reverse_sorted_words = ex25.reverse_sort_words(words)


print(f'sorted words are {sorted_words}')
print(f'reverse sorted words are {reverse_sorted_words}')