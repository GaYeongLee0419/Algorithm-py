n = int(input())

array = []
for i in range(n):
    array.append(input())

array = list(set(array))

array.sort()

print(array)
for i in range(len(array)):
    print(array[i])