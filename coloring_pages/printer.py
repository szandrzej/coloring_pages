import subprocess

def print_file(file_path, printer_name=None):
    try:
        if printer_name:
            subprocess.run(["lp", file_path], check=True)
        else:
            subprocess.run(["lp", file_path], check=True)
        print(f"Sent {file_path} to the printer.")
    except subprocess.CalledProcessError as e:
        print(f"Printing failed: {e}")
