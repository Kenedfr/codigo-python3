set_inicial = {11, 12, 13, 14}
print("Set inicial:", set_inicial)

set_inicial.add(15)
print("Após adicionar 15:", set_inicial)

set_inicial.update([1, 2, 3, 4, 5])
print("Após atualizar com 1, 2, 3, 4, 5:", set_inicial)

set_inicial.discard(13)
print("Após remover o 13:", set_inicial)

novo_set = {20, 21, 23, 1, 2}
print("Novo set:", novo_set)

print("União dos sets:", set_inicial.union(novo_set))

print("Interseção dos sets:", set_inicial.intersection(novo_set))

print("Diferença entre set_inicial e novo_set:", set_inicial.difference(novo_set))

print("Diferença simétrica entre os sets:", set_inicial.symmetric_difference(novo_set))
