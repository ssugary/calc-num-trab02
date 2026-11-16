import numpy as np
import matplotlib.pyplot as plt
from metodos import interpolacao_sistema_linear
from funcoes import f_25

def plotar_25():
    x_real = np.linspace(0, 4, 200)
    y_real = [f_25(x) for x in x_real]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_real, y_real, label="Função Original (25)", color='black', linewidth=2)
    
    graus = [4, 10, 15]
    cores = ['blue', 'orange', 'red']
    
    for n, cor in zip(graus, cores):
        x_pontos = np.linspace(0, 4, n+1)
        y_pontos = [f_25(xi) for xi in x_pontos]
        
        y_interp = [interpolacao_sistema_linear(x_pontos, y_pontos, xi) for xi in x_real]
        
        plt.plot(x_real, y_interp, label=f"Polinômio Grau {n}", color=cor, linestyle='--')
        plt.scatter(x_pontos, y_pontos, color=cor)
        
    plt.title("Interpolação da Função de 25")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.ylim(-1, 2) 
    plt.show()
