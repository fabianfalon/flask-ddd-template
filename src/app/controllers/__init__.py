import importlib
import glob

from src.app.injections.containers import Containers

container = Containers()

# Ruta al directorio que contiene los módulos
modules_directory = "src/app/controllers/"

# Obtener la lista de todos los archivos Python en el directorio
module_files = glob.glob(f"{modules_directory}/**/*.py", recursive=True)

# Importar cada módulo encontrado dinámicamente
for module_file in module_files:
    # Obtener la ruta relativa del módulo (reemplazar barras con puntos para importar)
    module_path = module_file.replace("/", ".").replace("\\", ".")[:-3]

    # Importar el módulo dinámicamente
    module = importlib.import_module(module_path)

    # Incluir el módulo en la configuración del contenedor
    container.wire(modules=[module])
