import os
import shutil
import tempfile

def limpiar_directorio(directorio):
    # Recorrer todos los archivos y directorios en el directorio especificado
    for root, dirs, files in os.walk(directorio, topdown=False):
        for name in files:
            file_path = os.path.join(root, name)
            try:
                # Eliminar el archivo
                os.remove(file_path)
                print(f"Archivo eliminado: {file_path}")
            except Exception as e:
                print(f"Error al eliminar el archivo {file_path}: {e}")

        for name in dirs:
            dir_path = os.path.join(root, name)
            try:
                # Eliminar el directorio
                shutil.rmtree(dir_path)
                print(f"Directorio eliminado: {dir_path}")
            except Exception as e:
                print(f"Error al eliminar el directorio {dir_path}: {e}")

def limpiar_archivos_temporales():
    # Obtener la ruta del directorio temporal principal
    temp_dir = tempfile.gettempdir()
    print(f"Directorio temporal principal: {temp_dir}")
    limpiar_directorio(temp_dir)

    # Obtener la ruta del directorio temporal secundario
    tmp_dir = os.getenv('TMP')
    if tmp_dir:
        print(f"Directorio temporal secundario: {tmp_dir}")
        limpiar_directorio(tmp_dir)

    # Obtener la ruta del directorio Prefetch
    prefetch_dir = os.path.join(os.getenv('WINDIR'), 'Prefetch')
    print(f"Directorio Prefetch: {prefetch_dir}")
    limpiar_directorio(prefetch_dir)
