def difference_detect(list):
    for element in list[1:]:
        if element != list[0]:
            return True
    return False

def divide_and_count(list):
    left_list = list[0:len(list)//2]
    right_list = list[len(list)//2:len(list)]
    if not difference_detect(list):
        return 0
    if len(list) == 2:
        return 1
    left_count = divide_and_count(left_list)
    right_count = divide_and_count(right_list)
    if left_count >0 and right_count >0:
        return left_count + right_count
    else:
        return 1

A = int(input())
B = int(input())
print(A+B)

data = []
for i in range(2):
    row = list(input().split())
    data.append(row)
data[0][0] = int(data[0][0])
N = data[0][0]
S = [char for char in data[1][0]]
print(S)
    
print(divide_and_count(S))

