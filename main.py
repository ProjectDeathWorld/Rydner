# This is triangle
n = 3
for i in range(1, n + 1):
    print('*' * i)
print("\n")

# This is reverse triangle
n = 3
for i in range(n, 0, -1):
    print('*' * i)
print("\n")

# This is diamond
n = 3
for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))

