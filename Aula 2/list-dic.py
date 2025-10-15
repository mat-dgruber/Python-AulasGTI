numeros = [1, 2, 3, 4, 5]

quadrados = [n ** 2 for n in numeros]

quadrados_pares = [n** 2 for n in numeros if n % 2 == 0]

print(quadrados)
print(quadrados_pares)


#[expressão for item in iterável if condição]
