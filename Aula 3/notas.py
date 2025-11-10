# 2. Função para Processar Notas

print("--- Processamento de Notas ---")

def processar_notas(notas: list) -> float:
    """
    Recebe uma lista de notas, remove a nota mais baixa
    e retorna a média das notas restantes.
    """
    if not notas:
        print("A lista de notas está vazia.")
        return 0.0

    # Encontra a nota mais baixa usando min()
    nota_mais_baixa = min(notas)
    print(f"Notas originais: {notas}")
    print(f"Nota mais baixa a ser removida: {nota_mais_baixa}")

    # Cria uma cópia da lista para não modificar a original fora da função
    notas_copia = list(notas)

    # Remove a primeira ocorrência da nota mais baixa
    notas_copia.remove(nota_mais_baixa)
    print(f"Notas restantes: {notas_copia}")

    # Calcula e retorna a média das notas restantes
    if not notas_copia:
        print("Não há notas restantes para calcular a média.")
        return 0.0

    media_restantes = sum(notas_copia) / len(notas_copia)
    return media_restantes

# --- Exemplo de uso da função ---
minhas_notas = [8.5, 7.0, 9.0, 5.5, 10.0]
media_final = processar_notas(minhas_notas)

print(f"A média das notas (após remover a mais baixa) é: {media_final:.2f}")

# Exemplo com a nota mais baixa duplicada
notas_duplicadas = [10.0, 5.0, 8.0, 5.0]
media_duplicada = processar_notas(notas_duplicadas)
print(f"\nExemplo com nota duplicada:")
print(f"Notas: {notas_duplicadas}")
# .remove() só remove a primeira ocorrência
print(f"A média (após remover uma nota 5.0) é: {media_duplicada:.2f}")