import numpy as np
from metodos import interpolacao_diferencas_divididas, interpolacao_lagrange

def analisar_co2():
    print("\nConcentração de CO2:")
    anos = np.array([1960, 1970, 1980, 1990, 2000, 2010, 2020])
    co2 = np.array([315, 327, 337, 335, 370, 388, 411])

    idx_a = [3, 4, 5, 6] 
    anos_a = anos[idx_a]
    co2_a = co2[idx_a]

    idx_b2 = [4, 5, 6] 
    co2_grau2 = interpolacao_diferencas_divididas(anos[idx_b2], co2[idx_b2], 2008)
    co2_grau3 = interpolacao_diferencas_divididas(anos_a, co2_a, 2008)

    print(f"Estimativa 2008 com n = 2: {co2_grau2:.2f} ppm")
    print(f"Estimativa 2008 com n = 3: {co2_grau3:.2f} ppm")
    print(f"Valor Observado: 381.00 ppm")

    idx_c = [2, 3, 4]
    co2_inverso = co2[idx_c]
    anos_inverso = anos[idx_c]

    ano_350 = interpolacao_lagrange(co2_inverso, anos_inverso, 350)
    print(f"(c) Ano em que o CO2 atingiu 350 ppm (Grau 2 Inverso): {ano_350:.0f}")
