

def fuerza_bruta_sub(A, B, ofertas, idx=0):
    # Caso base: Si no hay más oferentes, asignamos todas las acciones al gobierno
    if idx == len(ofertas):
        return A * B, [A]  # El gobierno compra todas las acciones restantes

    # Datos del oferente actual
    pi, mi, Mi = ofertas[idx]
    
    # Inicializamos el valor máximo y la mejor asignación
    valor_maximo = -float('inf')
    mejor_asignacion = []

    # Probar todas las posibles asignaciones de acciones para este oferente
    for xi in range(mi, min(Mi, A) + 1):
        # Llamada recursiva para los oferentes restantes
        valor_restante, asignacion_restante = fuerza_bruta_sub(A - xi, B, ofertas, idx + 1)

        # Calcular el valor total si asignamos xi acciones al oferente actual
        valor_actual = xi * pi + valor_restante

        # Actualizar si encontramos una mejor solución
        if valor_actual > valor_maximo:
            valor_maximo = valor_actual
            mejor_asignacion = [xi] + asignacion_restante

    return valor_maximo, mejor_asignacion

# Función para encontrar la mejor asignación de acciones
def fuerza_bruta_sub_aux(A, B, ofertas):
    max_valor, mejor_asignacion = fuerza_bruta_sub(A, B, ofertas)
    print(max_valor)
    print(mejor_asignacion)