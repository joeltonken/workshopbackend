# escreva uma funcao que receba dois numeros e retorne true se o primeiro numero for multiplo do segundo

def multiplo(num1, num2) -> int:
  return num1 % num2 == 0

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))

print(f'{num2} é multiplo de {num1}:', multiplo(num2, num1))
