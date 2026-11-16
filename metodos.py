import numpy as np

def interpolacao_sistema_linear(x, y, x_alvo):
    n = len(x)
    A = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            A[i][j] = x[i]**j
    
    coef = np.linalg.solve(A, y) # Se quiser, podemos substituir isso por algum método de resolução de sistemas lineares que implementamos
    y_alvo = sum(coef[i] * (x_alvo**i) for i in range(n))
    
    return y_alvo

def interpolacao_lagrange(x, y, x_alvo):
    n = len(x)
    y_alvo = 0
    
    for i in range(n):
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x_alvo - x[j]) / (x[i] - x[j])
    
        y_alvo += y[i] * L_i
    
    return y_alvo

def interpolacao_diferencas_divididas(x, y, x_alvo):
    n = len(x)
    dd = np.zeros((n, n))
    dd[:, 0] = y
        
    for j in range(1, n):
        for i in range(n - j):
            dd[i][j] = (dd[i+1][j-1] - dd[i][j-1]) / (x[i+j] - x[i])

    y_alvo = dd[0][0]
    x_term = 1
    
    for i in range(1, n):
        x_term *= (x_alvo - x[i-1])
        y_alvo += dd[0][i] * x_term
    
    return y_alvo
