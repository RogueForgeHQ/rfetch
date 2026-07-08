import platform
import shutil

def get_os_name():
    with open("/etc/os-release", "r") as file:
        for line in file:
            if line.startswith("PRETTY_NAME="):
                return line.split("=", 1)[1].strip().strip('"')

    return "Unknown Linux"


def get_kernel():
    return platform.release()

def is_steam_installed():
    return shutil.which("steam") is not None
