a = 5
b = 6

# a, b = b, a

a = a ^ b           # xor
b = a ^ b
a = a ^ b

print(a)
print(b)
