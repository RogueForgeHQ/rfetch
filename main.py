from src.system import get_os_name, get_kernel, is_steam_installed, is_gamemode_installed, get_cpu_name, get_ram_size, get_gpu_name, get_disk_usage, get_uptime, get_desktop_environment

def print_banner():
    print("============================")
    print("      Rogue Forge")
    print("        rfetch")
    print("============================")
    print()


def main():
    print_banner()

    print(f"OS        : {get_os_name()}")
    print(f"Kernel    : {get_kernel()}")
    print(f"CPU       : {get_cpu_name()}")
    print(f"RAM       : {get_ram_size()}")
    print(f"GPU       : {get_gpu_name()}")
    total, used, free = get_disk_usage()
    print(f"Disk      : {used} GB / {total} GB ({free} GB free)")
    steam = "Installed ✅" if is_steam_installed() else "Not Installed ❌"

    print(f"Steam     : {steam}")
    hours, mins = get_uptime()
    print(f"UpTime    : {hours}h {mins}m")
    print(f"Desktop   : {get_desktop_environment()}")
    gamemode = "Installed ✅" if is_gamemode_installed() else "Not Installed ❌"

    print(f"GameMode  : {gamemode}")

if __name__ == "__main__":
    main()
