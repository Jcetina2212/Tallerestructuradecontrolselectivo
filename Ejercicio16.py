"""
Entradas
A-->int-->a
B-->int-->b
C-->int-->c
caja negra
discriminante-->int-->d
"""
import math
#entradas
a=int(input("A:"))
b=int(input("B"))
c=int(input("C"))
#caja negra
d=(b**2)-(4*a*c)
if(d>0):
    x1=((-b+math.sqrt(b**2-(4*a*c)))/(2*a))
    x2=((-b-math.sqrt(b**2-(4*a*c)))/(2*a))
elif(d==0):
    x1=(-b)/(2*a)
    x2=(-b)/(2*a)
elif(math.sqrt(b**2-(4*a*c)<0)):
     x1="No tiene solución en los reales"
     x2="No tiene solucion en los reales"
else:
    x1="No tiene solución en los reales"
    x2="No tiene solucion en los reales"
print(f"x1:{x1}")
print(f"x2:{x2}")
