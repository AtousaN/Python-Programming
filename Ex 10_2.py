import numpy as np
import matplotlib.pyplot as plt
vec1 = np.array([-1., 4., -9.])
mat1 = np.array([[1., 3., 5.], [7., -9., 2.], [4., 6., 8.]])
vec2 = (np.pi/4) * vec1
vec2 = np.cos(vec2)
print(vec2)
vec3 = vec1 + 2 * vec2
print(vec3)
vec4 = mat1 * vec3
print('mat1 = ' , mat1)
print('transpose' , np.transpose(mat1) )
print('determinant' , np.linalg.det(mat1) )
print('trace' , np.sum(np.diag(mat1)) )
minimum = np.min(mat1)
print(np.where(mat1 == minimum))
print('minimum =' , minimum)
A = np.array([[17, 24, 1, 8, 15],
              [23, 5, 7, 14, 16],
              [4, 6, 13, 20, 22],
              [10, 12, 19, 21, 3],
              [11, 18, 25, 2, 9]])
row = np.sum(A,axis=-1)
column = np.sum(A,axis=-2)
diag = np.sum(np.diag(A))
flip = np.fliplr(A)
diagflip = np.sum(np.diag(flip))
if np.min(np.sum(A,axis=1)) == np.max(np.sum(A,axis=1)) == np.min(np.sum(A,axis=0)) == np.max(np.sum(A,axis=0)) == np.sum(A.diagonal()) == np.sum(np.diag(flip)) :
    print('A is a magic matrix')
else :
    print('A is not a magic matrix')
M = np.random.rand(10, 10)

MUL = M[ :5 , :5 ]
MUR = M[ :5 , 5: ]
MLL = M[ 5: , :5 ]
MLR = M[ 5: , 5: ]


