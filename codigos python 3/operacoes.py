def calcular_media(notas):
    """
    Calcula a média das notas dos 4 bimestres de um aluno.
    :param notas: Lista de notas dos 4 bimestres.
    :return: Média das notas.
    """
    return sum(notas) / len(notas)

def verificar_reprovacao(media):
    """
    Verifica se o aluno foi reprovado com base na média.
    :param media: Média do aluno.
    :return: True se o aluno foi reprovado, False caso contrário.
    """
    return media < 6

def exibir_reprovados(dados_alunos, matriculas_reprovados):
    """
    Exibe os dados dos alunos reprovados.
    :param dados_alunos: Dicionário com os dados dos alunos.
    :param matriculas_reprovados: Lista com as matrículas dos alunos reprovados.
    :return: Nenhum valor de retorno. Apenas imprime os dados dos alunos reprovados.
    """
    for matricula in matriculas_reprovados:
        aluno = dados_alunos.get(matricula)
        if aluno:
            print(f"Aluno Reprovado: {aluno['nome']} – Matrícula: {matricula} – Média Final: {aluno['media']:.2f}")