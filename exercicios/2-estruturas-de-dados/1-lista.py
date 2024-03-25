# Crie uma lista apenas com elementos numéricos
lista_num = [1, 3, 5, 8, 10, 15.4]
print(lista_num)

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
list_all = [1, 2, 4, 5.4, 8.43, True, 'igor', [1, 2, 3, 4]]
print(list_all)

# Imprima na tela apenas os 5 primeiros elementos da lista
print(list_all[0:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
print(lista_num[0:-1:2])

# Remova da lista o último item
lista_num.pop()
print(lista_num)

# Insira na lista um novo item
lista_num.append(22)
print(lista_num)

# Remova da lista um item específico
list_all.remove('igor')
print(list_all)