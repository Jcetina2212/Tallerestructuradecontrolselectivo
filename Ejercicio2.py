"""
entradas
sueldo de un trabajador-->float-->s
salidas 
sueldo tras el aumento dependiendo del sueldo-->float-->sf
"""
#entradas
s=float(input(""))
#caja negra
s1=0.15*s
s2=0.12*s
sf=""
if(s<900000):
  sf=s1+s
else:
  sf=s2+s
#salidas
print(sf)