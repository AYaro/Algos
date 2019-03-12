class A(object):
    def __init__(self, value, key):
        self.value = value
        self.key = key


inputFile = open("input.txt", "r")
length = int(inputFile.readline())
a = []
for i, val in enumerate(inputFile.readline().split()):
    element = A(float(val), i)
    a.append(element)
inputFile.close()
outputFile = open("output.txt", "w")

for i in range(length - 1, 0, -1):
        for j in range(i):
            if a[j].value > a[j+1].value:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp

outputFile.write(str(a[0].key + 1) + ' ' + str(a[(length-1)//2].key + 1) + ' ' + str(a[length-1].key + 1))
