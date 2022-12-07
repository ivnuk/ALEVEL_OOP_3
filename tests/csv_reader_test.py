from unittest import TestCase
from unittest.mock import patch, mock_open

from words.data_reader import CSVGetter

READ_DATA = "header\nword1\nword2\nword3\n"


def get_rand(*args):
    return 'abc'


class CSVReaderTestCase(TestCase):
    # employees.employee.Employee.save
    @patch('builtins.open', mock_open(read_data=READ_DATA))
    def test_get_random_word_return_word(self):
        getter = CSVGetter("fakefile")
        word = getter.get_random_word()
        self.assertIn(word, READ_DATA.split("\n"))

    @patch('words.data_reader.CSVGetter.get_random_word', new=get_rand)
    def test_get_random_word_mocked(self):
        reader = CSVGetter('dummy_file')
        word = reader.get_random_word()  # get_rand()
        self.assertEqual(word, 'abc')
