l_comidas = ["Batata","Laranja","Hamburguer"] #List
t_comidas = ("Batata","Laranja","Hamburguer") #Tuple

#l_comidas[1] = "Macarrão" Can be modified
#t_comidas[1] = "Macarrão" Can't be modified

# A tuple can be modified with a litlle trick

l_comidas = list(t_comidas)
l_comidas[1] = "Macarrão"
t_comidas = tuple(l_comidas)

for c in t_comidas:
    print(c)
    print(type(t_comidas))

