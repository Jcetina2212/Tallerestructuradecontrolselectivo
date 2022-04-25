"""
entradas
A-->int-->a
B-->int-->b
C-->int-->c
D-->int-->d
salida
Numero entero redondeado al mas cercano-->int-->N_f
"""
#entradas
a=int(input(""))
b=int(input(""))
c=int(input(""))
d=int(input(""))
#caja negra 
a_1=""
b_1=""
c_1=""
d_1=""
if(b>=5 and b<9):
    a_1=a
    b_1=b+1
    c_1=0
    d_1=0
elif(b>=5 and b>=9):
    a_1=a+1
    b_1=0
    c_1=0
    d_1=0
else:
    a_1=a
    b_1=b
    c_1=0
    d_1=0
a_1=str(a_1)
b_1=str(b_1)
c_1=str(c_1)
d_1=str(d_1)
N_f=a_1+b_1+c_1+d_1
#salidas
print(N_f)

