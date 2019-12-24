array = [5,0,4,3,0,2,1]
zeros = []

count = 0
while count < len(array):
    print(f'count is {count} \n \t array is {array}')

    if array[count] == 0:
        array.pop(count)
        zeros.append(0)

    count += 1