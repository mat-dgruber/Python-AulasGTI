class Funcionario:
     def __init__(self,nome, cargo, salario):
         
          if not nome or not isinstance(nome, str):
            raise ValueError("O nome do funcionário não pode ser vazio.")
          
          if not isinstance(salario, (int, float)) or salario <= 0:
            raise ValueError("O salário deve ser um número positivo.")
          

          self.nome = nome
          self.cargo = cargo
          self.salario = salario

     def calcular_bonus(self) -> float:
         return self.salario * 0.10
     
     
     def __str__(self) -> str:
        """Representação em string do objeto Funcionario."""
        return f"Funcionario(Nome: {self.nome}, Cargo: {self.cargo}, Salário: R${self.salario:.2f})"
     
     def __repr__(self) -> str:
        """Representação 'oficial' do objeto Funcionario."""
        return f"Funcionario(nome='{self.nome}', cargo='{self.cargo}', salario={self.salario})"