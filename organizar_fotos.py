import os
import shutil

# Usa esta ruta (cámbiala por la TUYA dependiendo de lo que vayas a organizar amigue):
ruta_fotos = r"C:\Users\A\serpientes"  # ¡Observa la 'r' al inicio y sin doble \\ eso ayuda a que no se confunda con el \ que python lo interpreta como un escape)

# Crea la carpeta "Ordenadas" si no existe
os.makedirs(os.path.join(ruta_fotos, "Ordenadas"), exist_ok=True)

for archivo in os.listdir(ruta_fotos):
    if archivo.lower().endswith((".jpg", ".png")):
        try:
            shutil.move(
                os.path.join(ruta_fotos, archivo),
                os.path.join(ruta_fotos, "Ordenadas", archivo)
            )
            print(f"✅ Movido: {archivo}")
        except Exception as e:
            print(f"❌ Error con {archivo}: {str(e)}")

print("¡Proceso completado! Revisa la carpeta 'Ordenadas'.")
