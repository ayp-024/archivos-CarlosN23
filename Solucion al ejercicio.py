with open('data/calificaciones.txt', 'r') as f_in, open('data/promedios.txt', 'w') as f_out:
    for linea in f_in:
        partes = linea.strip().split()
        nombre, apellido = partes[0], partes[1]
        calificaciones = [int(cal) for cal in partes[2:]]
        promedio = sum(calificaciones) / len(calificaciones)
        f_out.write(f"{apellido.upper()}, {nombre}: {promedio:.1f}\n")
