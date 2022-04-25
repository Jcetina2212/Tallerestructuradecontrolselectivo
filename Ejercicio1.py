"""
Entradas
Dinero en el banco-->float-->d
Interes del banco-->float-->i
Salidas
Intereses generados-->float-->ig
Total dinero-->float-->t
Desicioó-->str-->de
"""
d=float(input("Digite la cantidad invertida en el banco:"))
i=float(input("Interes que maneja el banco:"))
#caja negra
i_1=i/100
ig=i_1*d
t=ig+d
de=""
if(ig>=100000):
    de="Es conveniente invertir"
else:
    de="No se recomienda invertir"
#salidas
print(f"Interes generado:{ig}")
print(de)
print(f"Total de dinero:{t}")
