def calcular_media(notas):
   
    return sum(notas) / len(notas)

def verificar_reprovacao(media):
 
    return media < 6

def imprimir_alunos_reprovados(alunos, reprovados):
   
    for matricula in reprovados:
        aluno = alunos[matricula]
        media = calcular_media(aluno['notas'])
        print(f"Aluno Reprovado: {aluno['nome']} - Matrícula: {matricula} - Média Final: {media}")