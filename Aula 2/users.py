cache_users = {}

def obter_usuario(user_id: int):
     if user_id in cache_users:
          print("Retornando usuário do cache.")
          return cache_users[user_id]
     
     # Simula uma operação custosa, como uma consulta a um banco de dados.
     print("Buscando usuário no banco de dados...")
     usuario = {
          "id": user_id,
          "nome": f"Usuário{user_id}",
          "email": f"Email do Usuário{user_id}" "@example.com"
     }
     cache_users[user_id] = usuario
     return usuario

user1 = obter_usuario(1)
user2 = obter_usuario(1)
user3 = obter_usuario(2)


print("Total em cache:" , len(cache_users))
print(f"IDs em cache: {list(cache_users.keys())}")