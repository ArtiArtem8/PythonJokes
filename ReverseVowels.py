def reverseVowels(s: str):
    vowels = set("aeuioAEUIO")
    i, j = 0, len(s) - 1
    string = list(s)
    while True:
        while string[i] not in vowels and i < j:
            i += 1
        while string[j] not in vowels and j > i:
            j -= 1

        if i == j or i > j:
            break

        string[i], string[j] = string[j], string[i]
        i += 1
        j -= 1
    return ''.join(string)


def reverseVowels2(s: str):
    vowels = set("aeuioAEUIO")
    s = list(s)
    vow = list()
    for i in range(len(s)):
        if s[i] in vowels:
            vow.append(s[i])
            s[i] = 1
    for i in range(len(s)):
        if s[i] == 1:
            s[i] = vow.pop()
    return ''.join(s)


print(reverseVowels2("ddareoi"))
