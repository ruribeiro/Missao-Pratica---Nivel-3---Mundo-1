from operacoes import calcular_media, verificar_reprovacao, imprimir_alunos_reprovados

# Dados dos alunos (exemplo)
alunos = {
    64: {'nome': 'rafael', 'notas': [7, 8, 6, 5]},
    31: {'nome': 'uchoa', 'notas': [9, 10, 8, 9]},
    97: {'nome': 'ribeiro', 'notas': [4, 5, 3, 2]}
}

# Encontrar os alunos reprovados
reprovados = []
for matricula, aluno in alunos.items():
    media = calcular_media(aluno['notas'])
    if verificar_reprovacao(media):
        reprovados.append(matricula)

# Imprimir os alunos reprovados
imprimir_alunos_reprovados(alunos, reprovados)