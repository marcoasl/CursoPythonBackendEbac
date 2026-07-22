# Dado um array meu_arrayzinho contendo X números distintos no intervalor [0, x]
# retorne o único número no intervalo que está faltando no array.


meu_arrayzinho = [0,1,2,3,4,6,7,8,9,10,44,88,99]


tamanho_meu_arrayzinho = len(meu_arrayzinho)
soma_valores_meu_arrayzinho = sum(meu_arrayzinho)


soma_total = tamanho_meu_arrayzinho * (tamanho_meu_arrayzinho + 1) // 2

print(soma_total - soma_valores_meu_arrayzinho)