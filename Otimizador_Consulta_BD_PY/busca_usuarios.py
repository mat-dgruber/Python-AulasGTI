import time
import random

def criar_usuarios(num_usuarios):
     usuarios = []
     for n in range(num_usuarios):
          usuarios.append({
               'id': n,
               'nome': f'Usuario{n}',
               'email': f'usuario{n}@gmail.com'
          })
     return usuarios

def criar_index(usuarios):
     index_Id = {usuario['id']: usuario for usuario in usuarios}
     index_Nome = {usuario['nome']: usuario for usuario in usuarios}
     index_Email = {usuario['email']: usuario for usuario in usuarios}
     return index_Id, index_Nome, index_Email


def buscar_por_indice(criterio, valor, indices):

     index_id, index_nome, index_email = indices

     if criterio == 'id':
          return index_id.get(valor)
     elif criterio == 'nome':
          return index_nome.get(valor)
     elif criterio == 'email':
          return index_email.get(valor)
     return None

def buscar_linear(criterio, valor, usuarios):
     for usuario in usuarios:
          if usuario.get(criterio) == valor:
               return usuario
     return None
     
if __name__ == '__main__':
     num_usuarios = 10
     #10 e n 1000000000 para n estourar minha maquina

     print(f'Criando {num_usuarios} usuários...')
     usuarios = criar_usuarios(num_usuarios)

     print('\n Criando índices...')
     index_id, index_nome, index_email = criar_index(usuarios)
     indices = (index_id, index_nome, index_email)
    #index = criar_index(usuarios)

     print('\n Comparando a performace...')
     id_aleatorio = random.randint(0, num_usuarios - 1)
     email_aleatorio = f'usuario{random.randint(0, num_usuarios - 1)}@gmail.com'
     nome_aleatorio = f'Usuario{random.randint(0, num_usuarios - 1)}'

     criterios_busca = [
          ('id', id_aleatorio),
          ('email', email_aleatorio),
          ('nome', nome_aleatorio),
     ]


     for criterio, valor in criterios_busca:
        print(f"\n--- Buscando por '{criterio}' com o valor '{valor}' ---")
        
        # Performance da busca com índice
        inicio_indice = time.time()
        usuario_encontrado_indice = buscar_por_indice(criterio, valor, indices)
        fim_indice = time.time()
        tempo_indice = (fim_indice - inicio_indice) * 1000 # em milissegundos
        
        # Performance da busca linear
        inicio_linear = time.time()
        usuario_encontrado_linear = buscar_linear(criterio, valor, usuarios)
        fim_linear = time.time()
        tempo_linear = (fim_linear - inicio_linear) * 1000 # em milissegundos

        print(f"Busca com índice: Encontrado = {usuario_encontrado_indice is not None}. Tempo: {tempo_indice:.6f} ms")
        print(f"Busca linear: Encontrado = {usuario_encontrado_linear is not None}. Tempo: {tempo_linear:.6f} ms")

