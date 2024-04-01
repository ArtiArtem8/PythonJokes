import random

from hamming_code import *


data = [random.randint(0, 1) for i in range(4)]
# data = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# data = [0, 0, 0, 1]
data = [1, 0, 0, 0, 0]
# data = list(map(int, input("Enter data: ")))
print("Data:", p(data))
print()

encoded_data = hamming_encode(data)
print("Encoded Data:           ", p(encoded_data))

encoded_data[random.randint(0, len(encoded_data) - 1)] ^= 1
print("Encoded Data with error:", p(encoded_data))

decoded_message = decode(encoded_data)
print()
print("Decoded Data:", p(decoded_message))
print("Decoded Data:", ["Fail", "Success"][decoded_message == data])
