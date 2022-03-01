input_string = 'dddfffhjkkkkkdddddiii4445555'

count = 1

rle = ''

for i in range(1, len(input_string)):
    if input_string[i] == input_string[i - 1]:
        count += 1
    else:
        rle += str(count) + ':' + input_string[i - 1] + '-'
        count = 1

rle += str(count) + ':' + input_string[i]

print(rle)
