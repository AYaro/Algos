inputFile = open("input.txt", "r")
length = int(inputFile.readline())
a = [int(x) for x in inputFile.readline().split()]
inputFile.close()
outputFile = open("output.txt", "w")

outputFile.write('1' + ' ')
for index in range(1, length):

     currentValue = a[index]
     position = index

     while position > 0 and a[position-1] > currentValue:
         a[position] = a[position-1]
         position = position-1

     outputFile.write(str(position+1)+' ')
     a[position] = currentValue

outputFile.write('\n')
for element in a: outputFile.write(str(element)+' ')

