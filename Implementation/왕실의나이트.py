input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0]) - int(ord('a'))) + 1 #a=1로 생각

# 이동 가능한 모든 가짓 수
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)] 

result = 0
for step in steps :
    next_row = row + step[1]
    next_column = column + step[0]

    if next_row >= 1 and next_column >= 1 and next_row <= 8 and next_column <= 8:
        result += 1

print(result)
