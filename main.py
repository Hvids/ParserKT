from parser.Dict import Dict
from parser.Example import Examples
from parser.File import FileOpen
if __name__ == '__main__':
    dict = Dict()
    examples = Examples()
    file_dict  = FileOpen('dict.html')
    file_ex = FileOpen('input.html')
    print('Parse Dict')
    dict.parserDict(file_dict)
    print('Parse Example')
    examples.parserExamples(file_ex)
    print('Add Example')
    dict.updateExamplesInWord(examples)
    print('Write Dict')
    dict.writeDict('result.html')
