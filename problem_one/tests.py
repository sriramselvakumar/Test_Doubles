import unittest

import os

from sum import sum_up


class SumTests(unittest.TestCase):
    # Dummy
    def test_file_exist_check(self):
        with self.assertRaises(FileNotFoundError):
            sum_up('real_madrid.txt')
    # Dummy

    def test_type_conversion(self):
        with self.assertRaises(ValueError):
            line = '3,5.6'
            txt = open('type_conversion.txt', 'w+')
            txt.write(line)
            txt.close()
            sum_up('type_conversion.txt')

        os.remove('type_conversion.txt')

    # @Mock
    def test_summing(self):
        line = '3 5'
        txt = open('sum_test.txt', 'w+')
        txt.write(line)
        txt.close()
        sum_up('sum_test.txt')
        txt_file = open('sum_test.txt', 'r')
        line = txt_file.read()
        txt_file.close()
        numbers = line.split(' ')
        result = numbers[len(numbers)-1]
        self.assertEqual('8', result)
        os.remove('sum_test.txt')
