import json

dict_foods = {"arroz":"faz bem","refigerante":"faz mal"}

dict_foods_json = json.dumps(dict_foods)

print(type(dict_foods_json))

# Não sei como funciona o Json ainda, mas por algum motivo o type aparece str,
# bem em algum momento acho que vou descobrir
"""
dict_foods_json= '{"arroz":"faz bem","refrigerante":"faz mal"}'

dict_foods = json.loads(dict_foods_json)
print(type(dict_foods))
"""

#Descobri que não se pode colocar o nome do arquivo de Json pq da um erro com o import :'3