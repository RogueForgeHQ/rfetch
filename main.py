from src.system import get_os_name, get_kernel, is_program_installed, get_cpu_name, get_ram_size, get_gpu_name, get_disk_usage, get_uptime, get_desktop_environment, get_display_server, get_shell, get_architecture, get_host

def print_banner():
    print("============================")
    print("      Rogue Forge")
    print("        rfetch")
    print("============================")
    print()


def main():
    print_banner()

    print(f"{"OS":<13}: {get_os_name()}")
    print(f"{"Kernel":<13}: {get_kernel()}")
    print(f"{'Host':<13}: {get_host()}")
    print(f"{"Architecture":<13}: {get_architecture()}")
    hours, mins = get_uptime()
    print(f"{"UpTime":<13}: {hours}h {mins}m")

    print()

    print(f"{"CPU":<13}: {get_cpu_name()}")
    print(f"{"GPU":<13}: {get_gpu_name()}")
    print(f"{"RAM":<13}: {get_ram_size()}")
    total, used, free = get_disk_usage()
    print(f"{"Disk":<13}: {used} GB / {total} GB ({free} GB free)")

    print()

    print(f"{"Desktop":<13}: {get_desktop_environment()}")
    print(f"{"Display":<13}: {get_display_server()}")
    print(f"{"Shell":<13}: {get_shell()}")

    print()
    
    steam = "Installed ✅" if is_program_installed("steam") else "Not Installed ❌"
    print(f"{"Steam":<13}: {steam}")

    gamemode = "Installed ✅" if is_program_installed("gamemode") else "Not Installed ❌"
    print(f"{"GameMode":<13}: {gamemode}")

    wine = "Installed ✅" if is_program_installed("wine") else "Not Installed ❌"
    print(f"{'Wine':<13}: {wine}")

    heroic = "Installed ✅" if is_program_installed("heroic") else "Not Installed ❌"
    print(f"{'Heroic':<13}: {heroic}")
   
    lutris = "Installed ✅" if is_program_installed("lutris") else "Not Installed ❌"
    print(f"{'Lutris':<13}: {lutris}")

    mangohud = "Installed ✅" if is_program_installed("mangohud") else "Not Installed ❌"
    print(f"{'Mangohud':<13}: {mangohud}")
    
    gamescope = "Installed ✅" if is_program_installed("gamescope") else "Not Installed ❌"
    print(f"{'Gamescope':<13}: {gamescope}")
    



if __name__ == "__main__":
    main()
