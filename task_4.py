import numpy as np
import scipy.linalg as sc

A = np.array([[1,2,3],[2,16,21],[4,28,73]])
P, L, U = sc.lu(A)

print(P)
print(L)
print(U)

print(np.dot(P, A) - np.dot(L,U))

print("A = L*U")
print(np.dot(L,U))
print("Прилумаем вектор правых частей B и решим систему A*X = B:")
B = np.array([12,2,1])
print(B)
print("Решение системы:")
print(np.linalg.solve(A,B))