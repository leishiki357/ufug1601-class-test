import sys
data = []
for line in sys.stdin:
    numbers = line.split()
    data.append(numbers)

A = [int(x) for x in data[0]]
B = [int(x) for x in data[1]]

A.reverse()
B.reverse()
D = B[:]

D[0]+=1

n = A[len(A)-1]
m = B[len(B)-1]
c = []
for power in range(n+m+1):
    counter = 0
    for i in range(n+1):
        for j in range(m+1):
            if i + j == power:
                term = A[i] * D[j]
                counter += term
    c.append(counter)

c.reverse()
C = [int(x) for x in c]
print(*C)