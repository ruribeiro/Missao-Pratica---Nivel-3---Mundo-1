# set inicial
set_inicial = {11, 12, 13, 14}

# Imprimindo o set inicial
print(set_inicial)

# elementos
set_inicial.add(15)
print(set_inicial)

# set com múltiplos elementos
set_inicial.update([1, 2, 3, 4, 5])
print(set_inicial)

# elemento removido
set_inicial.discard(13)
print(set_inicial)

# novo set
novo_set = {20, 21, 23, 1, 2}
print(novo_set)

# União dos sets
uniao = set_inicial.union(novo_set)
print(uniao)

# Interseção dos sets
intersecao = set_inicial.intersection(novo_set)
print(intersecao)

# Diferença entre os sets
diferenca = set_inicial.difference(novo_set)
print(diferenca)

# Diferença simétrica entre os sets
diferenca_simetrica = set_inicial.symmetric_difference(novo_set)
print(diferenca_simetrica)