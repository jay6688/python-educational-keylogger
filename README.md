# Python Educational Keylogger ⌨️

A foundational Python script built to demonstrate how hardware input interception and operating system hooking work. This tool captures keystrokes, formats them into human-readable text (handling special keys like Space, Enter, and Shift), and logs them to a local file.

## ⚠️ Educational Disclaimer
**This project is strictly for educational purposes and authorized auditing.** It was built to understand the underlying mechanics of keystroke logging and hardware hooking in order to better defend against malware and spyware. Never deploy this script on a system you do not own or do not have explicit permission to monitor.

## ✨ Features
* **Hardware Interception**: Uses the `pynput` library to hook into the OS and listen for physical keyboard events.
* **Clean Formatting**: Translates raw hardware signals (e.g., `Key.space`, `Key.enter`) into readable strings and line breaks, avoiding messy, vertical raw data logs.
* **Background Logging**: Quietly appends intercepted keystrokes to a local `clean_log.txt` file in real-time.
* **Kill Switch**: Includes an embedded kill switch (the `ESC` key) to safely detach the hook and terminate the script.

## ⚙️ Prerequisites
* Python 3.x
* `pynput` library (`pip install pynput`)

## 🧠 What I Learned
* **OS-Level Hooking**: Understanding how background processes can intercept hardware interrupts before they reach the active application.
* **File I/O Operations**: Managing continuous file appending (`"a"` mode) without locking the file or crashing the script.
* **Exception Handling**: Using `try/except` blocks to differentiate between standard character inputs and complex system keys.
