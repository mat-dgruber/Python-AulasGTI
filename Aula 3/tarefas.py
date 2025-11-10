# 1. Lista de Tarefas
print("--- Lista de Tarefas ---")

# Cria uma lista de tarefas vazia
tarefas = []
print(f"Lista inicial: {tarefas}")

# Adiciona três tarefas (strings) a ela
tarefas.append("Fazer compras")
tarefas.append("Estudar Python") # Esta é a segunda tarefa (índice 1)
tarefas.append("Lavar o carro")
print(f"Depois de adicionar 3 tarefas: {tarefas}")

# Remove a segunda tarefa.
# A segunda tarefa está no índice 1 (listas começam do 0)
# Usamos .pop() para remover pelo índice.
tarefas.pop(1)
print(f"Depois de remover a 2ª tarefa: {tarefas}")

# Imprime o número de tarefas restantes usando len()
num_tarefas_restantes = len(tarefas)
print(f"Número de tarefas restantes: {num_tarefas_restantes}")

print("\n" + "="*30 + "\n")