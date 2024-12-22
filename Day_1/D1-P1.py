#figure out how to import txt file 
#list lefthand side #'s in matrix
#list righthand side #'s in order in matrix
#sort in order lefthand side #'s and righthand side #'s
#subtract lefthand side cell and righthand side cell and store in new matrix (value must be abs)
#sum of cells in new matrix

# Open the file and read line by line
matrix = []
with open('/Users/dans/Documents/Code/AOC/Day_1/D1.txt', 'r') as file:
    for line in file:
        row = list(map(int, line.split()))
        matrix.append(row)

columns = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
columnsSorted = [sorted(col) for col in columns]
matrixSorted = [[columnsSorted[j][i] for j in range(len(columnsSorted))] for i in range(len(matrix))]

col1 = [row[0] for row in matrixSorted]
col2 = [row[1] for row in matrixSorted]

distance = [abs(a - b) for a, b in zip(col1, col2)]
distMatrix = [[diff] for diff in distance]

totalDist = sum(diff[0] for diff in distMatrix)

print(totalDist)
