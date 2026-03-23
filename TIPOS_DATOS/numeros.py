x=1
y=2.5
z=1j
print(type(x))
print(type(y))
print(type(z))

positivo =5
negativo=-5

imaginario = -5-1j

xf=float(x)
print(type(xf))
print(xf)
ye=int(y)
print(type(ye))
print(ye)

entero = 5
flotante =5.5
enterocomplejo = complex(entero)
flotantecomplejo = complex(flotante)
print(type(enterocomplejo))
print(type(flotantecomplejo))
print(enterocomplejo)   
print(flotantecomplejo)


import random as r

print(r.randrange(1,10)) #numero aleatorio entre 1 y 9

text = "+++-hello-++h+"
cleaned_text = text.strip("+h-")
print(cleaned_text)