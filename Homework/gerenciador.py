from funcionarios import Funcionario
from typing import List

def adicionar_funcionario(funcionarios: List[Funcionario], funcionario: Funcionario):
    
    if not isinstance(funcionario, Funcionario):
        raise TypeError("Apenas objetos da classe Funcionario podem ser adicionados.")
    if not funcionario.nome or funcionario.salario < 0:
         raise ValueError("Nome inválido ou salário negativo.")
        
    
    funcionarios.append(funcionario)

def listar_por_cargo(funcionarios: List[Funcionario], cargo: str) -> List[Funcionario]:
    funcionarios_filtrados = [f for f in funcionarios if f.cargo.lower() == cargo.lower()]
    return funcionarios_filtrados

def calcular_folha_total(funcionarios: List[Funcionario]):
    folha_total= 0.0
    for funcionario in funcionarios:
        salario_com_bonus = funcionario.salario + funcionario.calcular_bonus()
        folha_total += salario_com_bonus
     
    return folha_total


#--------------------------------------------------------
if __name__ == '__main__':
    # 1. Setup da lista
    funcionarios: List[Funcionario] = []
    
    # 2. Cadastro de Funcionários
    try:
        f1 = Funcionario("João Silva", "Desenvolvedor", 6000.00)
        f2 = Funcionario("Maria Souza", "Gerente", 12000.00)
        f3 = Funcionario("Pedro Reis", "Desenvolvedor", 4500.00)
        f4 = Funcionario("Ana Lima", "Analista RH", 7000.00)

        adicionar_funcionario(funcionarios, f1)
        adicionar_funcionario(funcionarios, f2)
        adicionar_funcionario(funcionarios, f3)
        adicionar_funcionario(funcionarios, f4)

        print("\n--- Funcionários Cadastrados ---")
        for f in funcionarios:
            print(f)

    except ValueError as e:
        print(f"ERRO DE VALIDAÇÃO: {e}")
    except TypeError as e:
        print(f"ERRO DE TIPO: {e}")

    # 3. Listar por Cargo
    print("\n--- Listar Desenvolvedores ---")
    desenvolvedores = listar_por_cargo(funcionarios, "Desenvolvedor")
    for d in desenvolvedores:
        print(f"- {d.nome}, Bônus: R${d.calcular_bonus():.2f}")

    # 4. Calcular Folha de Pagamento Total
    folha = calcular_folha_total(funcionarios)
    print(f"\n--- Folha de Pagamento Total ---")
    print(f"Total a pagar (Salários + Bônus): R${folha:.2f}")

    # 5. Teste de Validação (Opcional)
    print("\n--- Teste de Validação (Nome Vazio) ---")
    try:
        Funcionario("", "Estagiário", 1500.00)
    except ValueError as e:
        print(f"Erro esperado capturado: {e}")

    print("\n--- Teste de Validação (Salário Negativo) ---")
    try:
        Funcionario("Teste Salário", "Estagiário", -100.00)
    except ValueError as e:
        print(f"Erro esperado capturado: {e}")