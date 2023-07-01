
import string
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('words')

from nltk.corpus import words

word_list = words.words()
all_letters = string.ascii_letters

divided_dict = dict()
strtWords = ''

for letter in all_letters:
    divided_dict[letter] = [word for word in word_list if word.startswith(letter)]

word = 'htlaufe'
constant = 'h'
anagrams = []
wordsWithConstant = []

# for letter in all_letters:
#     for char in word:
#         if letter == char:
#             strtWords+=(str(divided_dict[letter]))

def contains(word, anagram): 
	for letter in anagram: 
		if letter not in word: 
			return False 
	return True 

def wordChecker(word, constant):
    for section in [divided_dict[letter] for letter in word]:
        for small_word in section:
                if contains (word,small_word):
                    anagrams.append(small_word)


    for each in anagrams:
        if constant in each:
            if len(each) > 3:
                if each not in wordsWithConstant:
                    wordsWithConstant.append(each)
    return(wordsWithConstant)

new_check = wordChecker('lgpfino', 'f')
print(new_check)