from collections import defaultdict

pedidos = [ # Mantido como lista de dicionários para este exemplo
    {"cliente": "Ana", "valor": 50.00},
    {"cliente": "Bruno", "valor": 150.00},
    {"cliente": "Ana", "valor": 80.00},  # Ana: 130 total
    {"cliente": "Carlos", "valor": 30.00},
    {"cliente": "Bruno", "valor": 50.00},  # Bruno: 200 total
]


totais_por_cliente = defaultdict(float)
for pedido in pedidos:
    totais_por_cliente[pedido['cliente']] += pedido['valor']

clientes_premium = {
    cliente: total_gasto
    for cliente, total_gasto in totais_por_cliente.items()
    if total_gasto > 100.00
}

print(clientes_premium)

"""
from collections import defaultdict

totais = defaultdict(float)
for pedido in pedidos:
    totais[pedido["cliente"]] += pedido["valor"]

cliente_vip = {cliente: total for cliente, total in totais.items() if total > 100}
print(cliente_vip)  # Saída esperada: {'Ana': 130.0, 'Bruno': 200.0}

"""