# need to append .txt file columns to matrix
# need to iterate each cell on left hand side list, where it is multiplied by amount of times exact int is repeated on right handside column



matrix = []
with open('/Users/dans/Documents/Code/AOC/Day_1/D1.txt', 'r') as file:
    for line in file:
        row = list(map(int, line.split()))
        matrix.append(row)

columns = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
