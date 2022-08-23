import numpy as np
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[12,2,1]])
print("Матрица A =")
print(A)
print("Определитель матрицы A =", np.linalg.det(A))
print("Ранг матрицы А = ", np.linalg.matrix_rank(A,0.0001))

C = np.concatenate((A,B.T), axis=1)
print("Расширенная матрица C = ")
print(C)
print("Ранг матрицы C = ", np.linalg.matrix_rank(C,0.0001))
print("Изменим вектор правой части B так, чтобы система стала совместной")
B1 = np.array([[12,15,18]])
C1 = np.concatenate((A,B1.T), axis=1)
print("Ранг расширенной матрицы C1 = ", np.linalg.matrix_rank(C1,0.0001))


print("Решение системы A*X = B1 :")
result = np.linalg.solve(A,np.array([12,15,18]))
print(result)