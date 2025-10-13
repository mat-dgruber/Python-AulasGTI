def main(): 
    id_usuario = 1817
    nome_usuario = "Matheus Diniz"
    email_usuario = "matheus.diniz@cpb.com.br"
    conta_ativa = True
    tags = ["premium", "email_confirmado", "notAdmin"]  
    perfil = criar_usuario(nome_usuario, 30)

    print(f"ID: {id_usuario} (tipo: {type(id_usuario)})")
    print(f"Nome: {nome_usuario} (tipo: {type(nome_usuario)})")
    print(f"Email: {email_usuario} (tipo: {type(email_usuario)})")
    print(f"Ativo: {conta_ativa} (tipo: {type(conta_ativa)})")
    print(f"Tags: {tags} (tipo: {type(tags)})")


def criar_usuario(nome: str, idade: int) -> dict[str, str | int]:
     return {"nome": nome, "idade": idade}






