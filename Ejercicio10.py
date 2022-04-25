"""
Entradas
categoria-->int-->c
sueldo bruto-->float-->s
salidas
categoria del trabajador-->int
nuevo sueldo bruto-->float-->n
"""
#entradas
c=int(input("Digite la categoria:"))
s=float(input("Digite el sueldo bruto:"))
#caja negra
n=""
if(c==1):
    if(s==5000000.0 and s>4300000.0):
        n=(0.1*s)+s
    else:
        n=(f"{s} Aumento no encontrado dentro de los rangos estipulados")
elif(c==2):
    if(s<=4300000.0 and s>3600000.0):
        n=(0.15*s)+s
    else:
        n=(f"{s} Aumento no encontrado dentro de los rangos estipulados")
elif(c==3):
    if(s<=3600000.0 and s>2000000.0):
        n=(0.2*s)+s
elif(c==4):
    if(s>=2000000.0 and s>900000.0):
        n=(0.4*s)+s
    else:
        n=(f"{s} Aumento no encontrado dentro de los rangos estipulados")    
elif(c==5):
    if(s==900000.0):
        n=(0.6*s)+s
    else:
        n=(f"{s} Aumento no encontrado dentro de los rangos estipulados")
#salidas
print(f"El nuevo salario es: {n} COP")
