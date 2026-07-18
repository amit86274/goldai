
import platform
def runtime_info():
    return {
        "python": platform.python_version(),
        "platform": platform.system()
    }
