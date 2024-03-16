def is_pangram(phrase='')->bool:

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in alphabet:
        if letter not in phrase.lower():
            return False

    return True