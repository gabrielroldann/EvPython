# Exercício 072 - Tuplas (Curso Em Vídeo)

# Enunciado:
# - Crie um programa que tenha uma tupla totalmente preechida com uma contagem por extenso, de zero até vinte.
# - Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

# Resolução:

contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
            'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um número entre 0 e 20 para ver sua escrita por extenso: '))
    if 0 <= num <= 20:
        break
    print('Número não está entre 0 e 20. ', end='')
print(f'Extenso: {contagem[num]}')


# -----------------------------------------------------------------------------------------------------------------#
# Exercício 073 - Tuplas (Curso Em Vídeo)

# Enunciado:
# - Crie uma tupla com os 20 primeiros times colocados do Brasileirão*, na ordem de colocação. Depois mostre:
# - A) Apenas os 5 primeiros colocados.
# - B) Os últimos 4 colocados.
# - C) Uma lista com os times em ordem alfabética.
# - D) Em que posição está o time do Ceará SC.
# - *Usado a lista do Brasileirão de 2022.

# Resolução:

times = ('Palmeiras', 'Fluminense', 'Flamengo', 'Corinthians', 'Internacional', 'Athletico-PR', 'Atlético-MG',
         'Santos','América-MG', 'Bragantino', 'Goiás', 'São Paulo', 'Fortaleza', 'Botafogo', 'Ceará SC', 'Cuiabá',
         'Avaí', 'Coritiba', 'Atlético-GO', 'Juventude')

# Maneira 01 (Simples)

print('='*25)
print('Tabelas de Colocações')
print('='*25)
print('')
print('5 Primeiros Colocados:')
print(f'1º - {times[0]}', f'\n2º - {times[1]}', f'\n3º - {times[2]}', f'\n4º - {times[3]}', f'\n5º - {times[4]}')
print('-'*25)
print('4 Últimos Colocados:')
print(f'17º - {times[16]}', f'\n18º - {times[17]}', f'\n19º - {times[18]}', f'\n20º - {times[19]}')
print('-'*25)
print('Times em ordem alfabética:')
print(sorted(times))
print('-'*25)
print('Posição do Ceará SC: ')
print('O Ceará SC está na 15º posição.')

# Maneira 02 (Estrutura de Repetição)

print('='*25)
print('Tabelas de Colocações')
print('='*25)
print('')
print('5 Primeiros Colocados:')
for pos, c in enumerate(times[0:5]):
    print(f'{pos+1}º - {c}')
print('-'*25)
print('4 Últimos Colocados: ')
for pos, c in enumerate(times[16:]):
    print(f'{pos+1}º - {c}')
print('-'*25)
print('Times em ordem alfabética: ')
print(sorted(times))
print('-'*25)
print('Posição do time Ceara SC:')
print(f'O {times[14]} está na 15º posição.')
#                      - ou -
print(f'O Ceará SC está na {times.index("Ceará SC")+1}º posição.')
#                      - ou -
print(f'O {times[14]} está na {times.index("Ceará SC")+1}º posição.')


# -----------------------------------------------------------------------------------------------------------------#
# Exercício 074 - Tuplas (Curso Em Vídeo)

# Enunciado:
# - Crie um programa que vai gerar cinco número aleatórios e colocar em uma tupla.
# - Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

# Resolução:

from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Números sorteados: {n}')
print(f'Maior número sorteado: {max(n)}')
print(f'Menor número sorteado: {min(n)}')


# -----------------------------------------------------------------------------------------------------------------#
# Exercício 075 - Tuplas (Curso Em Vídeo)

# Enunciado:
# - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# - A) Quantas vezes aparece o valor 9.
# - B) Em que posição foi digitado o primeiro valor 3.
# - C) Quais foram os números pares.

# Resolução:

nums = (int(input('Digite o primeiro valor: ')), int(input('Digite o segundo valor: ')),
        int(input('Digite o terceiro valor: ')), int(input('Digite o quarto valor: ')))

print(f'O número 9 aparece {nums.count(9)} vezes.')
if 3 in nums:
    print(f'O número 3 foi digitado na(s) posição(ões) {nums.index(3)+1}')
else:
    print('O valor 3 não foi digitado.')
print('Números pares: ', end='')
for n in nums:
    if n % 2 == 0:
        print(n, end=' ')

# -----------------------------------------------------------------------------------------------------------------#
# Exercício 076 - Tuplas (Curso Em Vídeo)

# Enunciado:
# - Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência.
# - No final, mostre uma listagem de preços, organizados os dados em forma tabular.

# Resolução:

comp = ('Gabinete', 250, 'Fans', 130, 'Placa Mãe', 670, 'Placa de Vídeo', 4700, 'Memórias RAM', 350, 'Fonte', 600,
        'Processador', 9800)

# Maneira 01

print('-'*50)
print('Lista de produtos e preços para montagem do PC Gamer')
print('-'*50)
print(f'{comp[0]} R$ {comp[1]}')
print(f'{comp[2]} R$ {comp[3]}')
print(f'{comp[4]} R$ {comp[5]}')
print(f'{comp[6]} R$ {comp[7]}')
print(f'{comp[8]} R$ {comp[9]}')
print(f'{comp[10]} R$ {comp[11]}')
print(f'{comp[12]} R$ {comp[13]}')

#  Maneira 02

print('='*41)
print(f'{"LISTA DE PREÇOS":^41}')
print('-'*41)
for item in range(0, len(comp)):
   if item % 2 == 0:
        print(f'{comp[item]:.<30}', end='')
   else:
        print(f'R${comp[item]:>8.2f}')
print('='*41)


# -----------------------------------------------------------------------------------------------------------------#
# Exercício 077 - Tuplas (Curso Em Vídeo)

# Enunciado:
# - Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# - Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.

# Resolução:

palavras = ('Bilas', 'Lulu', 'David', 'Vitinho')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra.upper(), end=' ')
