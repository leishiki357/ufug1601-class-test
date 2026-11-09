import sys
lines = sys.stdin.readlines()
A = lines[0].strip()
B = lines[1].strip()
SEPARATOR = lines[2].strip()
print(A, B)
print(A, B + A + SEPARATOR + B)
print(A + B)