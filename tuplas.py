#tupla
primeira_tupla = (1, 2, 3, 4, "Olá, tupla")

print("A tupla é:", primeira_tupla)

# índice do elemento 4
indice_do_quatro = primeira_tupla.index(4)
print("O índice do elemento 4 é:", indice_do_quatro)

# busca elemento 3
contem_tres = 3 in primeira_tupla
print("A tupla contém o elemento 3?", contem_tres)

# busca elemento 33
contem_trinta_e_tres = 33 in primeira_tupla
print("A tupla contém o elemento 33?", contem_trinta_e_tres)