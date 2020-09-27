import json

list_comidas = ["Arroz","Feijão","Batata"]
list_comidas_json = json.dumps(list_comidas)
#Py list -> Json array/list

tuple_comidas = ("Arroz","Feijão","Batata")
tuple_comidas_json = json.dumps(tuple_comidas)
#Py tuple -> Json array/list

dict_comidas = {
    "arroz":"cereal",
    "batata":"legume"
}
dict_comidas_json = json.dumps(dict_comidas, indent=3,separators=(":"," é "))
#Py dict -> Json object

print(dict_comidas_json)