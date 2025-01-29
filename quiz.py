def un_paso(v, f, t, m):
    """
    Calcula el cambio de posición y la velocidad final en un paso del sistema.
    
    Parámetros:
    - v: vector de velocidad (tupla o lista, ej. [vx, vy])
    - f: vector de fuerza (tupla o lista, ej. [fx, fy])
    - t: escala de tiempo (float)
    - m: masa del objeto (float)
    
    Retorna:
    - delta_pos: vector de desplazamiento (tupla o lista)
    - v_f: vector de velocidad final (tupla o lista)
    """
    # Calculamos la aceleración
    a = [force / m for force in f]  # Aceleración en cada dirección
    
    # Calculamos la nueva velocidad
    v_f = [vi + ai * t for vi, ai in zip(v, a)]
    
    # Calculamos el cambio de posición
    delta_pos = [vi * t + 0.5 * ai * t**2 for vi, ai in zip(v, a)]
    
    return delta_pos, v_f


def acumula_pasos(pos_i, v_i, kv, pasos, t, m):
    """
    Calcula la trayectoria acumulada del sistema en varios pasos.
    
    Parámetros:
    - pos_i: posición inicial (tupla o lista, ej. [x, y])
    - v_i: velocidad inicial (tupla o lista, ej. [vx, vy])
    - kv: constante de viscosidad (float)
    - pasos: número de pasos a calcular (int)
    - t: escala de tiempo para cada paso (float)
    - m: masa del objeto (float)
    
    Retorna:
    - Lista_pasos: lista de posiciones acumuladas
    """
    Lista_pasos = []  # Lista para almacenar las posiciones en cada paso
    v = v_i
    pos = pos_i
    kv_n = -kv  # Factor de amortiguación (negativo)
    
    for _ in range(pasos):
        # Calculamos la fuerza viscosa
        f = [kv_n * vi for vi in v]
        
        # Calculamos el cambio de posición y la nueva velocidad
        delta_pos, v = un_paso(v, f, t, m)
        
        # Actualizamos la posición
        pos = [p + dp for p, dp in zip(pos, delta_pos)]
        
        # Almacenamos la nueva posición
        Lista_pasos.append(pos)
    
    return Lista_pasos

# Parámetros iniciales
pos_i = [0, 0]  # Posición inicial
v_i = [10, 10]  # Velocidad inicial
kv = 0.1        # Constante de viscosidad
pasos = 10      # Número de pasos
t = 1           # Intervalo de tiempo por paso
m = 1           # Masa del sistema

# Llamada a la función
trayectoria = acumula_pasos(pos_i, v_i, kv, pasos, t, m)
print("Trayectoria acumulada:", trayectoria)
