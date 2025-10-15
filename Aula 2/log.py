from collections import namedtuple

LogEntry = namedtuple("LogEntry", ["timestamp", "message", "status_code"])

logs = [
     LogEntry("2023-10-01 10:00:00", "User logged in", 200),
     LogEntry("2023-10-01 10:05:00", "User viewed dashboard", 400),
     LogEntry("2023-10-01 10:15:00", "User logged out", 500),
     LogEntry("2023-10-01 10:20:00", "User logged in", 200),
     LogEntry("2023-10-01 10:25:00", "User updated profile", 300),
     LogEntry("2023-10-01 10:30:00", "User logged out", 500),
]

erros = [log for log in logs if log.status_code >= 400]

acao = [log.message for log in logs]

ultimos_logs = logs[-2:]

"""
print("------Últimos Logs------")
print(ultimos_logs)
print("------Erros------")
print(erros)
print("------Ações------")
print(f"Logins: {acao.count('User logged in')}")
print(acao)
"""

print("------Desempacotamento------")
print(f"Total de erros: {len(erros)}")


logs_ordendados = sorted(logs, key=lambda log: log.status_code, reverse=True)