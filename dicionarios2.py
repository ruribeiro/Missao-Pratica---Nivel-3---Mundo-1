# dicionário inicial
meu_dicionario = {1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}}

# novos elementos update
meu_dicionario.update({2: {'nome': 'João', 'idade': 30, 'nacionalidade': 'brasileira'},
                       3: {'nome': 'Ana', 'idade': 25, 'nacionalidade': 'portuguesa'}})

print( meu_dicionario)

# cópia do dicionario
copia_dicionario = meu_dicionario.copy()

# Removendo um elemento usando pop
elemento_removido = meu_dicionario.pop(1)
print(elemento_removido)
print(meu_dicionario)

# Removendo o último elemento usando popitem
ultimo_elemento = meu_dicionario.popitem()
print(ultimo_elemento)
print(meu_dicionario)

# Limpando os dicionários
meu_dicionario.clear()
copia_dicionario.clear()

# Criando um novo dicionário usando fromkeys
chaves = ['a', 'b', 'c']
valor_padrao = 'valor padrão'
novo_dicionario = dict.fromkeys(chaves, valor_padrao)

# Imprimindo o novo dicionário
print(novo_dicionario)

# Imprimindo chaves, valores e itens
print("Chaves:", novo_dicionario.keys())
print("Valores:", novo_dicionario.values())
print("Itens:", novo_dicionario.items())