tp = (10,20,30)
try:
    tp[1] = 10
except NameError:
    print("Tuplas não podem ser modificadas")
else:
    print("Tudo certo")