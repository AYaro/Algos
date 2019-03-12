class A(object):
    def __init__(self, value, key):
        self.value = value
        self.key = key


inputFile = open("input.txt", "r")
length = int(inputFile.readline())
a = [int(x) for x in inputFile.readline().split()]
inputFile.close()
outputFile = open("output.txt", "w")
if length != 1:
    for i in range(0, length-1):
        minValue = a[i]
        minIndex = i
        for j in range (i+1, length):
            if a[j] < minValue:
                minValue = a[j]
                minIndex = j
        temp = a[minIndex]
        a[minIndex] = a[i]
        a[i] = temp
        if minIndex != i:
            outputFile.write('Swap elements at indices ' + str(i+1) + ' and ' + str(minIndex+1) + '.\n')

outputFile.write("No more swaps needed.\n")
for element in a: outputFile.write(str(element)+' ')
