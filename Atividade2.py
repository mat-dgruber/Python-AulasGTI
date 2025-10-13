def classificar_resposta(tempo_ms):
    if tempo_ms < 100:
        return "Excelente"
    elif 100 <= tempo_ms <= 300:
        return "Bom"
    elif 300 < tempo_ms <= 1000:
        return "Aceitável"
    else:
        return "Lento"

tempos_resposta = [50, 120, 450, 1200, 80, 950]

print("--- Classificação dos Tempos de Resposta ---")
for tempo in tempos_resposta:
    classificacao = classificar_resposta(tempo)
    print(f"Tempo: {tempo}ms -> {classificacao}")

