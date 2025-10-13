tempos_resposta = [50, 120, 450, 1200, 80, 950]

print("--- Classificação dos Tempos de Resposta ---")
for tempo in tempos_resposta:
     if tempo < 100:
          classificacao = "Excelente"
     elif 100 <= tempo <= 300:
          classificacao = "Bom"
     elif tempo <= 1000:
          classificacao = "Aceitável"
     else:
          classificacao = "Lento"
     print(f"Tempo: {tempo}ms -> {classificacao}")

