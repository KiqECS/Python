import re

texto = "Lorem ipsum mi phasellus dictumst egestas nunc primis auctor est, ac vivamus sagittis tincidunt velit vivamus iaculis nam at ac, integer enim habitant urna conubia auctor risus inceptos. ut porta lobortis gravida porta aliquam primis pharetra, egestas malesuada ornare blandit curabitur erat nullam integer, libero eget viverra ornare phasellus bibendum. "

count_l = re.findall("l",texto)
print(count_l)

qtd="Quantidade de Ls no texto: {}"

print(qtd.format(len(count_l)))

count = 0
for t in count_l:
    print(t)
    count+=1
    print("\'", count , "\'")