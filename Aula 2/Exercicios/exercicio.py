
pedidos = [
    (1, "Ana", 150.00, "pago"),
    (2, "Bruno", 200.00, "pendente"),
    (3, "Ana", 100.00, "pago"),
    (4, "Carlos", 300.00, "pendente"),
    (5, "Ana", 50.00, "cancelado"),
]

pedidos_pendentes = [pedido for pedido in pedidos if pedido[3] == "pendente"]

valor_total = sum(p[2] for p in pedidos if p[3] != "cancelado")

from collections import Counter
clientes = [pedido[1] for pedido in pedidos]
top_cliente = Counter(clientes).most_common(1)[0][0]

print("--- Análise de Pedidos ---")
print("\n(1) Pedidos Pendentes:")
for pedido in pedidos_pendentes:
    print(f"  - ID: {pedido[0]}, Cliente: {pedido[1]}, Valor: R${pedido[2]:.2f}")

print(f"\n(2) Valor Total de todos os pedidos: R${valor_total:.2f}")
print(f"\n(3) Cliente com mais pedidos: {top_cliente}")