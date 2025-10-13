# *args e **kwargs (flexibilidade total)
def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

resultado = soma(1, 2, 3, 4, 5)
print("Soma:", resultado)


def exibir_info(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

exibir_info(nome="Ana", idade=25, cidade="São Paulo")



def funcao_completa(obrigatorio, opcional=None, *args, **kwargs):
    print("Obrigatório:", obrigatorio)
    print("Opcional:", opcional)
    print("Args:", args)
    print("Kwargs:", kwargs)

funcao_completa("Valor Obrigatório", 42, "extra1", "extra2", chave1="valor1", chave2="valor2")