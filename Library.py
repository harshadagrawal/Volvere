import subprocess
import sys

def install_modules(module_names):
    for module_name in module_names:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
            print(f"Successfully installed {module_name}")
        except subprocess.CalledProcessError:
            print(f"Failed to install {module_name}")

# Example: Install multiple modules
modules_to_install = [ "psutil","speedtest-cli","platform","socket","screeninfo"]
install_modules(modules_to_install)