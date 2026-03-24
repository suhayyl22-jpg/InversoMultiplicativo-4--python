import numpy as np

print("=== INVERSO MULTIPLICATIVO ===")

# 🔹 EJERCICIO 1: Método por fórmula (determinante)
A = np.array([[2, 1], [5, 3]])

print("\n=== EJERCICIO 1 (FÓRMULA / SISTEMA) ===")
print("Matriz A:\n", A)

a, b = A[0]
c, d = A[1]

print("\nPaso 1: Determinante")
det = a*d - b*c
print(f"det(A) = ({a}*{d}) - ({b}*{c}) = {det}")

print("\nPaso 2: Intercambiar diagonal y cambiar signos")
print(f"Matriz adjunta = [[{d}, {-b}], [{-c}, {a}]]")

print("\nPaso 3: Multiplicar por 1/det")
A_inv = (1/det) * np.array([[d, -b], [-c, a]])

print("\nResultado:")
print(A_inv)


# 🔹 EJERCICIO 2: Gauss-Jordan
B = np.array([[1, 2], [3, 4]])

print("\n=== EJERCICIO 2 (GAUSS-JORDAN) ===")
print("Matriz B:\n", B)

print("\nPaso 1: Matriz aumentada [B | I]")
I = np.eye(2)
aug = np.hstack((B, I))
print(aug)

print("\nPaso 2: Hacer 1 en la posición (1,1)")
print("Fila1 ya tiene 1")

print("\nPaso 3: Hacer 0 debajo")
f2 = aug[1] - 3*aug[0]
print("F2 = F2 - 3*F1")
print(f2)

print("\nPaso 4: Hacer 1 en segunda fila")
f2 = f2 / f2[1]
print("F2 = F2 / elemento pivote")
print(f2)

print("\nPaso 5: Hacer 0 arriba")
f1 = aug[0] - 2*f2
print("F1 = F1 - 2*F2")
print(f1)

print("\nResultado aproximado:")
print(np.linalg.inv(B))


# 🔹 EJERCICIO 3: Diagonalización
C = np.array([[4, 0], [0, 2]])

print("\n=== EJERCICIO 3 (DIAGONALIZACIÓN) ===")
print("Matriz C:\n", C)

print("\nPaso 1: Es diagonal → solo invertir elementos")
print("1/4 y 1/2")

C_inv = np.array([[1/4, 0], [0, 1/2]])

print("\nResultado:")
print(C_inv)


# 🔹 EJERCICIO 4: Por factores (determinante y adjunta)
D = np.array([[3, 1], [2, 2]])

print("\n=== EJERCICIO 4 (POR FACTORES) ===")
print("Matriz D:\n", D)

a, b = D[0]
c, d = D[1]

print("\nPaso 1: Determinante")
det = a*d - b*c
print(f"det(D) = ({a}*{d}) - ({b}*{c}) = {det}")

print("\nPaso 2: Matriz adjunta")
adj = np.array([[d, -b], [-c, a]])
print(adj)

print("\nPaso 3: Multiplicar por 1/det")
D_inv = (1/det) * adj

print("\nResultado:")
print(D_inv)
