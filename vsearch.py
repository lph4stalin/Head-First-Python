def search4vowels(phrase):
    return set('aeiou').intersection(set(phrase))


def search4letters(phrase, letters='aeiou'):
    return set(letters).intersection(set(phrase))
