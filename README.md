# TeleLog

![ezgif-754de35099187](https://github.com/user-attachments/assets/3f162470-1fc4-4681-900e-d180d4b7e4f4)



![ezgif-76b73f93d96da](https://github.com/user-attachments/assets/c74e2073-4b0a-4cb2-9480-47ae019a9aec)



## Keylogger Auto-Generator Auto-Obfuscation and Auto-Compilation.

This repository contains a Python-based tool that generates an obfuscated keylogger script and compiles it into an executable file. The tool is designed to work in two steps:

1. **First Script (`first.py`)**: Generates an obfuscated keylogger script (`rto.py`) after taking user input for the Telegram Bot API key and Chat ID.
2. **Second Script (`second.py`)**: Fixes the script structure, re-obfuscates it, and compiles it into an executable file (`rtc.exe`).

The final executable is placed in a folder called `minified\dist`.

---

## Table of Contents

1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Usage](#usage)
   - [Step 1: Run `first.py`](#step-1-run-firstpy)
   - [Step 2: Run `second.py`](#step-2-run-secondpy)
4. [Folder Structure](#folder-structure)
5. [Important Notes](#important-notes)
6. [Disclaimer](#disclaimer)

---

## Requirements

Before running the scripts, ensure you have the following installed:

- Python 3.8 or higher
- Pip (Python package manager)
- Modules: pyinstaller, pyminifier,requests,cryptography,keyboard 

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. **Install Dependencies**:
   Run the following command to install the required Python modules:
   ```bash
   pip install -r requirements.txt
   ```

   This will install all the necessary libraries, including `cryptography`, `keyboard`, `requests`, and `pyminifier`.

---

## Usage

### Step 1: Run `first.py`

1. **Execute the Script**:
   Run the `first.py` script to generate the obfuscated keylogger script:
   ```bash
   python first.py
   ```

2. **Provide Input**:
   - When prompted, enter your **Telegram Bot API Key**.
   - Next, enter your **Chat ID**.

3. **Output**:
   - The script will generate a `secret.key` file (used for encryption).
   - It will also create an obfuscated script (`rto.py`) in the current directory.
   - Finally, it will create a folder called `minified` and move the obfuscated script (`rto.py`) into it.

---

### Step 2: Run `second.py`

1. **Navigate to the `minified` Folder**:
   ```bash
   cd minified
   ```

2. **Execute the Script**:
   Run the `second.py` script to fix the script structure and compile it into an executable:
   ```bash
   python second.py
   ```

3. **Output**:
   - The script will extract the obfuscated code, re-obfuscate it, and generate a new script (`rtc.py`).
   - It will then compile `rtc.py` into an executable (`rtc.exe`) using `pyinstaller`.
   - The executable will be placed in the `dist` folder inside the `minified` directory.

---

## Folder Structure

After running both scripts, your folder structure will look like this:

```
TeleLog/
├── first.py
├── requirements.txt
├── secret.key
├── minified/
│   ├── rto.py
│   ├── second.py
│   ├── extractedtext.txt
│   ├── rtc.py
│   └── dist/
│       └── rtc.exe
```

---

## Important Notes

- **Telegram Bot API Key and Chat ID**: You need a valid Telegram Bot API key and Chat ID to receive logs. You can create a bot using [BotFather](https://core.telegram.org/bots#botfather) and get your Chat ID using tools like [@userinfobot](https://t.me/userinfobot).
- **Obfuscation**: The scripts use `pyminifier` for obfuscation. Ensure you have installed it via `requirements.txt`.
- **Anti-Debugging and Environment Checks**: The script includes anti-debugging and environment checks to detect debuggers, virtual machines, or sandboxes.
- **Compilation**: The `second.py` script uses `pyinstaller` to compile the script into an executable. Ensure `pyinstaller` is installed.

---

## Disclaimer

This tool is intended for **educational purposes only**. The authors do not condone or support the use of this tool for any malicious or illegal activities. Always ensure you have proper authorization before using this tool on any system.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For any issues or questions, please open an issue on the GitHub repository.
 
