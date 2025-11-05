def fizzbuzz(n):

  for i in range(1, n + 1):
    match (i % 3, i % 5):
      case (0, 0):
        print('FizzBuzz')
      case (0, _):
        print('Fizz')
      case (_, 0):
        print('Buzz')
      case _:
        print(f"(n):{i} não é divisível por 3 ou 5")


try:
  numero_n = int(input("Digite um número (n): "))
  print(f"\n--- Executando FizzBuzz até {numero_n} ---")
  fizzbuzz(numero_n)

except ValueError:
  print("Erro: Por favor, digite um número inteiro válido.")