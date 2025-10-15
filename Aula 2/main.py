"""
usuarios = ["Ana", "Bruna", "Carla", "Daniela", "Elisa"]
usuarios.append("Fernanda")
usuarios.insert(2, "Gabriela")
usuarios.remove("Ana")
usuarios[1] = "Beatriz"
usuarios[usuarios.index("Daniela")] = "Diana"
print(usuarios)
"""

cordenadas = (10.5, 20.3, 30.7)
x, y, z = cordenadas
#print(f"x: {x}, y: {y} z: {z}")


def obter_usario():
     return ("João", 28, "masculino")

nome, idade, genero = obter_usario()
#print(f"Nome: {nome}, Idade: {idade}, Gênero: {genero}")
