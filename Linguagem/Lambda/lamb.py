#Can be
soma = lambda a,b: a+b
print(soma(2,6))
# and
print((lambda a,b: a+b) (2,5))
############

print((lambda a,b,c,d,e: (a*b)/(c*d)-e ) (100,3000,444,800,960))