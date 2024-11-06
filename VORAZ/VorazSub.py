def subasta_voraz(A, B, ofertas):
    n = len(ofertas)
    # Ordenar las ofertas por precio de mayor a menor
    ofertas_ordenadas = sorted(enumerate(ofertas), key=lambda x: x[1][0], reverse=True)

    total_precio = 0
    total_acciones = 0
    asignacion = [0] * n  # Asignación para los ofertantes

    for index, (p, m, M) in ofertas_ordenadas:
        if total_acciones >= A:
            break
        acciones_a_comprar = min(M, A - total_acciones)
        if acciones_a_comprar >= m:
            asignacion[index] = acciones_a_comprar
            total_precio += acciones_a_comprar * p
            total_acciones += acciones_a_comprar

    # Si hay acciones sobrantes, se compran al precio B
    

    return total_precio, asignacion