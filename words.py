import pickle
import os
words = []


class WordHolderClass:  # defined in order to be saved in pickle
    def __init__(self):
        pass

    word_list = {}

    def list_words(self):
        print(self.word_list)

    def get_top_words(self, all=False):
        top_words_dict = sorted(self.word_list.items(), key=lambda kv: kv[1])
        top_words_list = []

        for kvp_word in top_words_dict:  # "kvp" = key-value pair
            top_words_list.append(kvp_word[0])  # grabs the word out of the KVP, dropping the count.

        top_words = list(reversed(top_words_list))  # change from least to greatest to Greatest to least.

        if all:  # if all is set to true, return EVERY word in order
            return top_words
        return top_words[:20]  # otherwise, return only the first 20 top words


wh = WordHolderClass()  # init the class. "wh" = word_holder


def add(word):
    words.append(word.lower().strip())  # clean before entry


def dump():
    global words  # call from outside the dump() scope.

    for word in words:
        if word in wh.word_list:
            wh.word_list[word] += 1
        else:
            wh.word_list[word] = 1

    words = []


def save(object):
    filename = get_full_path("wordlist")

    with open(filename, "wb") as fout:
        pickle.dump(object, fout)


def get_full_path(name):
    """
    This method takes a string "name" and returns the named file's filepath.
    :param name: The name of the account file
    :return: The full path of a .txt file
    """
    return os.path.abspath(os.path.join('.', 'lists', name + '.wrds'))


# remove non-alpha characters
def clean(word_input):
    return ''.join(filter(str.isalpha, word_input))


if __name__ == '__main__':
    print(get_full_path("wordlist"))

    for i in range(25):
        word = input(">>>").lower().strip()
        add(word)
    dump()
    wh.list_words()
    print(wh.get_top_words())
