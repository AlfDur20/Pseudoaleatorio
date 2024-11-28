# main.py
from PseudoaleatorioCongruencial import alg_congruencial
from PseudoaleatorioNoCongruencial import alg_no_congruencial

# Uso de la clase No_congruencial
print("No congruencial: ")
no_congruencial = alg_no_congruencial()
numero_inicial = 151
numero_inicial2 = 155
no_congruencial.MPM(numero_inicial, numero_inicial2)

# Uso de la clase Congruencial
print("Congruencial: ")
congruencial = alg_congruencial()
a = 5
m = 32
X_0 = 5
num = 10
congruencial.MCM(a, m, X_0, num)
