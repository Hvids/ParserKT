import sys
sys.path.append('/home/hvids/pract/parser')

from ord_dict import ord_dict
from quickSort import quickSort
class KeyAdder:
    def __init__(self):
        self.key = ''
        self.replace_words = []
        self.replace_word = ''
    def __str__(self):
        return self.key
    def isEmpty(self):
        return self.replace_word == ''
    def findKey(self,keys,word):
        for key in keys.getKeys():
            for replace_word in key.replace_words:
                if word.find(replace_word) == 0 and word[len(replace_word):].find(replace_word) == -1:
                    if word == replace_word:
                        self.key = key.key
                        self.replace_word = replace_word
                        break
                    if self.key == '':
                        self.key = key.key
                        self.replace_word = replace_word
                    elif len(self.replace_word) < len(replace_word):
                        self.key = key.key
                        self.replace_word = replace_word
class KeysAdder:
    def __init__(self):
        self.__keys = []
    def __init__(self,dict):
        self.__keys = []
        for key in dict.keys():
            new_key = KeyAdder()
            new_key.key = key
            act = False
            if key.find('|')!=-1:
                new_key.replace_words.append(key[:key.find('|')])
                act = True
            elif key.find('@')!=-1:
                new_key.replace_words.append(key[:key.find('@')])
                act = True
            elif key.find('&')!=-1:
                new_key.replace_words.append(key[:key.find('&')])
                new_key.replace_words.append(key[key.find('&')+2:-1].replace(')',''))
                act = True
            else:
                if key.find(')')!=-1:
                    new_key.replace_words.append(key.replace(')',''))
                    act = True
                if key.find('-')!=-1:
                    new_key.replace_words.append(key.replace('-',''))
                    act = True
                if key.find('(')!=-1:
                    new_key.replace_words.append(key.replace('(',''))
                    act = True
            if act == False:
                new_key.replace_words.append(key)
            self.__keys.append(new_key)
    def getKeys(self):
        return self.__keys


class KeysWriter:
    def __init__(self,dict):
        self.__keys = list(dict.keys())

    def getKeys(self):
        return self.__keys
    def sortKey(self):
        self.__keys = quickSort(self.__keys)
    def getSort(self):
        return self.__keys
