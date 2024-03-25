# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome = input('Qual seu nome ?')

# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias = input('Quantos dias você estuda por semana ?')

# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
total_horas = input('Qual a quantidade de horas que você estuda por dia ?')

# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
curso = input('Qual o curso que você está estudando no momento ?')

# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
total_horas = int(total_horas)
total_dias = int(total_dias)

print(f'Olá {nome}! Você costuma estudar {total_horas} horas por dia a cada {total_dias} dias na semana. Isso significa que você em média estuda {total_dias * total_horas} horas por semana com o curso de {curso}.')

