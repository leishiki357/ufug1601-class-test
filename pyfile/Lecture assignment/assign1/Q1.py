n = int(input())
times=0
while n != 1:
    if n % 2 == 0:
        n //= 2
        times=times+1
    else:
        n=3*n+1
        times=times+1
print(times)

