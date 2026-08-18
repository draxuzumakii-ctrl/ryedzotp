#!/usr/bin/env python3
# endpoints.py - Kumpulan Endpoint API

import random
from config import encrypt_data

# ========== USER AGENTS ==========
USER_AGENTS = [
    "Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; RMX2020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A505F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36",
]

# ========== ENDPOINT WHATSAPP ==========
WA_ENDPOINTS = [
    {
        "name": "WA Register",
        "url": "https://v.whatsapp.com/v2/register",
        "params": lambda phone: {
            "cc": "62", "in": phone, "rc": "0",
            "lg": "en", "lc": "ID", "mistyped": "false"
        }
    },
    {
        "name": "WA Exist",
        "url": "https://v.whatsapp.com/v2/exist",
        "params": lambda phone: {
            "cc": "62", "in": phone, "lg": "en", "lc": "ID"
        }
    }
]

# ========== ENDPOINT OTP ==========
OTP_ENDPOINTS = [
    {
        "name": "Shopee",
        "url": "https://mall.shopee.co.id/api/v4/account/otp",
        "params": lambda phone: {"phone": phone, "channel": "sms", "operation": "register"}
    },
    {
        "name": "Gojek",
        "url": "https://api.gojekapi.com/v3/customers/login_with_phone",
        "params": lambda phone: {"phone": phone, "country_code": "+62"}
    },
    {
        "name": "OVO",
        "url": "https://api.ovo.id/v1.1/api/auth/customer/login2FA",
        "params": lambda phone: {"mobile": phone, "deviceId": f"device_{random.randint(10000000,99999999)}"}
    },
    {
        "name": "DANA",
        "url": "https://api.dana.id/dana/v1/otp/send",
        "params": lambda phone: {"phone": phone, "type": "register"}
    },
    {
        "name": "Tokopedia",
        "url": "https://www.tokopedia.com/api/v1/otp/request",
        "params": lambda phone: {"phone": phone, "type": "register"}
    }
]

# ========== ENDPOINT SMS ==========
SMS_ENDPOINTS = [
    {
        "name": "TextBelt",
        "url": "https://textbelt.com/text",
        "params": lambda phone, msg: {"phone": phone, "message": msg, "key": "textbelt"}
    },
    {
        "name": "SMS Gateway",
        "url": "https://api.sms-gateway.app/send",
        "params": lambda phone, msg: {"phone": phone, "message": msg}
    }
]

# ========== ENDPOINT NGL ==========
NGL_URL = "https://ngl.link/api/submit"

# ========== ENDPOINT CALL ==========
CALL_ENDPOINTS = [
    {
        "name": "Call Flood 1",
        "url": "https://api.callflood.com/send",
        "params": lambda phone: {"phone": phone, "type": "call"}
    }
]

# ========== ENDPOINT EMAIL ==========
EMAIL_ENDPOINTS = [
    {
        "name": "Email Flood 1",
        "url": "https://api.emailflood.com/send",
        "params": lambda email, msg: {"email": email, "message": msg}
    }
]

def get_random_ua():
    return random.choice(USER_AGENTS)

def normalize_phone(phone):
    """Normalisasi nomor telepon"""
    phone = phone.strip().replace(" ", "").replace("-", "")
    if phone.startswith("0"):
        return "62" + phone[1:]
    elif phone.startswith("8"):
        return "62" + phone
    elif phone.startswith("+62"):
        return phone[1:]
    return phone
