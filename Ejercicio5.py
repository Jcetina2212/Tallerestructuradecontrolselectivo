"""
Entradas
ventas del departamento1-->float-->v_1
ventas del departamento2-->float-->v_2
ventas del departamento3-->float-->v_3
salario gloabal-->float-->s
caja negra
total ventas-->float-->t
porcentaje del veneficio-->float-->p
Salidas
cantidad a resivir de cada empleado de los 3 departamentos-->float-->c_1,c_2,c_3
"""
#entradas
from ctypes import c_int32


v_1=float(input("ventas del departamento 1:"))
v_2=float(input("ventas del departamento 2:"))
v_3=float(input("ventas del departamento 3:"))
s=float(input("salario de todos los empleados:"))
#caja negra
t=v_1+v_2+v_3
p=0.33*t
c_1=""
c_2=""
c_3=""
if(v_1>p):
    c_1=(0.20*s)+s
else:
    c_1=(f"{s} No aplica insentivo")
if(v_2>p):
    c_2=(0.20*s)+s
else:
    c_2=(f"{s} No aplica insentivo")
if(v_3>p):
    c_3=(0.20*s)+s
else:
    c_3=(f"{s} No aplica insentivo")
#salidas
print(f"El salrio para los empleados del departamento 1 es:{c_1}")
print(f"El salrio para los empleados del departamento 2 es:{c_2}")
print(f"El salrio para los empleados del departamento 3 es:{c_3}")

