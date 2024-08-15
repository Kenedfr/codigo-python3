dicionario = {
    1:{'nome': "Maria", "idade":26, "nacionalidade": "brasileira"}
    
}

dicionario.update({
    2: {'nome': 'Pedro', 'idade': 30, 'nacionalidade': 'português'},
    3: {'nome': 'Yuri', 'idade': 22, 'nacionalidade': 'japonesa'}
})

print(dicionario)

copia_dicionario = dicionario.copy()

elemento_removido = dicionario.pop(1)
print("elemento removido(chave 1):", elemento_removido)
print("Dicionario apos remoção", dicionario)

ultimo_elemento_removido = dicionario.popitem()
print("Ultimo elemnto removido:", ultimo_elemento_removido)
print("Dicionario após popitem:", copia_dicionario)

dicionario.clear()
copia_dicionario.clear()
print("Dicioanrio após clear:", dicionario)
print("Cópia do dicionario após clear:", copia_dicionario)

chaves = ["a", "b", "c",]
valor_padrao = 0
dicionario_novo = dict.fromkeys(chaves, valor_padrao)

print("items do novo dicionario:", dicionario_novo.items())
print("keys do novo dicionario:", dicionario_novo.keys())
print("values do novo dicionario:", dicionario_novo.values())
