#!/usr/bin/env python3
# modules/spam_sms.py

import requests
import concurrent.futures
import time
import random
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from endpoints import SMS_ENDPOINTS, get_random_ua, normalize_phone

def spam_sms(phone, jumlah, pesan, threads=10):
    """Spam SMS ke nomor target"""
    phone = normalize_phone(phone)
    sukses = 0
    gagal = 0
    
    print(f"\n[+] Spam SMS ke {phone}")
    print(f"[+] Pesan: {pesan}")
    print(f"[+] Jumlah: {jumlah} | Threads: {threads}\n")
    
    requests.packages.urllib3.disable_warnings()
    
    def kirim(api):
        try:
            resp = requests.post(
                api["url"],
                data=api["params"](phone, pesan),
                timeout=15,
                verify=False
            )
            return api["name"], resp.status_code
        except:
            return api["name"], "ERROR"
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        for i in range(jumlah):
            api = random.choice(SMS_ENDPOINTS)
            futures.append(executor.submit(kirim, api))
            time.sleep(0.1)
        
        for future in concurrent.futures.as_completed(futures):
            name, status = future.result()
            if status in [200, 201, 202]:
                sukses += 1
                print(f"[✓] {name}: {status}")
            else:
                gagal += 1
                print(f"[✗] {name}: {status}")
    
    print(f"\n[+] Selesai. Sukses: {sukses} | Gagal: {gagal}")
    return sukses > 0
