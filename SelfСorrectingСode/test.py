import unittest
from hamming_code import *

def num_to_bit_list(num):
    int.bit_length()
    bit_list = [(num >> shift_ind) & 1
                for shift_ind in range(num.bit_length())]
    bit_list.reverse()

    return bit_list
class MyTestCase(unittest.TestCase):
    def test_evil_test(self):
        length = 16
        for i in range(2**length):
            data = num_to_bit_list(i)
            encoded_data = hamming_encode(data)
            decoded_data = decode(encoded_data)
            self.assertEqual(data, decoded_data)


if __name__ == '__main__':
    unittest.main()
