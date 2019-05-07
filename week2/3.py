inputFile = open("input.txt", "r")
length = int(inputFile.readline())
alist = [0]*length
for i in range(length):
    alist[i] = i + 1
    if i > 1:
        alist[i], alist[i//2] = alist[i//2], alist[i]

outputFile = open("output.txt", "w")
outputFile.write(' '.join(map(str, alist)))

