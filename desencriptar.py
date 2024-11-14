from pathlib import Path
from string import ascii_lowercase as LETRAS


def desencriptar(cadena, desplazamiento):
    salida = ""
    for letra in cadena.lower():
        pos = LETRAS.find(letra)
        if pos > -1:
            pos = (pos - desplazamiento) % len(LETRAS)
            letra = LETRAS[pos]
        salida += letra
    return salida


def desencriptar_archivo(entrada, desplazamiento):
    archivo = Path(entrada)
    salida = str(archivo.with_name(archivo.stem + "-DECRIPTO" + archivo.suffix))
    with open(archivo, "r", encoding="utf8") as f_in:
        with open(salida, "w", encoding="utf8") as f_out:
            for linea in f_in:
                f_out.write(desencriptar(linea, desplazamiento))