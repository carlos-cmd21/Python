i=1

while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1

i=0
while i <= 10:
    if i == 5:
        break
    i += 2
    print(i)

#esto es un bucle infinito
'''
i=0
while i <= 10:
    if i == 5:
        continue
    i += 1
    print(i)
'''
i=0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)
else:
    print("i dejo de ser menor a 10")