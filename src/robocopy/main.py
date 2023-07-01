import os

def copy(src,dst):
    command = f'robocopy {src} {dst} /E'
    os.system(command)
    print(f"Copied files from {src} to {dst}")

