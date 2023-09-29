import re

from dictionary import tr_words


def search(pattern):
    for word in tr_words:
        if re.fullmatch(pattern, word.strip()):
            yield word