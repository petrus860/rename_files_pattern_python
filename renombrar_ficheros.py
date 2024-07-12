
import os
from pathlib import Path
import re

def renombrar_archivos(ruta_base):
    ruta_base = Path(ruta_base)
    patron = re.compile(r'.*\s-\scopia\..*')
    for carpeta, _, archivos in os.walk(ruta_base):
        for nombre_archivo in archivos:
            if patron.match(nombre_archivo):
                ruta_completa = Path(carpeta) / nombre_archivo
                nuevo_nombre = re.sub(r' \- copia', '', nombre_archivo)
                nueva_ruta = Path(carpeta) / nuevo_nombre
                if not nueva_ruta.exists():
                    os.rename(ruta_completa, nueva_ruta)
                    print(f"Renombrado: {ruta_completa} a {nueva_ruta}")
                else:
                    print(f"El archivo {nueva_ruta} ya existe. Se omite el renombrado de {ruta_completa}.")

# Ejemplo de uso
ruta_base = "C://ficheros/Documentos"
renombrar_archivos(ruta_base)