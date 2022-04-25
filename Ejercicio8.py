"""
entradas
P-->int-->p
Q-->int-->q
caja negra
expresión-->int-->e
salidas
satisface o no satisface la expresión-->int-->s
"""
#entradas
p=int(input("Digite P:"))
q=int(input("Digite Q:"))
#caja negra
e=(p**3)+(q**4)-(2*(p**2))
s=""
if(e>680):
  s=(f"{p} y {q} satisfacen la expresion")
else:
  s=(f"{p} y {q} no satisfacen la expresion")
  #salidas
print(s)