def sort(alist):
    inversions = 0
    if len(alist) > 1:
        mid = len(alist) // 2
        left_list = alist[:mid]
        right_list = alist[mid:]

        inversions = sort(left_list)
        inversions += sort(right_list)

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
                inversions += len(left_list) - index_left
            position += 1

        while index_left < len(left_list):
            alist[position] = left_list[index_left]
            position += 1
            index_left += 1

        while index_right < len(right_list):
            alist[position] = right_list[index_right]
            position += 1
            index_right += 1
        return inversions
    return 0


inputFile = open("input.txt", "r")
length = int(inputFile.readline()) - 1
alist = [int(x) for x in inputFile.readline().split()]
inputFile.close()
outputFile = open("output.txt", "w")
res = sort(alist)
outputFile.write(str(res))
