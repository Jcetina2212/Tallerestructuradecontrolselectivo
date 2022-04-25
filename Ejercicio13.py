"""
Entradas
Dia de nacimiento-->int-->d
Mes de nacimiento-->int-->m
Año de nacimiento-->int-->f
año actual-->int-->Añ_a
mes actual-->int-->M_a
dia actual-->int-->D_a
Salidas
signo-->str-->signo
Edad-->int-->e
"""
from datetime import datetime
#sacamos le fecha actual del sistema
Ah = datetime.now()
Añ_a = Ah.year
M_a = Ah.month
D_a = Ah.day
#entradas (formato dia/mes /año)
d=int(input("Digite el dia de nacimiento:"))
m=int(input("Digite el mes de nacimiento:"))
f=int(input("Digite el año de naciemiento:"))
#caja negra
#edad
e=""
if(M_a>=m):
    e=Añ_a-f
else:
    e=(Añ_a-f)-1
#signo
signo=""
if(m==1):
    if(d>=21 and d<=30):
        signo="Acuario"
    else:
        signo="Capricornio"
elif(m==2):
        if(d>=19 and d<=30):
            signo="Piscis"
        else:
            signo="Acuario"
elif(m==3):
    if(d>=21 and d<=30):
        signo="Aries"
    else:
        signo="Piscis"
elif(m==4):
    if(d>=21 and d<=30):
        signo="Tauro"
    else:
        signo="Aries"
elif(m==5):
    if(d>=22 and d<=30):
        signo="Géminis"
    else:
        signo="Tauro"
elif(m==6):
    if(d>=22 and d<=30):
        signo="Cáncer"
    else:
        signo="Géminis"
elif(m==7):
    if(d>=23 and d<=30):
        signo="Leo"
    else:
        signo="Cáncer"
elif(m==8):
    if(d>=24 and d<=30):
        signo="Virgo"
    else:
        signo="Leo"
elif(m==9):
    if(d>=23 and d<=30):
        signo="Libra"
    else:
        signo="Virgo"
elif(m==10):
    if(d>=23 and d<=30):
        signo="Escorpíon"
    else:
        signo="Libra"
elif(m==11):
    if(d>=22 and d<=30):
        signo="Sagitario"
    else:
        signo="Escorpíon"
elif(m==12):
    if(d>=12 and d<=30):
        signo="Capricornio"
    else:
        signo="Sagitario"
#salidas
print(f"{e} Años")
print(signo)

