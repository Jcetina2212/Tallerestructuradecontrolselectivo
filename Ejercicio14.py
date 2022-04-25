"""
Entradas
Lectura anterior-->int-->l
Lectura actual-->int-->l_a
caja negra
Lectura resultante-->int-->l_r
Salidas
Total a pagar-->float-->t
"""
#entradas
l=int(input("Digite la lectura anterior:"))
l_a=int(input("Digite la lectura actual:"))
#caja negra
l_r=l-l_a
t=""
if(l_r>=0 and l_r<=100):
    t=l_r*4600
elif(l_r>100 and l_r<=300):
    t=l_r*80000
elif(l_r>300 and l_r<=500):
    t=l_r*100000
else:
    t=l_r*120000
#salidas
print(f"El valor a pagar es de {t} COP")