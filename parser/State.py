import sys
sys.path.append('/home/hvids/pract/parser')

from File import FileOpen
class State:
    def __init__(self, File):
        self.__state = File.getState()
    def cutAfterB(self):
        self.__state = self.__state[self.__state.find('</b>')+4:]
    def cutBeforeB(self):
        self.__state = self.__state[self.__state.find('<b>')+3:]
    def getWord(self):
        return self.__state[3:self.__state.find('</b>')]
    def getWordTrans(self):
        if self.__state.find('<b>') ==-1:
            return self.__state
        else:
            return self.__state[:self.__state.find(';')]
    def getExampleText(self):
        return self.__state[self.__state.find('<b>')+3:self.__state.find('</b>')]
    def getExampleTrans(self):
        if self.__state.find('</b>') == -1:
            return self.__state + ''
        else:
            return self.__state[:self.__state.find(';')] + ''
    def isEmpty(self):
        return self.__state.find('<b>') == -1
