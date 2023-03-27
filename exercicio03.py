# escreva uma funcao que receba o lado (l) de um quadrado e retorne sua area (a = lado²)

def areaquadrado(num1):
  return num1*num1

num1 = float(input("Informe o valor do lado do quadrado: "))
print(f'A área de um quadrado corresponde a {areaquadrado(num1):.2f}m²')