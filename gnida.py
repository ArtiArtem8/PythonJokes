import os

total_sum = 0

def parse_and_merge(file_path):
    positions = {}

    # Read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Split the line into parts
            parts = line.split()
            if len(parts) < 6:
                continue  # skip malformed lines

            # Extract character and coordinates
            char = parts[0]
            x = int(parts[1])
            y = int(parts[2])
            width = int(parts[3])
            height = int(parts[4])
            zero = parts[5]

            # Create a key for the dictionary
            key = (x, y, width, height, zero)

            # Add the character to the corresponding position
            if key in positions:
                positions[key] += char
            else:
                positions[key] = char

    sum = 0
    # Print the merged characters in the original format
    for key, merged_chars in positions.items():
        x, y, width, height, zero = key
        sum += len(merged_chars)
        print(f"{merged_chars} {x} {y} {width} {height} {zero}")
    print(f"{sum=}")
    global total_sum
    total_sum += sum

# Call the function with the path to your file
print(os.listdir(r'C:\Users\a_shi\Downloads\Telegram Desktop\14\\'))
for i in os.listdir(r'C:\Users\a_shi\Downloads\Telegram Desktop\14\\')[:1]:
    if i.endswith(".box"):
        print(f'\n\n{i}\n')
        parse_and_merge(rf'C:\Users\a_shi\Downloads\Telegram Desktop\14\{i}')

print(total_sum)