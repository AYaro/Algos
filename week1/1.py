inputFile = open("input.txt", "r")
a,b = [int(x) for x in inputFile.readline().split()]
inputFile.close()
outputFile = open("output.txt", "w")
outputFile.write(str(a+b))
outputFile.close()
