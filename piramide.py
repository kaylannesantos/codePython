def calcular_altura_piramide(blocos):
    altura = 0  # Número de camadas completas
    blocos_necessarios = 1  # Blocos necessários para a próxima camada

    while blocos >= blocos_necessarios:
        blocos -= blocos_necessarios  # Usando blocos para completar a camada
        altura += 1  # Aumentando a altura da pirâmide
        blocos_necessarios += 1  # Blocos necessários para a próxima camada

    return altura

# Exemplo de uso:
blocos = int(input("Digite o número de blocos: "))
altura = calcular_altura_piramide(blocos)
print(f"A altura da pirâmide é {altura} camadas completas")
