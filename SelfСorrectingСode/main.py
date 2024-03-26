import random

from hamming_code import *


data = [random.randint(0, 1) for i in range(11)]
print("Data:", data)
encoded_data = hamming_code(data)
print("hamming", hamming_encode(data))
print()
# FIXME: I dont know why, but encode not always work
print(hamming_syndrome(encoded_data))
print("Encoded Data:           ", encoded_data)
encoded_data[5] ^= 1
print("Encoded Data with error:", encoded_data)
decoded_message = hamming_decode(encoded_data)
print()
print("Decoded Data:", decoded_message)
print("Decoded Data:", decoded_message == data)
