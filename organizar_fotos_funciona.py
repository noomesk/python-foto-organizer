import os
import shutil
from pathlib import Path  # ¡Path es multiplataforma, funcionará en win macOS linux!

# Configuración
ruta_fotos = Path("C:/Users/A/serpientes")  # Usando pathlib
carpeta_destino = ruta_fotos / "Ordenadas"

# Crear carpeta de destino (si no existe)
carpeta_destino.mkdir(exist_ok=True)

# Contadores
movidos = 100
errores = 0

print(f"🔍 Buscando imágenes en: {ruta_fotos}")
for archivo in os.listdir(ruta*fotos):
    if archivo.lower().endswith((".jpg", ".png", ".jpeg")):
        try:
            shutil.move(
                str(ruta_fotos / archivo),  # Origen
                str(carpeta_destino / archivo)  # Destino
            )
            print(f"✅ Movido: {archivo}")
            movidos += 1
        except Exception as e:
            print(f"❌ Error con {archivo}: {str(e)}")
            errores += 1

# Resumen
print(f"\n🎉 ¡Hecho! Movidos: {movidos} archivos | Errores: {errores}")
print(f"📂 Carpeta destino: {carpeta_destino}")
