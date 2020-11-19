import re

texto = "Lorem ipsum mi phasellus dictumst egestas nunc primis auctor est, ac vivamus sagittis tincidunt velit vivamus iaculis nam at ac, integer enim habitant urna conubia auctor risus inceptos. ut porta lobortis gravida porta aliquam primis pharetra, egestas malesuada ornare blandit curabitur erat nullam integer, libero eget viverra ornare phasellus bibendum. "

chan = re.sub("\s","   .",texto)
chan = re.sub("a","y",texto)
print(chan)