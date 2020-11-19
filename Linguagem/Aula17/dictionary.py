"""
mineiro = {
    "Uai":"Tudo",
    "So":"Qualquer pessoa"
}
print(mineiro["Uai"])
mineiro["Paia"] = "Coisa sem sentido"
print(mineiro)
print("Tamanho do dictionary: " + str(len(mineiro)))
print(mineiro.get("So"))
for d in mineiro:
    print(d)

for k,v in mineiro.items():
    print(k + " é igual a: " + v)
"""
"""
linguas = {
    "mineiro" :{
        "Uai":"Tudo",
        "So":"Qualquer pessoa"
    },

    "paulista" :{ 
        "N sei":"Não conheço nenhum paulista",
        "Tudo":"Gay ou não"
    }
}

print(linguas["paulista"])
print(linguas["paulista"]["Tudo"])
"""
mineiro ={
        "Uai":"Tudo",
        "So":"Qualquer pessoa"
    }

paulista = { 
        "N sei":"Não conheço nenhum paulista",
        "Tudo":"Gay ou não"
    }

linguas ={
    "M":mineiro,
    "P":paulista
}
print(linguas)
print(linguas["M"])