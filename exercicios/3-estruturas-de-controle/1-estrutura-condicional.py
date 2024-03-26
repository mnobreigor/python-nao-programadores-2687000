# Declare 4 variáveis do tipo numérica

a = 2
b = 7
c = 15
d = 20

# Crie uma estrutura condicional para comparar dois números

if(a > d):

# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor

  print(f'A condição foi cumprida, pois {a} é maior que {d}.')

# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor

else:
  print(f'A condição não é verdadeira, pois {d} é maior que {a}.')

# Insira outras condições na estrutura condicional usando o elif
if(b == c):
  print(f'Exato ! {b} e {c} são iguais !')
elif(d > c):
  print(f'Muito bem ! {d} é maior que {c}.')
else:
  print(f'Nenhuma das afirmações são verdadeiras.')

# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
if(a == c) and (b > d):
  print(f'Exato ! {a} e {c} são iguais e {b} é maior que {d}')
else:
  print('A condição é falsa !')

# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"

if(c > b):
  print(f'Exato ! De fato {c} é maior que {b}.')
if(d > a):
  print(f'Exato ! De fato {d} é maior que {a}.')