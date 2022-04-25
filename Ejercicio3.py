"""
entradas
A-->int-->a
B-->int-->b
C-->int-->c
D-->int-->d
salidas
f-->expresión final 
"""
#entradas
a=int(input(""))
b=int(input(""))
c=int(input(""))
d=int(input(""))
#caja negra
f=""
if(d==0):
  f=(a+c)**2
elif(d>0):
  f=((a-b)**3)/d
else:
  f="expresión invalida"
#salidas
print(f)