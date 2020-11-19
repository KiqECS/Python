compras=["Arroz", "Feijão", "Batata"]
compras.append("Refigerante") #Add itens
compras.remove("Arroz")
"""
compras.clear() # Delete all list
compras2=list(compras) # Copy list to another list
"""
del compras[0] # Remove by indice 
tbcompras=["Chips", "Doces","Cerveja"]
importantes=compras + tbcompras

importantes.append("Café")
#importantes.pop() #Remove the last one  

print("Número de objetos " + str(len(importantes)))
print(importantes)