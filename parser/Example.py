import sys
sys.path.append('/home/hvids/pract/parser')

from State import State
class Example:
    def __init__(self):
        self.__text = ''
        self.__trans = ''
        self.__list_text = []
    def getText(self):
        return self.__text
    def getTrans(self):
        return self.__trans
    def setText(self,new_text):
        self.__text = new_text
    def setTrans(self,new_trans):
        self.__trans = new_trans
    def createListText(self):
        self.__list_text = self.__text.split(' ')
    def getListText(self):
        return self.__list_text
    def replaceTilda(self,key):
        self.__text = self.__text.replace(key.replace_word,'~')

class Examples:
    def __init__(self):
        self.__examples = []
    def parserExamples(self,File):
        while not File.isEmpty():
            state = State(File)
            example = Example()
            text = state.getExampleText()
            example.setText(text)
            state.cutAfterB()
            trans = state.getExampleTrans()
            example.setTrans(trans)
            self.__examples.append(example)
            File.cutAfterP()
    def getExamples(self):
        return self.__examples
    def getExample(self,index):
        return self.__examples[index]
    def printExamples(self):
        for ex in self.__examples:
            print('_____')
            print('Text: ',ex.getText())
            print('Trans: ', ex.getTrans())
