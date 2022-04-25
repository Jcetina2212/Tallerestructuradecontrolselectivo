"""
Entradas
dinero-->float-->d
"""
#Entradas
d=float(input("Ingrese la cantidad de dinero en COP: "))
#caja negra
monedas_1=d
billetes_100=(monedas_1-monedas_1%100000)//100000
monedas_1=monedas_1%100000
billetes_50=(monedas_1-monedas_1%50000)//50000
monedas_1=monedas_1%50000
billetes_20=(monedas_1-monedas_1%20000)//20000
monedas_1=monedas_1%20000
billetes_10=(monedas_1-monedas_1%10000)//10000
monedas_1=monedas_1%10000
billetes_5=(monedas_1-monedas_1%5000)//5000
monedas_1=monedas_1%5000
billetes_2=(monedas_1-monedas_1%2000)//2000
monedas_1=monedas_1%2000
billetes_1=(monedas_1-monedas_1%1000)//1000
monedas_1=monedas_1%1000
monedas_500=(monedas_1-monedas_1%500)//500
monedas_1=monedas_1%500
monedas_200=(monedas_1-monedas_1%200)//200
monedas_1=monedas_1%200
monedas_100=(monedas_1-monedas_1%100)//100
monedas_1=monedas_1%100
monedas_500=(monedas_1-monedas_1%500)//500
monedas_1=monedas_1%500
monedas_200=(monedas_1-monedas_1%200)//200
monedas_1=monedas_1%200
monedas_100=(monedas_1-monedas_1%100)//100
monedas_1=monedas_1%100
monedas_50=(monedas_1-monedas_1%50)//50
monedas_1=monedas_1%50
if(billetes_100>=1):
    print ('Valor de billetes de 100000: ' + repr (billetes_100))
if(billetes_50>=1):
    print ('Valor de billetes de 50000: ' + repr (billetes_50))
if(billetes_20>=1):
    print ('Valor de billetes de 20000: ' + repr (billetes_20))
if(billetes_10>=1):
    print ('Valor de billetes de 10000: ' + repr (billetes_10))
if(billetes_5>=1):
    print ('Valor de billetes de 5000: ' + repr (billetes_5))
if(billetes_2>=1):
    print ('Valor de billetes de 2000: ' + repr (billetes_2))
if(billetes_1>=1):
    print ('Valor de billetes de 1000: ' + repr (billetes_1))
if(monedas_500>=1):
    print ('Valor de monedas de 500: ' + repr (monedas_500))
if(monedas_200>=1):
    print ('Valor de monedas de 200: ' + repr (monedas_200))
if(monedas_100>=1):
    print ('Valor de monedas de 100: ' + repr (monedas_100))
if(monedas_50>=1):
    print ('Valor de monedas de 50: ' + repr (monedas_50))
