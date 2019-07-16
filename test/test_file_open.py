import unittest
import sys
sys.path.append('/home/hvids/pract/parser')
from FileOpen import FileOpen

class TestFileOpen(unittest.TestCase):

    def test_get_state(self):
        test_state = "<b>a</b> ага;  <b>~, tutuldıñmı!</b> ага, попался!; <b>~ñl~dıñmı? – ebet, ~ñl~dım.</b> понял? – ага, понял."
        file = FileOpen('test/dict.html')
        self.assertEqual(file.getState(),test_state, "Should be 6")
    def test_is_empty(self):
        file_empty = FileOpen('test/test_dict_empty.html')
        file = FileOpen('test/dict.html')
        self.assertEqual(file.isEmpty(),False)
        self.assertEqual(file_empty.isEmpty(),True)
    def test_is_cut_after_p(self):
        test_state = '<b>abit&(abdi)</b> невольник'
        file = FileOpen('test/dict.html')
        file.cutAfterP()
        self.assertEqual(file.getState(),test_state)

if __name__ == '__main__':
    unittest.main()
