# lexicon

lexicon = {
    "north" : "direction",
}


def scan(sentence):
    """Scans sentences given by user"""
    result = []
    words = sentence.split()
    for word in words:
        word_type = lexicon.get(word)
        result.append((word_type, word))

    return result



def split_words(words):
    """Takes the word/sentence provided as argument and splits them"""
    return words.split()
