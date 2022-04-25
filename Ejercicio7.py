"""
entradas
Distancia recorrida-->float-->d
Salidas
Total a pagar-->float-->t
"""
#entradas
d=float(input("Digite la cantidad de kilimetros recorridos:"))
#caja negra
t=""
if(d<=300):
    t=50000
else:
    if(d<1000):
        t=70000+((d/300)*30000)
    else:
        t=150000+((d-1000)*9000)
#salidas
print(f"{t} COP")