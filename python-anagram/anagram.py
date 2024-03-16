#Detect anagrams Method
def detect_anagrams(base_word='', words_list=None):
    if words_list is None: #Check if word list is not null
        words_list = []
    anagrams = [] #Prepare an empty list
    base_word = base_word.casefold() #lowercase our base word
    for word in words_list: #Compare each item with base word
        lower_word = word.casefold()
        if lower_word != base_word:
            if sorted(lower_word) == sorted(base_word):
                anagrams.append(word)

    return anagrams

