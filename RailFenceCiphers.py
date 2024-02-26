# Original: https://www.codewars.com/kata/58c5577d61aefcf3ff000081/train/python

def encode_rail_fence_cipher(string, n):
    rails = [""] * n
    n -= 1
    for i, s in enumerate(string):
        rails[abs((i - n) % (n * 2) - n)] += s
    print(rails)
    return ''.join(rails)


print(encode_rail_fence_cipher("HelloWorld!", 5))
"""
H       l
 e     r  d
  l   o    !
   l W
    o
Hlerdlo!lwo
H       l
 e     r d
  l   o   !
   l w     
    o
"""


def decode_rail_fence_cipher(string, n):
    print(len(string))
    from math import ceil
    msg = (' ' * ((n - 1) * 2 - 1)).join(list(string[:ceil(len(string) / ((n - 1) * 2))]))
    msg = msg.ljust(len(string), ' ')
    msg = [i if i != ' ' else '' for i in msg]
    if (len(string)) % ((n - 1) * 2) > n or (len(string)) % ((n - 1) * 2) == 0:
        msg.extend('' for _ in range((((n - 1) * 2) * ceil(len(string) / ((n - 1) * 2))+1) - len(string)))
        msg[-1] = 1
    print(msg)
    ex = (((n - 1) * 2) * ceil(len(string) / ((n - 1) * 2))+1) - len(string) - 1
    ch = ceil(len(string) / ((n - 1) * 2))
    while "" in msg:
        old_msg = msg[:]
        for i in range(len(msg)):
            if ex > 0 and old_msg[i] == 1:
                if msg[i - 1] == '' and ex > 0:
                    msg[i - 1] = 1
                    ex -= 1
            elif old_msg[i] != '':
                if i != 0 and msg[i - 1] == '':
                    msg[i - 1] = string[ch]
                    ch += 1
                if i != len(msg) - 1 and msg[i + 1] == '':
                    msg[i + 1] = string[ch]
                    ch += 1
            if ch == len(string):
                break

    return ''.join(filter(lambda x: x != 1, msg))


print(decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3))
print("WEAREDISCOVEREDFLEEATONCE")
print(decode_rail_fence_cipher("Hlerdlo!lwo", 5))
print("HelloWorld!")
print(decode_rail_fence_cipher("pdxveizhjcmbmj", 5))
print("pxijmczvdehmjb")
print(decode_rail_fence_cipher("acagdcmjkwdp", 3))
print("agwdccdmajpk")
'''a   c   a   '
    g d c m j k
     w   d   p
'''
'ag dcc maj  '
"""
       p       d       '
        x     v e     '
         i   z   h   '
          j c     m b
           m       j
"""
"pxijmczvdehmjb"
'p       d     ;;'
'pxij czvdehm  '
'p       d     '
# decode_rail_fence_cipher("H !e,Wdloollr", 4)
# print("Hello, World!")
'H           !'
"Hello, World!"

'WECRLTEERDSOEEFEAOCAIVDEN'
'WEAREDISCOVEREDFLEEATONCE'
'WEIREDDSCONERE FLE ATO CE'
'WE RED SCO ERE FLE ATO CE'
'W   E   C   R   L   T   E'
'ghgptuegysnriukmqq'
'ghtmyuegnqkriupqsg'
