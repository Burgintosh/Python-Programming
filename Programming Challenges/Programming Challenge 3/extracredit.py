url = "http://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt"
import os
from urllib.request import urlopen
wordfile = urlopen(url)
words = wordfile.read().decode('utf-8').upper().split() # List of all words

# Order the strings in alphabetical order, create a dictionary using the alphabetically ordered string as the key and a list containing the words that form that string as the value.
# Then prompt user for input word. Put it in alphabetical order, use that to get list from dictionary, and loop through alphabet, adding each one to the base and pulling those lists of words.
def create_dictionary():
    english_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        try:
            english_dict[sorted_word].append(word)
        except KeyError:
            english_dict[sorted_word] = [word]
    return english_dict 

def allsteps(base_word):
    '''
    >>> allsteps("APPLE")
    ['ALEPPO', 'APPEAL', 'CAPPLE', 'DAPPLE', 'LAPPED', 'LAPPER', 'LAPPET', 'PALPED', 'PAPULE', 'RAPPEL', 'UPLEAP']

    >>> allsteps("UC")
    ['CUB', 'CUD', 'CUE', 'CUM', 'CUP', 'CUR', 'CUT', 'LUC', 'UCA']

    >>> allsteps("BEARCAT")
    ['ACERBATE', 'BACTERIA', 'BRACCATE', 'BRACTEAL', 'CARTABLE', 'SCABRATE']

    '''
    
    #alphabet = [chr(ord('A') + i) for i in range(26)] # Should create list of alphabet characters, all capitals because we use upper() method later.
    #english_dict = create_dictionary()
    step_words = []

    base_word = base_word.upper()
    base_word_sorted = ''.join(sorted(base_word))
    for letter in alphabet:
        find_steps = base_word + letter
        find_steps_sorted = ''.join(sorted(find_steps))
        if(not english_dict.get(find_steps_sorted) == None):
            step_words += english_dict[find_steps_sorted]
    step_words.sort()
    return step_words

def longest_ladder(word):
    paths = []
    current_steps = allsteps(word)
    if(len(current_steps) <= 0):
        return 1
    for step in current_steps:
        paths.append(longest_ladder(step))
    return 1 + max(paths)

alphabet = [chr(ord('A') + i) for i in range(26)] 
english_dict = create_dictionary()
base_word = input("Enter a word to find longest ladder of: ")
print(longest_ladder(base_word))


import doctest
if __name__ == "__main__":
    doctest.testmod(verbose=True)
