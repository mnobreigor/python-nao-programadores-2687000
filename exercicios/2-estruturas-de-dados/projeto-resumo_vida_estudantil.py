# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.

estudante = {}
estudante['nome'] = input('Qual seu nome ? ')
estudante['ano_linkedin'] = int(input('Em que ano você criou seu LinkedIn ? '))
estudante['ano_atual'] = int(input('Em que ano estamos atualmente ? '))

curso = input('Quais cursos você realizou no LinkedIn Learning ? (Separe-os por vírgula, por favor) ')
estudante['cursos'] = curso.split(', ')

total_anos = estudante['ano_atual'] - estudante['ano_linkedin']
total_cursos = len(estudante['cursos'])

print(f"Oi {estudante['nome']}, desde {estudante['ano_linkedin']} você conhece o LinkedIn. Nesses {total_anos} anos, você realizou um total de {total_cursos} cursos, sendo o primeiro curso o de {estudante['cursos'][0]} e o último curso de {estudante['cursos'][-1]}.")
