import random
numi=1
numf=1.3
numc=1j

aleatorios=random.randrange(0,99)
variosaleatorios=[
    random.randrange(0,99),
    random.randrange(0,99),
    random.randrange(0,99),
    random.randrange(0,99),
    random.randrange(0,99)
]#Random List
comparador=numc

print("Valor: " + str(comparador) + " Tipo: " + str(type(comparador)))
print("Valor aleatorio: " + str(aleatorios))#Value between 0 .. 99

print("1° Valor aleatorio da lista: " + str(variosaleatorios[0]))
print("2° Valor aleatorio da lista: " + str(variosaleatorios[1]))
print("3° Valor aleatorio da lista: " + str(variosaleatorios[2]))
print("4° Valor aleatorio da lista: " + str(variosaleatorios[3]))
print("5° Valor aleatorio da lista: " + str(variosaleatorios[4]))