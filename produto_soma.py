import random

a = int(input("digite o valor de A "))
b = int(input("digite o valor de B "))
c = int(input("digite o valor de C "))

b = b * (-1) #inversa do valor de B

print(f"\n{a}x² + {b}x + {c} = 0")

contador = 1

while contador <= 100:
    num1 = random.choice([0])
    num2 = random.choice([0])

    soma = num1 + num2
    mult = num1 * num2

    while soma != b and mult != c:

        # pelo menos faça do -20 a 20
        num1 = random.choice([-4,-3,-2,-1,0,1,2,3,4])
        num2 = random.choice([-4,-3,-2,-1,0,1,2,3,4])

        soma = num1 + num2
        mult = num1 * num2

    else:
        if soma == b and mult == c:
            print(f"{num1} + {num2} = {b}")
            print(f"{num1} x {num2} = {c}")
            print(f"{num1} e {num2} são as raoizesn\n")
            break
    
    contador += 1
    if contador == 100: 
        print("não foi possivel resolver\n")
        break
