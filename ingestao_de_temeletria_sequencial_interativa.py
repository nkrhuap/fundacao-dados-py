# Contexto de Mercado: Sensores de IoT e agentes de monitoramento emitem métricas em formatos brutos de texto. Um coletor de métricas precisa normalizar essas informações para os tipos primitivos corretos antes de alimentar um banco de dados analítico.
# Objetivo: Construir um script de parsing básico que receba entradas manuais via input() e faça a conversão controlada para os tipos adequados.
#
# Requisitos:
# - O script deve solicitar via terminal: id_dispositivo (texto), temperatura_lida (número com casas decimais), ciclos_executados (número inteiro) e sensor_ativo (texto representando booleano, ex: "true" ou "false").
# - Realize a conversão explícita de cada variável para o seu tipo canônico (str, float, int, bool).
# - A conversão booleana deve tratar explicitamente a entrada de texto, garantindo que "false" ou "False" resulte no booleano False e "true" ou "True" resulte em True.
#
# Critério de Conclusão: O programa deve imprimir na tela o tipo primitivo de cada variável após a conversão, provando que nenhum tipo foi preservado como str por omissão.
#
# Abordagem Sequencial Interativa (Múltiplos input()): O programa faz perguntas sequenciais ao usuário, pausando a execução a cada campo:
id_dispositivo = str(input("ID: "))  # 1
temperatura_lida = float(input("Temperatura: ").strip())  # 4
ciclos_executados = int(input("Ciclos: ").strip())  # 3
sensor_ativo = str(input("Ativo? (Responda com 1 ou True): ").strip().lower())  # 2

if sensor_ativo in ["1", "true"]:
    sensor_ativo = True
else:
    sensor_ativo = False

print(
    "id_dispositivo: ",
    id_dispositivo,
    " ",
    type(id_dispositivo).__name__,
    " | ",
    "temperatura_lida: ",
    temperatura_lida,
    " ",
    type(temperatura_lida).__name__,
    " | ",
    "ciclos_executados: ",
    ciclos_executados,
    " ",
    type(ciclos_executados).__name__,
    " | ",
    "sensor_ativo: ",
    sensor_ativo,
    " ",
    type(sensor_ativo).__name__,
)
