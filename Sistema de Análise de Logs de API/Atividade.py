from collections import Counter, defaultdict

def analisar_logs(logs):

     contagem_metodos = Counter()
     contagem_endpoints = Counter()
     contagem_usuarios = Counter()
     tempos_resposta_por_endpoint = defaultdict(int)

     total_erros = 0

     def gerar_log_linhas(logs):
          for linha in logs:
               yield linha

     for linha in gerar_log_linhas(logs):
          try:
               _, metodo, endpoint, status_str, tempo_str, user_id = linha.split('|')
               status = int(status_str)
               tempo_ms = int(tempo_str.strip('ms'))
               
               contagem_metodos[metodo] += 1
               contagem_endpoints[endpoint] += 1
               contagem_usuarios[user_id] += 1
               tempos_resposta_por_endpoint[endpoint] += tempo_ms

               if status >= 400:
                    total_erros += 1
          except (ValueError, IndexError) as e:
               print(f"Aviso: Linha de log inválida ignorada - {linha} - Erro: {e}")

     endpoint_mais_acessado = contagem_endpoints.most_common(1)
     usuario_mais_ativo = contagem_usuarios.most_common(1)

     tempo_medio_por_endpoint = {
          endpoint: tempos_resposta_por_endpoint[endpoint] / contagem
          for endpoint, contagem in contagem_endpoints.items()
     }

     metricas = {
          "total_requisicoes": sum(contagem_metodos.values()),
          "por_metodo": dict(contagem_metodos),
          "total_erros": total_erros,
          "endpoint_mais_acessado": endpoint_mais_acessado[0][0] if endpoint_mais_acessado else "N/A",
          "usuario_mais_ativo": usuario_mais_ativo[0][0] if usuario_mais_ativo else "N/A",
          "tempo_medio_por_endpoint": tempo_medio_por_endpoint
     }

     return metricas



logs = [
    "2024-10-11 10:23:45|GET|/api/products/123|200|150ms|user_456",
    "2024-10-11 10:23:46|POST|/api/orders|201|300ms|user_789",
    "2024-10-11 10:23:47|GET|/api/products/456|404|50ms|user_456",
    "2024-10-11 10:23:48|GET|/api/users/789|200|100ms|user_123",
    "2024-10-11 10:23:49|DELETE|/api/orders/999|500|500ms|user_789",
    "2024-10-11 10:23:50|GET|/api/products/123|200|120ms|user_456",
    "2024-10-11 10:23:51|GET|/api/products/123|200|130ms|user_456"
]

# Chama a função para analisar os logs
resultado = analisar_logs(logs)

# Imprime o relatório formatado
print("\n--- Relatório de Análise de Logs ---")
print(f"Total de requisições: {resultado['total_requisicoes']}")
print(f"Total de erros (status >= 400): {resultado['total_erros']}")
print("\nRequisições por método HTTP:")
for metodo, total in resultado['por_metodo'].items():
    print(f"  - {metodo}: {total}")
print(f"\nEndpoint mais acessado: {resultado['endpoint_mais_acessado']}")
print(f"Usuário com mais requisições: {resultado['usuario_mais_ativo']}")
print("\nTempo médio de resposta por endpoint:")
for endpoint, tempo_medio in resultado['tempo_medio_por_endpoint'].items():
    print(f"  - {endpoint}: {tempo_medio:.2f}ms")
print("-------------------------------------")