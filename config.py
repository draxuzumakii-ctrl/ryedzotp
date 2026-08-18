#!/usr/bin/env python3
# config.py - Konfigurasi & Enkripsi

import os
import platform
import hashlib
import base64
import json
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# ========== KONFIGURASI DASAR ==========
VERSION = "2.0.0"
TOOLS_NAME = "SPAM MACHINE"
AUTHOR = "Your Name"

# ========== ENKRIPSI ==========
SECRET_KEY = "spam_machine_secret_key_2024"

def get_fernet_key():
    """Generate Fernet key dari secret"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=b"spam_machine_salt",
        iterations=100000
    )
    key = base64.urlsafe_b64encode(kdf.derive(SECRET_KEY.encode()))
    return key

def encrypt_data(data):
    """Enkripsi data"""
    try:
        fernet = Fernet(get_fernet_key())
        if isinstance(data, dict):
            data = json.dumps(data)
        if isinstance(data, str):
            data = data.encode()
        encrypted = fernet.encrypt(data)
        return base64.b64encode(encrypted).decode()
    except:
        return data

def decrypt_data(encrypted):
    """Dekripsi data"""
    try:
        fernet = Fernet(get_fernet_key())
        encrypted = base64.b64decode(encrypted)
        decrypted = fernet.decrypt(encrypted)
        return decrypted.decode()
    except:
        return encrypted

# ========== DATA TERENKRIPSI ==========
_ENCRYPTED = {
    "license_price": encrypt_data("150000"),
    "whatsapp_admin": encrypt_data("6281234567890"),
    "telegram_admin": encrypt_data("@admin_spam"),
    "trial_quota": encrypt_data("3"),
    "version": encrypt_data(VERSION)
}

def get_config(key):
    """Ambil config terenkripsi"""
    if key in _ENCRYPTED:
        return decrypt_data(_ENCRYPTED[key])
    return None

# ========== DEVICE ID ==========
def get_device_id():
    """Generate Device ID unik"""
    try:
        if platform.system() == "Linux":
            with open("/etc/machine-id", "r") as f:
                machine_id = f.read().strip()
        elif platform.system() == "Windows":
            import subprocess
            result = subprocess.run(["wmic", "csproduct", "get", "uuid"],
                                   capture_output=True, text=True)
            machine_id = result.stdout.strip().split("\n")[-1].strip()
        else:
            machine_id = platform.node()
        
        hash_id = hashlib.sha256(machine_id.encode()).hexdigest()[:32]
        return encrypt_data(hash_id)
    except:
        import random
        random_id = str(random.random())
        hash_id = hashlib.sha256(random_id.encode()).hexdigest()[:32]
        return encrypt_data(hash_id)

# ========== FUNGSI LAIN ==========
def get_active_apis():
    return 25

def get_total_apis():
    return 30

def is_maintenance():
    return False

def get_maintenance_message():
    return ""

def get_user_stats():
    try:
        from database import load_db
        db = load_db()
        total = len(db["users"])
        premium = sum(1 for u in db["users"].values() if u["status"] == "premium")
        return premium, total - premium
    except:
        return 0, 0

def get_trial_quota():
    return int(get_config("trial_quota"))

def get_license_price():
    return int(get_config("license_price"))

def get_whatsapp_admin():
    return get_config("whatsapp_admin")

def get_telegram_admin():
    return get_config("telegram_admin")
