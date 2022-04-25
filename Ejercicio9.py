"""
Entradas
Nombre del cliente-->str-->n
Monto de la compra-->float-->m_c
caja negra
descuento efectuado-->float-->d
Monto a pagar-->float-->m_p
"""
#entradas
n=str(input("Ingrese el nombre del cliente:"))
m_c=float(input("Digite el monto de la compra:"))
#caja negra
d=""
m_p=""
if(m_c<50000):
    d="No aplica descuento"
    m_p=m_c
elif(m_c>=50000 and m_c<100000):
    d="Descuento del 5 %"
    m_p=(0.5*m_c)-m_c
elif(m_c>=100000 and m_c<700000):
    d="Descuento del 11%"
    m_p=(0.11*m_c)-m_c
elif(m_c>=700000 and m_c<1500000):
    d="Descuento del 18%"
    m_p=(0.18*m_c)-m_c
elif(m_c>1500000):
    d="Descuento del 25%"
    m_p=(0.25*m_c)-m_c
#salidas
print(f"Usuario: {n}")
print(d)
print(f"El total a pagar es de: {m_p} COP")