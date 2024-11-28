
import pandas as pd

class alg_no_congruencial:
    def __init__(self):
        pass

    def MPM(self,numero_inicial, numero_inicial2):
        listan=[]
        listaRn=[]
        listaRn1=[]
        listaRn2=[]
        listaMRn2=[]
        listaV1 = []
        listaV2 = []
        
        n=0
        while True:
            listan.append(n)
            n+=1
            listaRn.append(numero_inicial)
            listaRn1.append(numero_inicial2)
            nuevo_numero = numero_inicial * numero_inicial2
            listaRn2.append(nuevo_numero)
            nuevo_numero = str(nuevo_numero)
            nuevo_numero = nuevo_numero[1:-1]
            if not nuevo_numero: 
                nuevo_numero ='0' 
            listaMRn2.append(nuevo_numero)
            if len(nuevo_numero) > 0:
                if nuevo_numero[0] == '0':
                    nuevo_numero = nuevo_numero[1:]
            if len(nuevo_numero) >= 1 :
                valor1 = nuevo_numero[0:3]
                listaV1.append(valor1)
            else:
                valor1 = 0
                listaV1.append(valor1)
            if len(nuevo_numero) >= 4:
                valor2 = nuevo_numero[-3:]
                listaV2.append(valor2)
            else:
                valor2 = 0
                listaV2.append(valor2)
            numero_inicial = numero_inicial2
            numero_inicial2 = int(valor1)
            if numero_inicial == 0:
                break
        
        
        tabla = pd.DataFrame({
            "n": listan,
            "R(n)": listaRn,
            "R(n+1)": listaRn1,
            "R(n)^2": listaRn2,
            "M.R(n)^2": listaMRn2,
            "Valor 1":listaV1,
            "Valor 2": listaV2
        })

        print(tabla.to_string(index=False))



