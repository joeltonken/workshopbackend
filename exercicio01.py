# faça uma funçao que retorne o maior de dois numeros (5,6 ou 2,1 ou 7,7)

def maior(num1, num2) -> int:
  maxnum = num1
  if num1 > maxnum:
     maxnum = num1
      
  if num2 > maxnum:
    maxnum = num2
    
    return maxnum

def menor(num1, num2) -> int:
    minum = num1
    if num1 < minum:
      minum = num1

    if num2 < minum:
      minum = num2
                
    return minum

num1 = int(input('Informe o valor do primeiro número: '))
num2 = int(input('Informe o valor do segundo número: '))

print("O maior número é:", maior(num1, num2))
print("O menor número é:", menor(num1, num2))