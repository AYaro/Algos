inputFile = open("input.txt", "r")
n, k = [int(x) for x in inputFile.readline().split()]
lst = [int(x) for x in inputFile.readline().split()]


arrays = []
for i in range(k):
    temporary_array = []
    for j in range(i, n, k):
        temporary_array.append(lst[j])
    temporary_array.sort()
    arrays.append(temporary_array)
result = "YES"

for i in range(1, n):
    if arrays[i % k][i // k] < arrays[(i - 1) % k][(i - 1) // k]:
        result = "NO"
        break


file = open("output.txt", "w")
file.write(result)
