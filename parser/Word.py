import sys
sys.path.append('/home/hvids/pract/parser')

from State import State
from Example import Example
class Word:
    def __init__(self):
        self.__word = ''
        self.__trans = ''
        self.__example = []
    def createWord(self,State):
        self.__word = State.getWord()
        State.cutAfterB()
        self.__trans = State.getWordTrans()
        while not State.isEmpty():
            State.cutBeforeB()
            example = Example()
            text = State.getExampleText()
            example.setText(text)
            State.cutAfterB()
            trans = State.getExampleTrans()
            example.setTrans(trans)
            self.__example.append(example)
    def addExample(self,example):
        self.__example.append(example)
    def getWord(self):
        return self.__word
    def getTrans(self):
        return self.__trans
    def getExample(self):
        return self.__example
