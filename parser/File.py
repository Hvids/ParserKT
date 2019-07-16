class FileOpen:
    def __init__(self, name):
        self.__file = open(name,'r',encoding = 'utf-8').read()
    def getState(self):
        return self.__file[self.__file.find('<p>')+3:self.__file.find('</p>')]
    def isEmpty(self):
        return self.__file.find('<p>') == -1
    def cutAfterP(self):
        self.__file = self.__file[self.__file.find('</p>')+4:]
    def getFile(self):
        return self.__file

class FileWrite:
    def __init__(self,name):
        self.__file = open(name,'w')
    def write(self,str):
        self.__file.write(str)
    def writeWord(self,word):
        self.__file.write('<b>')
        self.__file.write(word.getWord()+ ' ')
        self.__file.write('</b>')
        self.__file.write(word.getTrans())
        if (len(word.getExample()) != 0):
            self.__file.write('; ')
        for example in word.getExample():
            if example == word.getExample()[-1]:
                self.__file.write('<b>')
                self.__file.write(example.getText() + ' ')
                self.__file.write('</b>')
                self.__file.write(example.getTrans()+ ' ')
                break
            self.__file.write('<b>')
            self.__file.write(example.getText()+ ' ')
            self.__file.write('</b>')
            self.__file.write(example.getTrans()+ ' ')
