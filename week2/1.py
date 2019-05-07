def sort(alist, left, right):
    output_string = ''
    if len(alist) > 1:
        mid = len(alist) // 2
        left_list = alist[:mid]
        right_list = alist[mid:]

        output_string += str(sort(left_list, left, left + mid - 1))
        output_string += str(sort(right_list, left + mid, right))

        index_left = 0
        index_right = 0
        position = 0

        while index_left < len(left_list) and index_right < len(right_list):
            if left_list[index_left] <= right_list[index_right]:
                alist[position] = left_list[index_left]
                index_left += 1
            else:
                alist[position] = right_list[index_right]
                index_right += 1
            position += 1

        while index_left < len(left_list):
            alist[position] = left_list[index_left]
            position += 1
            index_left += 1

        while index_right < len(right_list):
            alist[position] = right_list[index_right]
            position += 1
            index_right += 1

        output_string += f"{left + 1} {right + 1} {alist[0]} {alist[-1]}\n"

    if output_string != '':
        return output_string
    else:
        return ''


inputFile = open("input.txt", "r")
length = int(inputFile.readline()) - 1
alist = [int(x) for x in inputFile.readline().split()]
inputFile.close()
outputFile = open("output.txt", "w")
res = sort(alist, 0, length)
outputFile.write(res)
outputFile.write(' '.join(map(str, alist)))
