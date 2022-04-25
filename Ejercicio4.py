"""
Entradas
precio-->float-->p
caja negra
cantida que asume la empresa-->float-->e
cantidad que asume el banco-->float-->b
credito al fabricante-->float-->c
cantidad de intereses-->float-->i
total a invertir-->float-->t_d
"""
p=float(input("Ingrese el monto total de la compra: "))
#Caja negra
e=""
b=""
c=""
i=""
t_d=""
if(p>=5000000):
    e=p*0.55
    b=p*0.30
    c=p*0.15
    i=c*0.20
    t_d=c+i
else:
    e=p*0.70
    b=0
    c=p*0.30
    i=c*0.20
    t_d=c+i
#salidas
print(f"la cantidad a invertir de los fondos de la empresa es de: {e} COP ")
print(f"La cantidad de dinero que dejara el fabricante a credito es de: {c} COP")
print(f"El total de dinero que se devolvera al fabricante sera de: {t_d} COP")
if(b!=0):
    print(f"El dinero que prestara el banco sera de: {b} COP")

