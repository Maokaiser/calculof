print("ingrese las masas de 2 planetas y la distancia entre ellos")
m1=float(input("primera masa: "))
m2=float(input("segunda masa: "))
r=float(input("Distancia entre ellos: "))
f = float

def fuerza(m1,m2,r):
    
    f= (6.67*m1*m2)/(r*r)

    print("la fuerza entre ambos planetes es de ", f )

fuerza(m1,m2,r)


