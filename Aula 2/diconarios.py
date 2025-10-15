usario = {
     "id": 1,
     "nome": "João",
     "email": "joao@email.com",
     "ativo": True
}




for chave in usario:
     print(f"{chave}: {usario[chave]}")

for chave, valor in usario.items():
     print(f"{chave} : {valor}")

for valor in usario.values():
     print(valor)

for chave in usario.keys():
     print(chave)