class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self._cpf = cpf  # Atributo privado

    @property
    def cpf(self):
        return self._cpf

        @cpf.setter
        def cpf(self, valor):
          if len(valor) != 11 or not valor.isdigit():
              raise ValueError("CPF inválido")
          self._cpf = valor

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."
    
    def __str__(self):
        return f"Pessoa(nome={self.nome}, idade={self.idade})"
    
    def __repr__(self):
        return self.__str__()

pessoa = Pessoa("João", 30, "123.456.789-00")
print(pessoa.apresentar())
pessoa.idade = 31
print(pessoa.apresentar())