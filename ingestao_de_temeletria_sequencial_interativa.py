id_dispositivo = str(input("ID: "))  # 1
temperatura_lida = float(input("Temperatura: ").strip())  # 4
ciclos_executados = int(input("Ciclos: ").strip())  # 3
sensor_ativo = bool(
    input("Ativo? (responda com 's' ou deixe em branco): ").strip().lower()
)  # 2

if sensor_ativo in ["1", "true"]:
    sensor_ativo = True
else:
    sensor_ativo = False

print(id_dispositivo, ":", sensor_ativo, ":", temperatura_lida, "_", ciclos_executados)
