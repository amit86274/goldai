import subprocess

def run_tests():
    return subprocess.run(['python','-m','pytest'], capture_output=True, text=True)
