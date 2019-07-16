import unittest
import sys
sys.path.append('/home/hvids/pract/parser')
from Example import Examples
from FileOpen import FileOpen
class TestExample(unittest.TestCase):
    def test_examples(self):
        file = FileOpen('test/input.html')
        exs = Examples()
        exs.parserExamples(file)
        self.assertEqual(exs.getExample(0).getText(),'şeer civarı')
if __name__ == '__main__':
    unittest.main()
