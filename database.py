#!/usr/bin/env python3
# database.py - Database Pengguna Terenkripsi

import json
import os
from datetime import datetime
from config import encrypt_data, decrypt_data

DB_FILE = "users.enc"

def load_db():
    """Load database"""
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            encrypted = f.read()
            try:
                decrypted = decrypt_data(encrypted)
                return json.loads(decrypted)
            except:
                return {"users": {}}
    return {"users": {}}

def save_db(db):
    """Simpan database"""
    json_str = json.dumps(db)
    encrypted = encrypt_data(json_str)
    with open(DB_FILE, "w") as f:
        f.write(encrypted)

def check_user(device_id):
    """Cek user"""
    db = load_db()
    return db["users"].get(device_id)

def create_user(device_id):
    """Buat user baru"""
    db = load_db()
    if device_id not in db["users"]:
        db["users"][device_id] = {
            "device_id": device_id,
            "status": "trial",
            "quota": 3,
            "created_at": datetime.now().isoformat(),
            "expired_at": None,
            "total_spam": 0,
            "last_used": None
        }
        save_db(db)
    return db["users"][device_id]

def update_user(device_id, updates):
    """Update user"""
    db = load_db()
    if device_id in db["users"]:
        db["users"][device_id].update(updates)
        save_db(db)
        return db["users"][device_id]
    return None

def use_quota(device_id):
    """Kurangi kuota"""
    user = check_user(device_id)
    if not user:
        return False
    
    if user["status"] == "trial" and user["quota"] > 0:
        user["quota"] -= 1
        user["total_spam"] += 1
        user["last_used"] = datetime.now().isoformat()
        update_user(device_id, user)
        return True
    elif user["status"] == "premium":
        user["total_spam"] += 1
        user["last_used"] = datetime.now().isoformat()
        update_user(device_id, user)
        return True
    return False

def activate_premium(device_id):
    """Aktivasi premium"""
    return update_user(device_id, {
        "status": "premium",
        "expired_at": None
    })

def reset_quota(device_id):
    """Reset kuota trial"""
    return update_user(device_id, {"quota": 3})
