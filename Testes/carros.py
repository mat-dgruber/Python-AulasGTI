class Carro:
     def __init__(self, 
                  marca: str, 
                  modelo: str, 
                  ano: int,
                  preco: float):
          self.marca = marca
          self.modelo = modelo
          self.ano = ano
          self.preco = preco

     def __repr__(self):
          return f"Carro(marca = {self.marca}, modelo = {self.modelo}, ano ={self.ano}, preco = {self.preco})"
     
     def __str__(self):
          return f"{self.marca} {self.modelo} ({self.ano}) → R$ {self.preco:.2f}"
     
if __name__ == "__main__":
     ka = Carro("Ford", "KA", 2000, 2000.00)
     print(ka)