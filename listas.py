#lista 
lista_mesclada = [1, 2, 3, "Olá, Python", True, 12.6]

# Imprimindo a lista inicial
print("Lista inicial:", lista_mesclada)

# Adicionando uma lista aninhada usando o método append
lista_mesclada.append(["Lista aninhada"])

# Imprimindo a lista após a adição
print("Lista após adicionar a lista aninhada:", lista_mesclada)

#inserção - 5 na posição 4
lista_mesclada.insert(4, 5)
print(lista_mesclada)

#impressão tamanho
print("Tamanho da lista:", len(lista_mesclada))

# Remoção de item na posição 1
lista_mesclada.pop(1)
print("Lista após remover o item na posição 1:", lista_mesclada)

#  nova lista com os itens até a posição 4 
nova_lista_mesclada = lista_mesclada[:5]
print("Nova lista com os itens até a posição 4:", nova_lista_mesclada)