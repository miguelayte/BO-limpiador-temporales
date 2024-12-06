import os
import subprocess
import sys

def build_executable():
    # Nombre del proyecto (mismo nombre que la carpeta raíz)
    project_name = "BO-limpiador-temporales"
    
    # Ruta al script principal
    main_script = os.path.join("limpiador_temporales", "main.py")
    
    # Directorio de salida
    output_dir = "dist"
    
    # Comando de PyInstaller
    pyinstaller_command = [
        "pyinstaller",
        "--onefile",           # Crear un único archivo ejecutable
        "--windowed",          # Sin consola (para aplicaciones con GUI)
        "--name", project_name,  # Nombre del ejecutable
        #"--icon", "icon.ico",  # Ícono opcional (crea uno o quita esta línea)
        main_script
    ]
    
    try:
        # Ejecutar PyInstaller
        result = subprocess.run(pyinstaller_command, capture_output=True, text=True)
        
        # Verificar si la compilación fue exitosa
        if result.returncode == 0:
            print(f"Compilación exitosa. Ejecutable creado en {output_dir}/{project_name}")
            print("Detalles de la compilación:")
            print(result.stdout)
        else:
            print("Error en la compilación:")
            print(result.stderr)
    
    except Exception as e:
        print(f"Ocurrió un error durante la compilación: {e}")

if __name__ == "__main__":
    build_executable()