#exer1:
for num in range(0,16,3):
    print(f"{num}")

#exer2:
for num in range(1,101):
    print(f"{num}")
num = 0
while num != 100:
    for num in range(1,101):
        print(f"{num}")

#exer3:
fim = False
while fim != True:
    for num in range(10,-1, -1):
        print(f"{num}")
        if num == 0:
            print("FIM!!")
            fim = True

#exer4:
num = 0
for num in range(0,101000, 1000):
    print(f"{num}")

#exer5:
soma = 0
num = 0
for number in range(1,11):
    print(f"digite um numero({number}):")
    num = int(input())  
    soma += num 
print(f"{soma}")

#exer6:
soma = 0
num = 0
for number in range(1,11):
    print(f"digite um numero({number}):")
    num = float(input())  
    soma += num 
media = (soma/10)
print(f"Média = {media}")

#exer7:
soma = 0
num = 0
for number in range(1,11):
    print(f"digite um numero({number}):")
    num = float(input())  
    if num > 0:
        soma += num 
media = (soma/10)
print(f"Média = {media}")

#exer8:
maior = menor = qnt = 0
for num in range(1,11):
    print("Digite um numero:")
    num = int(input())
    qnt +=1
    if qnt == 1:
        maior = menor = num
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
print(f"O menor num é:{menor} e o maior é: {maior}")

#exer9:
num = int(input("digite um numero,será impresso os X numeros impares:"))
for num in range(1, num*2 , 2):
    print(f"{num}")

#exer10:
soma = 0
for num in range(1,51): 
    soma += num 
print(f"{soma}")

#exer11:
num = int(input('digite um numero:'))
for n in range(0,num+1):
    print(f"{n}")

#exer12:
num = int(input('digite um numero:'))
for n in range(num, -1 , -1):
    print(f"{n}")

#exer13:
num = int(input('digite um numero:'))
if num%2 == 0:
    for n in range(0,num+1, 2):
        print(f"{n}")

#exer14:
num = int(input('digite um numero:'))
if num%2 == 0:
    for n in range(num, -1, -2):
        print(f"{n}")

#exer15:
num = int(input('digite um numero:'))
if num%2 != 0:
    for n in range(1, num+1, 2):
        print(f"{n}")

#exer16:
num = int(input('digite um numero:'))
if num%2 != 0 and num > 0:
    for n in range(num, 0, -2):
        print(f"{n}")

#exer17:
soma = 0
num = int(input('digite um numero:'))
if num > 0:
    for n in range(1, num+1):
        soma += n
print(f"Resultado da soma = {soma}")

#exer18:
qnt = int(input('digite a quantidade de vezes que sera digitado os numeros:'))
lido = maior = 0

for n in range(qnt):
    num = int(input('digite o numero:'))
    if num > maior:
        maior = num
        lido += 1
    elif num == maior:
        lido +=1
print(f"O maior numero foi o {maior}, e o maior n° foi lido {lido-1} vezes.")

#exer19:
print(f"digite um numero:")
num = int(input())
num_str = str(num)
if num > 100 and num < 999:
    print(f"1° algarismo: {num_str[0]}")
    print(f"2° algarismo: {num_str[1]}")
    print(f"3° algarismo: {num_str[2]}")

#exer20:
quantidade_de_numeros = int(input("digite a quantidade de numeros a serem lidos:"))
dados_lidos = 0
numeros_pares = 0
for i in range(quantidade_de_numeros):
    num = int(input('digite um numero:'))
    dados_lidos += 1
    if num%2 == 0:
        numeros_pares += 1
        print(f"O num {num} é par!")
    else:
        print(f"O num {num} é impar!")
print(f"A quantidade de dados lidos foi: {dados_lidos}")
print(f"A quantidade de numeros pares foi: {numeros_pares}")


