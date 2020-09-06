comida = ["Arroz","Feijão","Batata"]

it_Comida = iter(comida)

while it_Comida:
    try:
        print(next(it_Comida))
    except StopIteration:
        print("Fim da lista")
        break