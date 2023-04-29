aux = int(input('Digite um numero'))
i = 0
maior = aux
while i < 9:
    aux = int(input('Digite um numero: '))
    if(aux > maior):
        maior = aux
    i+=1
print(maior)