
def soma(num1,num2):
    result = num1 + num2
    print(result)

soma(5,2)

def soma_plus(*num):
    result_plus = 0
    for n in num:
        result_plus += n
            
    print("Soma total: " + str(result_plus))

soma_plus(5,8,7,6,1,3,8,30000)