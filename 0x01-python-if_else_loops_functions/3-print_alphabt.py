#!/usr/bin/python3
a = ord('a')
z = ord('z')
alpha = ''.join(chr(i) for i in range(a, z + 1)if chr(i) not in ('q', 'e'))
print(alpha)
