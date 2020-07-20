products=[]
def show_product():
    for p in products:
        print(p)
def add_product():
    new_product = input("Digite o nome do produto: ")
    products.append(new_product)
    print("Produto adicionado")

yorn_cproduct = input("Deseja adicionar algum produto a sua lista? [s/n]: ")
if yorn_cproduct == 's' or yorn_cproduct == "S":
    add_product()
    show_product()
    yorn_nproduct = input("Deseja adcionar um outro produto? [s/n]: ")
    while yorn_nproduct == 's' or yorn_nproduct == 'S':
        add_product()
        show_product()
        yorn_nproduct = input("Deseja adicionar um outro produto? [s/n]: ")
    print("Tudo bem!\nTchau!!") 
elif (yorn_cproduct == 'n' or yorn_cproduct == 'N'):
    print("Tudo bem!\nTchau!!")

