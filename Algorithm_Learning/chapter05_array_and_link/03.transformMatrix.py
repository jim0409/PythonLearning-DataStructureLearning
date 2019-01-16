arrA = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
N = 4
# claim a 4*4 matrix
arrB = [[None] * N for row in range(N)]


print('the origin matrix value :')
for i in range(4):
  for j in range(4):
     print('%d'%arrA[i][j], end='\t')
  print()

# do translation
for i in range(4):
  for j in range(4):
    arrB[i][j] = arrA[j][i]

print('the translation value :')
for i in range(4):
  for j in range(4):
    print('%d'%arrB[i][j], end='\t')
  print()
