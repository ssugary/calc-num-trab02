import numpy as np
from metodos import interpolacao_sistema_linear, interpolacao_lagrange, interpolacao_diferencas_divididas
from funcoes import f_exp, f_25
from co2 import analisar_co2
from graficos import plotar_25

def main():
    print("Interpolação da Função f(x) = e^x")
    graus = [3, 4, 5, 10]
    for n in graus:
        x_pontos = np.linspace(1, 3, n+1)
        y_pontos = [f_exp(xi) for xi in x_pontos]
        x_teste = 2.5
        y_real = f_exp(x_teste)
        
        y_aprox_lag = interpolacao_lagrange(x_pontos, y_pontos, x_teste)
        y_aprox_sis = interpolacao_sistema_linear(x_pontos, y_pontos, x_teste)
        y_aprox_dd  = interpolacao_diferencas_divididas(x_pontos, y_pontos, x_teste)
        
        print(f"\nGrau {n} (onde o Valor reeal em x={x_teste} é {y_real:.6f}):")
        print(f" Sist. Linear : Aprox = {y_aprox_sis:.6f} | Erro = {abs(y_real-y_aprox_sis):.2e}")
        print(f" Lagrange     : Aprox = {y_aprox_lag:.6f} | Erro = {abs(y_real-y_aprox_lag):.2e}")
        print(f" Dif. Divid.  : Aprox = {y_aprox_dd:.6f} | Erro = {abs(y_real-y_aprox_dd):.2e}")

    print("\nFunção f(x) = 1/(1+25x²)")
    graus_25 = [4, 10, 15]
    for n in graus_25:
        x_pontos = np.linspace(0, 4, n+1)
        y_pontos = [f_25(xi) for xi in x_pontos]
        x_teste = 1.5
        y_real = f_25(x_teste)
        y_aprox = interpolacao_sistema_linear(x_pontos, y_pontos, x_teste)
        print(f"Grau {n}: Valor real em x={x_teste} é {y_real:.6f} | Aprox = {y_aprox:.6f} | Erro = {abs(y_real-y_aprox):.2e}")

    analisar_co2()
    
if __name__ == "__main__":
    main()