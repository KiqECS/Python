nomes_sobrenomes = [["Geraldo", "Viana"],
                    ["Neuza", "Helena"],
                    ["Nickolas","Gomes"]
                   ]
nomes_idades = [["Nickolas", 6], ["Kaique", 17]]

print(nomes_sobrenomes[0][0])

nomes_sobrenomes.append(["Kaique","Gomes"])
for n,s in nomes_sobrenomes:
    print(n + " " + s)

for n,i in nomes_idades:
    print(n + " " + str(i))
