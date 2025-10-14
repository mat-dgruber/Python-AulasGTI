import locale

# Configura a localidade para o português do Brasil para formatação de moeda.
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    # Fallback para sistemas Windows
    locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')

class Funcionario:
     def __init__(self,nome, cargo, salario):
         
          if not nome or not isinstance(nome, str):
            raise ValueError("O nome do funcionário não pode ser vazio.")
          
          if not isinstance(salario, (int, float)) or salario <= 0:
            raise ValueError("O salário deve ser um número positivo.")
          

          self.nome = nome
          self.cargo = cargo
          self._salario = salario

     def calcular_bonus(self) -> float:
         return self._salario * 0.10
     
     @property
     def salario(self):
        return self._salario
     
     def __str__(self) -> str:
        """Representação em string do objeto Funcionario."""
        return f"Funcionario(Nome: {self.nome}, Cargo: {self.cargo}, Salário: {locale.currency(self._salario, symbol=True, grouping=True)}, Bônus: {locale.currency(self.calcular_bonus(), symbol=True, grouping=True)})"
     
     def __repr__(self) -> str:
        """Representação 'oficial' do objeto Funcionario."""
        return f"Funcionario(nome='{self.nome}', cargo='{self.cargo}', salario={self._salario}, bonus={self.calcular_bonus()})"