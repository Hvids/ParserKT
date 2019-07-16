import unittest
import sys
sys.path.append('/home/hvids/pract/parser')
from Dict import Dict
from File import FileOpen
from Example import Examples, Example

class TestDict(unittest.TestCase):
    def test_parser_dict(self):
        test_word = 'aba'
        File = FileOpen('test/dict.html')
        dict = Dict()
        dict.parserDict(File)
        self.assertEqual(dict.getWord(test_word).getWord(),test_word)

    def test_class_parse(self):
        dict = Dict()
        examples = Examples()
        file_dict  = FileOpen('test/dict.html')
        file_ex = FileOpen('test/input.html')
        dict.parserDict(file_dict)
        examples.parserExamples(file_ex)
        dict.updateExamplesInWord(examples)
        dict.writeDict('test/result.html')
        dict.printDict()
if __name__ == '__main__':
    unittest.main()
