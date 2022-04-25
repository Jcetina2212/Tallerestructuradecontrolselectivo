"""
Entradas
edad del paciente-->int-->e
hemoglobina en la muestr-->float-->h
genero-->str-->g
caja negra
resultado del analisis-->str-->r
"""
#entradas
from turtle import position


e=int(input("Digite la edad del paciente:"))
h=float(input("Digite la hemoglobina que marco el analisis:"))
g=str(input("Ingrese el genero del paciente"))
#caja negra
r=""
if(e>=0 and e<=1):
    if(h>=13 and h<=26):
        r="Negativo"
    else:
        r="Positivo"
elif(e>1 and e<=6):
    if(h>=10 and h<=18):
        r="Negativo"
    else:
        r="Positivo"
elif(e>6 and e<=12):
    if(h<=11 and h<=15):
        r="Negativo"
    else:
        r="Positivo"
elif(e>1 and e<=5):
    if(h<=11.5 and h<=15):
        r="Negativo"
    else:
        r="Positivo"
elif(e>5 and e<=10):
    if(h<=12.6 and h<=15.5):
        r="Negativo"
    else:
        r:"position"
elif(e>10 and e<=15):
    if(h<=13 and h<=15.5):
        r="Negativo"
    else:
        r="positivo"
elif(e>10 and e<=15):
    if(h<=13 and h<=15.5):
        r="Negativo"
    else:
        r="Positivo"
elif(e>15):
    if(g=="hombre" or "Hombre"):
        if(h<=14 and h<=18):
            r="Negativo"
        else:
            r="Positivo"
    else:
        if(h<=12 and h<=16):
            r="Negativo"
        else:
            r="Positivo"
#salidas
print(r)