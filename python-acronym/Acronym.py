import re
import numpy as np


# Method initialization
def abbreviate(phrase) -> str:
    # Variables initialization
    acronym = ""
    # Format sanitized
    phrase = phrase.replace('-', ' ')
    # Sentence to Arrqy
    arr_phrase = phrase.split()

    # Check the for CamelCase case, if is the case, split the word into an array
    # Add the new array in the current
    for i in range(len(arr_phrase)):
        if re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', arr_phrase[i]):
            arr_phrase[i] = re.sub('([A-Z][a-z]+)', r' \1', re.sub('([A-Z]+)', r' \1', arr_phrase[i])).split()

    # Concatenate Sub Array(s) with main array
    arr_phrase = (np.hstack(arr_phrase))

    # For each items, make the first letter in uppercase and Concatenate everyt letters
    # for creating and returning our acronym
    for i in range(len(arr_phrase)):
        acronym += arr_phrase[i][0].upper()

    return acronym


class Acronym:
    pass
