# 🐍 Organizador de Fotos Automático  prueba (usado en mi laboratorio para organizar fotos de serpientes)

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Organizador](https://img.shields.io/badge/🐍-organizador%20de%20fotos-yellow)


Clasifica imágenes `.jpg`, `.png` y `.jpeg` en una subcarpeta llamada ruk `Ordenadas`.

##  Cómo Usar: -m
1. **Editar la ruta** en `organizar_fotos.py`:
   ```python
   ruta_fotos = Path("C:/Users/A/serpientes")  # ← Cambiar por tu ruta
   ```
2. **Ejecutar**:
   ```bash
   python organizar_fotos.py
   ```

##  Funciones que son bien importantes revisar:
| Función/Línea           | Explicación                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| `pathlib.Path`          | Maneja rutas de forma segura (Windows/Linux/MacOS).           #es multiplataforma               |
| `carpeta_destino.mkdir()` | Crea la carpeta `Ordenadas` si no existe. #(mkdir iwal que en linux)                               |
| `shutil.move()`         | Mueve archivos evitando errores de permisos.                               |

## 🔍 Explicación Técnica
```python
if archivo.lower().endswith((".jpg", ".png", ".jpeg")):
```
- **`.lower()`**: Convierte el nombre a minúsculas para evitar errores (ej: `.JPG`).
- **`.endswith()`**: Filtra por extensiones de imagen.


##  Modularización del Código

La función `organizar_imagenes()` fue creada para separar la lógica principal del script y así facilitar su 
reutilización. Ahora bien  la idea de modularizar el código es volver esta función reutilizable. 
Puedes usar esta función en otros proyectos Python sin depender del archivo principal.

###  Ventajas de modularizar:
- Reutilizable: Bueno amis puedes importar la función desde otros scripts sin copiar todo el código.
- Essssssss musho + limpio y mantenible: El código está organizado por responsabilidades.
- Facilita pruebas unitarias: Puedes probar la función directamente sin ejecutar el programa completo jejej.

### YES YES YES!!! Cómo usarlo desde otro script:
```python
from organizar_fotos import organizar_imagenes

resultado = organizar_imagenes("ruta/a/imagenes")
print(resultado)

pablo te amo
este script funciona para fotos del lab

## 📄 Licencia
MIT © [noomesk](https://github.com/angie-plazas)"# Prueba" 
