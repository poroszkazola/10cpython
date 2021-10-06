'''
#import math
#a=math.pi
# kerekítés
print(round(6.1432,3))
print(round(6.1432,2))
#hatványozás
print(pow(2,8)) #pow(alap,kitevő)
#abs aboszolut ertek

#print(abs(-12))
#print(min(1,2,3,5,6,7,8,9,))
#print(max(1,2,3,4,5,6,7,8,9))
#print(a)

from math import *
b=pi
print(b)
#négyzetgyök vonás -sqrt

print(sqrt(4))
#felfelé kerekítés ceil
print(ceil(4.12))
print(floor(5.99))

from math import*
'''
from math import *

#1.feladat négyzet kerülete területe 

a= float(input("Addjameg az  első számot:"))
kerület = 4*a
terület = a*2
print(kerület)
print(terület)





#2.feladat téglalap kerülete területe 
a = float(input("Addjameg az a oldalt:"))
b = float(input("Addjameg az b oldalt:"))
terület = 2*a+2*b
kerület =  a*b
print(terület)
print(kerület)


#3.feladat kör  kerülete(2rPI) területe r2 PI

r= float(input("Addjameg az r oldalt:"))

kerülete = 2*r*pi
területe = r*2*pi
print(kerülete)
print(területe)





#4.feladat kocka  térfogata V = a3 felszíne A= 6*a2

a = float(input("Addja meg az a oldalt :"))
V = a**3
A = 6*a**2
print(V)
print(A)




#5.feladat  pitagorasz
# c négyzetgyök a**2 + b**2

a = float(input("Addja meg a számot:"))
b = float(input("Addja meg a b számot:"))
negyzetgyok = a**2+b**2
negyzetgyok1 = sqrt(negyzetgyok)
print(negyzetgyok1)