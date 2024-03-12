import itertools
from functools import reduce


def encode(data):
    p1 = data[0] ^ data[1] ^ data[3]
    p2 = data[0] ^ data[2] ^ data[3]
    p3 = data[1] ^ data[2] ^ data[3]
    encoded_data = [p1, p2, data[0], p3, data[1], data[2], data[3]]
    return encoded_data


def decode(received_data):
    s1 = received_data[0] ^ received_data[2] ^ received_data[4] ^ received_data[6]
    s2 = received_data[1] ^ received_data[2] ^ received_data[5] ^ received_data[6]
    s3 = received_data[3] ^ received_data[4] ^ received_data[5] ^ received_data[6]
    error_position = s1 + 2 * s2 + 4 * s3
    if error_position > 0:
        corrected_bit = received_data[error_position - 1]
        received_data[error_position - 1] = 1 - corrected_bit
    original_data = [received_data[2], received_data[4], received_data[5], received_data[6]]
    return original_data


def hamming_syndrome(bits):
    return reduce(
        lambda x, y: x ^ y,
        [i for (i, v) in enumerate(bits) if v]
    )


def prepare_data(data):
    n = len(data)
    i = 0
    j = 0
    k = 0
    while i + j < n + k:
        if j == (2 ** i - 1):
            i += 1
        else:
            k += 1
        j += 1
    return [0 if i == (2 ** j - 1) else data[-k] for i in range(n + j)]


def calculate_parity_bits(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == 0:
            parity_pos = 2 ** i
            xored = 0
            for j in range(1, n + 1):
                if j & parity_pos and j != parity_pos:
                    xored ^= int(arr[-j])
            arr[-parity_pos] = str(xored)
    return arr


def encode_hamming(data):
    prepared_data = prepare_data(data)
    encoded_data = calculate_parity_bits(prepared_data)
    return ''.join(encoded_data)


def hamming_encode(message):
    # Calculate the number of parity bits needed
    parity_bits = 0
    while 2 ** parity_bits < len(message) + parity_bits + 1:
        parity_bits += 1

    # Initialize the encoded message
    encoded_message = [0] * (len(message) + parity_bits)

    # Fill in the message bits
    j = 0
    for i in range(1, len(encoded_message) + 1):
        if i & (i - 1) != 0:  # Skip the positions of parity bits
            encoded_message[i - 1] = int(message[j])
            j += 1

    # Fill in the parity bits
    for i in range(parity_bits):
        parity_index = 2 ** i - 1
        parity = 0
        for j in range(parity_index, len(encoded_message), 2 * (i + 1)):
            for k in range(i + 1):
                if j + k < len(encoded_message):
                    parity ^= encoded_message[j + k]
        encoded_message[parity_index] = parity

    return encoded_message


def hamming_decode(encoded_message):
    parity_bits = 0
    while 2 ** parity_bits < len(encoded_message):
        parity_bits += 1

    syndrome = hamming_syndrome(encoded_message)
    print(syndrome)
    if syndrome != 0:
        encoded_message[syndrome - 1] ^= 1

    original_message = [encoded_message[i] for i in range(len(encoded_message)) if
                        i + 1 not in [2 ** k for k in range(parity_bits)]]
    return original_message


def print_data(data, n):
    for i in range(n):
        print(data[i:i + n])


def print_flattened_data(data):
    size = int(len(data) ** 0.5)
    if size * size != len(data):
        size += 1

    grid = [['0'] * size for _ in range(size)]
    for i in range(len(data)):
        row = i // size
        col = i % size
        grid[row][col] = data[i]

    # Print the grid
    for row in grid:
        print(*row)
