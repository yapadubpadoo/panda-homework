width_and_height = 7
center = 4

for rows_index in range(1, width_and_height + 1):
    line = ''
    spaces_left_count = abs(center - rows_index)
    spaces_right_count = abs(center - rows_index)
    asterisk_count = width_and_height - (spaces_left_count + spaces_right_count)
    for i in range(0, spaces_left_count):
        line = line + ' '
    for i in range(0, asterisk_count):
        line = line + '*'
    for i in range(0, spaces_right_count):
        line = line + ' '
    print(line)
