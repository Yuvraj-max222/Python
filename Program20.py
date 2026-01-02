#Create a 2D matrix of 5 rows and 5 columns. Print the minimum and  maximum element of both primary and secondary diagonal.
matrix = []
for i in range(5):
    row = []
    for j in range(5):
        element = int(input(f"Enter the elemnent at position ({i+1}, {j+1}): "))
        row.append(element)
        matrix.append(row)
        primary_diagonal = []
        secondary_diagonal = []
        for i in range(5):
            primary_diagonal.append(matrix[i][i])
            secondary_diagonal.append(matrix[i][4-i])
            print("Primary Diagonal: ", primary_diagonal)
            print("Secondary Diagonal: ", secondary_diagonal)
            print("Minimum element in Primary Diagonal: ", min(primary_diagonal))
            print("Maximum element in Primary Diagonal: ", max(primary_diagonal))
            print("Minimum element in Secondary Diagonal: ", min(secondary_diagonal))
            print("Maximum element in Secondary Diagonal: ", max(secondary_diagonal))