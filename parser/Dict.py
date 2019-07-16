import sys
sys.path.append('/home/hvids/pract/parser')

from Word import Word
from File import FileOpen, FileWrite
from State import State
from Example import Example
from Key import KeyAdder, KeysAdder, KeysWriter
class Dict:
    def __init__(self):
        self.__dict = {}
    def getWord(self,word):
        return self.__dict[word]
    def parserDict(self, File):
        while not File.isEmpty():
            state = State(File)
            word = Word()
            word.createWord(state)
            _word = word.getWord()
            self.__dict[_word] = word
            File.cutAfterP()
    def printDict(self):
        for key in self.__dict.keys():
            print('_____')
            print('Word: ' + self.__dict[key].getWord())
            print(' Trans: ' + self.__dict[key].getTrans())
            print(' Example:')
            for ex in self.__dict[key].getExample():
                print('     Text:',ex.getText())
                print('     Trans:',ex.getTrans())
    def __addExample(self,key_adder,example):
        self.__dict[key_adder.key].addExample(example)
    def updateExamplesInWord(self, examples):
        keys_adder = KeysAdder(self.__dict)
        for example in examples.getExamples():
            example.createListText()
            for word_example in example.getListText():
                key_adder = KeyAdder()
                key_adder.findKey(keys_adder, word_example)
                if  key_adder.isEmpty() == False:
                    example.replaceTilda(key_adder)
                    self.__addExample(key_adder,example)
    def writeDict(self,name):
        fwrite = FileWrite(name)
        keys_writer = KeysWriter(self.__dict)
        fwrite.write('<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"></head><body>')
        keys_writer.sortKey()
        for key in keys_writer.getKeys():
            fwrite.write('<p>')
            fwrite.writeWord(self.__dict[key])
            fwrite.write('</p>')
        fwrite.write('</body></html>')
