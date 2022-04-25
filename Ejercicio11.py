"""
Entradas
temperatra en grdos fahrenheit--> float-->t
Salidas
deporte a prcticar segun la temperatura-->str(cadena)-->d
"""
#Entradas
t=float(input("Digite temperatura: "))
#caja negra
d=""
if(t>85 and t<=120):
    d="Natación"
elif(t>70 and t<=85):
    d="Tenis"
elif(t>32 and t<=70):
    d="Golf"
elif(t>10 and t<=32):
    d="Esquí"
elif(t>=0 and t<=10):
    d="Marcha"
else:
    d="La temperatura no pertenece a ningun deporte"
#salidas
print(f"El deporte a practicar según su temperatura es:{d}")
