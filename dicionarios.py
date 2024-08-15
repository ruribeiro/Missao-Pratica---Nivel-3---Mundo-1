#dicionário
meu_dicionario = {
    1: {"nome": "Python", "tipo": "interpretada"},
    2: {"nome": "Java", "tipo": "compilada"},
    3: {"nome": "PHP", "tipo": "interpretada"}
}
# Imprimindo os valores das chaves "nome" e "tipo" para as chaves 1 e 2
print("Linguagem 1:", meu_dicionario[1]["nome"], "-", meu_dicionario[1]["tipo"])
print("Linguagem 2:", meu_dicionario[2]["nome"], "-", meu_dicionario[2]["tipo"])

# Criando um dicionário aninhado para frutas
dicionario_frutas = {}
dicionario_frutas[1] = {"nome": "limão", "tipo": "ácida"}
dicionario_frutas[2] = {"nome": "laranja", "tipo": "ácida"}
dicionario_frutas[3] = {"nome": "manga", "tipo": "semiácida"}
dicionario_frutas[4] = {"nome": "maçã", "tipo": "semiácida"}
dicionario_frutas[5] = {"nome": "banana", "tipo": "doce"}
dicionario_frutas[6] = {"nome": "mamão", "tipo": "doce"}

# Imprimindo o dicionário de frutas
print("Dicionário de frutas:", dicionario_frutas)

# Imprimindo o tipo do dicionário
print("Tipo do dicionário:", type(dicionario_frutas))

# Imprimindo o valor da chave "linguagem" (isso irá gerar um erro, pois não existe essa chave)
# print("Valor da chave 'linguagem':", meu_dicionario.get("linguagem"))

# Imprimindo o tamanho do dicionário de frutas
print("Tamanho do dicionário de frutas:", len(dicionario_frutas))

# Iterando sobre o dicionário de frutas e imprimindo os valores
for chave, valor in dicionario_frutas.items():
    print("Fruta", chave, ":", valor["nome"], "-", valor["tipo"])