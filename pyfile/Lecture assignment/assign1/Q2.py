n = int(input())
times=0
a = n//5
for i in range(1, a+1):
    b = (n-5*i)//2
    for j in range(1, b+1):
        c = n-5*i-2*j
        if c>=1:
            times+=1
        else:
            times+=0
print(times)
