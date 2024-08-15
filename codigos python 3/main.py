from operacoes import calcular_media, verificar_reprovacao, exibir_reprovados

dados_alunos = {
    101: {'nome': 'Julia', 'notas': [6, 6, 7, 8]},
    102: {'nome': 'João', 'notas': [4, 5, 6, 4]},
    103: {'nome': 'Yuri', 'notas': [9, 8, 7, 9]},
    104: {'nome': 'Pedro', 'notas': [3, 4, 5, 2]}
}

for matricula, dados in dados_alunos.items():
    dados['media'] = calcular_media(dados['notas'])

matriculas_reprovados = [
    matricula for matricula, dados in dados_alunos.items()
    if verificar_reprovacao(dados['media'])
]

exibir_reprovados(dados_alunos, matriculas_reprovados)