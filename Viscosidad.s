# Rutina de un solo paso
# Simula una operación matemática básica y un almacenamiento
# Usaremos MOV, ADD, y ST como instrucciones base

backend 0
# Inicializar valores en registros
MOV R1, 5        # R1 = 5
MOV R2, 10       # R2 = 10

# Realizar suma R3 = R1 + R2
ADDcc R3, R1, R2 # R3 = R1 + R2, actualiza banderas

# Almacenar resultado en memoria
malloc R5, 4     # Reserva 4 bytes de memoria en R5
ST [R5], R3      # Almacena el contenido de R3 en la dirección apuntada por R5

# Rutina de comparación
MOV R4, 15       # R4 = 15
SUBcc R0, R3, R4 # Compara R3 con R4, actualiza banderas

# Salto condicional si Z (Zero flag) está activo
BzC -2           # Regresa a una instrucción si la comparación da cero
NOP              # Instrucción de no operación
