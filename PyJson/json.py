import json
dict_foods = {"arroz":"faz bem","refigerante":"faz mal"}

dict_foods_json = json.dumps(dict_foods)

print(dict_foods_json)