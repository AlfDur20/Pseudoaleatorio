import pandas as pd

class alg_congruencial:
    def __init__(self):
        pass

    def MCM(self,a, m, X_0, num):
        listan = []
        listaXn=[]
        lista_aXn = []
        lista_aXn_modm = []

        Xn = X_0

        for n in range(num + 1):
            aXn = a * Xn
            aXn_modm = aXn % m
            listan.append(n)
            listaXn.append(Xn)
            lista_aXn.append(aXn)
            lista_aXn_modm.append(aXn_modm)
            Xn = aXn_modm

        tabla = pd.DataFrame({
            "n": listan,
            "X(n)": listaXn,
            "a*X(n)": lista_aXn,
            "[a*X(n)] mod m": lista_aXn_modm
        })

        print(tabla.to_string(index=False))

