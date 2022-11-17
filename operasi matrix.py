mat1 = [[6, 0, 4],
        [2, 7, 3],
        [1, 6, 2]]

mat2 = [[2, 6, 5],
        [3, 2, 4],
        [7, 1, 3]]
result = []
for i in range(len(mat1)):
    row = []
    for j in range(len(mat1[i])):
        row.append(mat1[i][j]+mat2[i][j])
    result.append(row)

print("the result of adding 2 matrices:")
for row in result:
    print(row)
print("="*10)

result = []
for i in range(len(mat1)):
    row = []
    for k in range(len(mat2[0])):
        val = 0
        for j in range(len(mat1[i])):
            val+=mat1[i][j]*mat2[j][k]
        row.append(val)
    result.append(row)

print("the result of multiplying 2 matrices:")
for row in result:
    print(row)
