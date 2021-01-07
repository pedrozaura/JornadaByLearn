# Calculadora de media com duas notas. 

nome = input('Insira seu nome: ')

nota1 = float(input('sua primeira nota: '))
nota2 = float(input('sua segunda nota: '))

print('Olá ', nome, ' suas notas foram: ' )
print(nota1, ' e ', nota2)

soma = nota1 + nota2
media = soma / 2

print ('Sua media é: ', media)