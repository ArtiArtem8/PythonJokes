import operator
from functools import reduce


#
# def encode(data):
#     p1 = data[0] ^ data[1] ^ data[3]
#     p2 = data[0] ^ data[2] ^ data[3]
#     p3 = data[1] ^ data[2] ^ data[3]
#     encoded_data = [p1, p2, data[0], p3, data[1], data[2], data[3]]
#     return encoded_data
#
#
# def decode(received_data):
#     s1 = received_data[0] ^ received_data[2] ^ received_data[4] ^ received_data[6]
#     s2 = received_data[1] ^ received_data[2] ^ received_data[5] ^ received_data[6]
#     s3 = received_data[3] ^ received_data[4] ^ received_data[5] ^ received_data[6]
#     error_position = s1 + 2 * s2 + 4 * s3
#     if error_position > 0:
#         corrected_bit = received_data[error_position - 1]
#         received_data[error_position - 1] = 1 - corrected_bit
#     original_data = [received_data[2], received_data[4], received_data[5], received_data[6]]
#     return original_data
#
#

#
#
# def prepare_data(data):
#     n = len(data)
#     i = 0
#     j = 0
#     k = 0
#     while i + j < n + k:
#         if j == (2 ** i - 1):
#             i += 1
#         else:
#             k += 1
#         j += 1
#     return [0 if i == (2 ** j - 1) else data[-k] for i in range(n + j)]
#
#
# def calculate_parity_bits(arr):
#     n = len(arr)
#     for i in range(n):
#         if arr[i] == 0:
#             parity_pos = 2 ** i
#             xored = 0
#             for j in range(1, n + 1):
#                 if j & parity_pos and j != parity_pos:
#                     xored ^= int(arr[-j])
#             arr[-parity_pos] = str(xored)
#     return arr
#
#
# def hamming_code(data):
#     # Определение количества проверочных битов
#     r = 0
#     while 2 ** r < len(data) + r + 1:
#         r += 1
#
#     # Создание кодового слова с нулевыми проверочными битами
#     code = [0] * (len(data) + r)
#
#     # Заполнение кодового слова данными
#     j = 0
#     for i in range(len(code)):
#         if i + 1 not in [2 ** k for k in range(r)]:
#             code[i] = int(data[j])
#             j += 1
#
#     print(code)
#     # Вывод таблицы четности
#     table = []
#
#     for i in range(r):
#         a = [0] * len(code)
#
#         for j in range((2 ** i) - 1, len(code), (2 ** (i + 1))):
#             count = 0
#             while count < 2 ** i:
#                 if j + count < len(code):
#                     a[j + count] = 1
#                     count += 1
#                 else:
#                     break
#         table.append(a)
#
#     # подставлем биты четности
#
#     for i in range(0, r):
#         res = -1
#         a = []
#         b = 0
#         for j in range(len(code)):
#             a.append(code[j] * table[i][j])
#         for c in a:
#             b += c
#         if b % 2 == 0:
#             res = 0
#         else:
#             res = 1
#         code[2 ** i - 1] = res
#     print(code)
#     return code
#
#
# def encode_hamming(data):
#     prepared_data = prepare_data(data)
#     encoded_data = calculate_parity_bits(prepared_data)
#     return ''.join(encoded_data)
#
#
# def hamming_encode(message):
#     # Calculate the number of parity bits needed
#     parity_bits = 0
#     while 2 ** parity_bits < len(message) + parity_bits + 1:
#         parity_bits += 1
#
#     # Initialize the encoded message
#     encoded_message = [0] * (len(message) + parity_bits)
#
#     # Fill in the message bits
#     j = 0
#     for i in range(len(encoded_message)):
#         if i + 1 not in [2 ** k for k in range(parity_bits)]:  # Skip the positions of parity bits
#             encoded_message[i] = int(message[j])
#             j += 1
#
#     # Fill in the parity bits
#     for i in range(parity_bits):
#         parity_index = 2 ** i - 1
#         parity = 0
#         for j in range(parity_index, len(encoded_message), 2 * (i + 1)):
#             for k in range(i + 1):
#                 if j + k < len(encoded_message):
#                     parity ^= encoded_message[j + k]
#         encoded_message[parity_index] = parity
#
#     return encoded_message
#
#
# def hamming_decode(encoded_message):
#     parity_bits = 0
#     while 2 ** parity_bits < len(encoded_message) + parity_bits + 1:
#         parity_bits += 1
#
#     syndrome = hamming_syndrome(encoded_message)
#     print(f"{syndrome=}")
#     if syndrome != 0:
#         encoded_message[syndrome - 1] ^= 1
#
#     print("Исправленное закодированное сообщение:", encoded_message)
#     original_message = [encoded_message[i] for i in range(len(encoded_message)) if
#                         i + 1 not in [2 ** k for k in range(parity_bits)]]
#     return original_message
#
#
# def print_data(data, n):
#     for i in range(n):
#         print(data[i:i + n])
#
#
# def print_flattened_data(data):
#     size = int(len(data) ** 0.5)
#     if size * size != len(data):
#         size += 1
#
#     grid = [['0'] * size for _ in range(size)]
#     for i in range(len(data)):
#         row = i // size
#         col = i % size
#         grid[row][col] = data[i]
#
#     # Print the grid
#     for row in grid:
#         print(*row)
#
#
def hamming_encode(bits):
    """
    Encode a list of bits using Hamming code.

    Args:
        bits (list): The list of bits to encode.

    Returns:
        list: The encoded bits.

    """
    # Calculate number of parity bits required
    m = len(bits)
    r = 0
    while (1 << r) < m + r + 1:
        r += 1

    encoded_bits = [0] * (m + r)
    iter_bits = iter(bits)
    for i in range(m + r):
        if i & (i + 1) != 0:
            encoded_bits[i] = next(iter_bits)

    encoded_bits.insert(0, 0)
    bin_code = hamming_syndrome(encoded_bits)
    for i in range(r):
        pos = 2 ** i
        if bin_code & pos:
            encoded_bits[pos] = 1

    encoded_bits[0] = sum(encoded_bits[1:]) % 2

    return encoded_bits


def hamming_syndrome(bits):
    return reduce(
        operator.xor,
        [i for i, v in enumerate(bits) if v], 0
    )


def decode(received_data):
    bin_code = hamming_syndrome(received_data)
    if bin_code != 0:
        received_data[bin_code] ^= 1

    original_data = [received_data[i] for i in range(len(received_data)) if i & (i - 1) != 0]
    return original_data


def p(data):
    return ''.join(map(str, data))
