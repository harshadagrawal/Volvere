import psutil
import speedtest
import platform
import socket
from screeninfo import get_monitors

def get_installed_software():
    software_list = [p.info['name'] for p in psutil.process_iter(['pid', 'name']) if 'name' in p.info]
    return software_list

def get_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000
    upload_speed = st.upload() / 1_000_000 
    return download_speed, upload_speed

def get_system_resolution():
    monitors = get_monitors()
    resolution = [(monitor.width, monitor.height) for monitor in monitors]
    return resolution

def get_cpu_info():
    cpu_info = platform.processor()
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)
    return cpu_info, cpu_cores, cpu_threads

def get_gpu_info():
    try:
        import GPUtil
        gpu_info = GPUtil.getGPUs()[0].name
    except ImportError:
        gpu_info = "Not available"
    return gpu_info

def get_ram_size():
    ram_size = psutil.virtual_memory().total / (1024 ** 3)
    return ram_size

def get_screen_size():
    resolution = get_system_resolution()
    diagonal_size = (resolution[0][0]**2 + resolution[0][1]**2)**0.5
    screen_size = round(diagonal_size / 141, 1)  # Convert to inches
    return screen_size

def get_mac_address():
    mac_address = ':'.join(['{:02x}'.format(int(byte, 16)) for byte in psutil.net_if_addrs()['Ethernet'][0].address.split('-')])
    return mac_address

def get_public_ip():
    public_ip = socket.gethostbyname(socket.gethostname())
    return public_ip

def get_windows_version():
    windows_version = platform.version()
    return windows_version

if __name__ == "__main__":
    installed_software = get_installed_software()
    internet_speed = get_internet_speed()
    resolution = get_system_resolution()
    cpu_info, cpu_cores, cpu_threads = get_cpu_info()
    gpu_info = get_gpu_info()
    ram_size = get_ram_size()
    screen_size = get_screen_size()
    mac_address = get_mac_address()
    public_ip = get_public_ip()
    windows_version = get_windows_version()

    print("Installed Software:", installed_software)
    print("Internet Speed (Mbps):", "Download:", internet_speed[0], "Upload:", internet_speed[1])
    print("Screen Resolution:", resolution)
    print("CPU Model:", cpu_info)
    print("Number of CPU Cores:", cpu_cores)
    print("Number of CPU Threads:", cpu_threads)
    print("GPU Model:", gpu_info)
    print("RAM Size (GB):", round(ram_size, 2))
    print("Screen Size (inches):", screen_size)
    print("MAC Address:", mac_address)
    print("Public IP Address:", public_ip)
    print("Windows Version:", windows_version)
