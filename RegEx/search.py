import re

texto = "Lorem ipsum mi phasellus dictumst egestas nunc primis auctor est, ac vivamus sagittis tincidunt velit vivamus iaculis nam at ac, integer enim habitant urna conubia auctor risus inceptos. ut porta lobortis gravida porta aliquam primis pharetra, egestas malesuada ornare blandit curabitur erat nullam integer, libero eget viverra ornare phasellus bibendum. "

p = input("Frase que deseja buscar: ")

buscar = re.search(p,texto)
b_s = buscar.start()
b_e = buscar.end()
tam = b_e - b_s
tam_text = "Inicia em {}, finaliza em {} e o tamanho da palavra é {}"
print(tam_text.format(b_s,b_e,tam))