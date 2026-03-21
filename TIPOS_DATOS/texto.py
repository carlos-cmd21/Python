print("Hola 'Mundo'")
ingles = "i'm Carlos"

multiples = '''Hola
Mundo
desde las
comillas
triples'''

print(ingles)
print(multiples )

palabra = "murcielago"
print(len(palabra))
texto = "Esto es un curso de fundamentos de Python "
estaincluida="Python" in texto
noestaincluida= "Javascript" not in texto   
print(estaincluida)
print(noestaincluida)
mayuscula = texto.upper()
minuscula = texto.lower()
print(mayuscula)
print(minuscula)
espacios ="         esto es un texto          "
sinEspacios=espacios.strip()
print(sinEspacios)

#ind     0123456789
texto = "Este es un texto"
#slicing
print(texto[:2])
print(texto[7:])
print(texto[5:-2])

curso = "Este curso es de javascript"
print(curso.replace("javascript","python"))
textodividido = texto.split(" ")
print(textodividido)

#Normalizacion 
texto2="Este texto tiene MAYUSCULAS y minusculas"
print("mayusculas".lower() in texto2.lower())