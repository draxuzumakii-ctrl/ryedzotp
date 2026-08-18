#!/usr/bin/env python3
# modules/spam_ngl.py

import requests
import concurrent.futures
import time
import random
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from endpoints import NGL_URL, get_random_ua

def spam_ngl(username, jumlah, pesan, threads=10):
    """Spam NGL ke username target"""
    sukses = 0
    gagal = 0
    
    print(f"\n[+] Spam NGL ke @{username}")
    print(f"[+] Pesan: {pesan}")
    print(f"[+] Jumlah: {jumlah} | Threads: {threads}\n")
    
    requests.packages.urllib3.disable_warnings()
    
    def kirim(i):
        try:
            ua = get_random_ua()
            data = {
                "username": username,
                "question": pesan,
                "deviceId": f"device_{random.randint(10000000,99999999)}",
                "gameSlug": "",
                "referrer": ""
            }
            resp = requests.post(
                NGL_URL,
                json=data,
                headers={"User-Agent": ua, "Content-Type": "application/json"},
                timeout=10
            )
            return i, resp.status_code
        except:
            return i, "ERROR"
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        for i in range(jumlah):
            futures.append(executor.submit(kirim, i+1))
        
        for future in concurrent.futures.as_completed(futures):
            i, status = future.result()
            if status in [200, 201, 202]:
                sukses += 1
                print(f"[✓] NGL #{i}: {status}")
            else:
                gagal += 1
                print(f"[✗] NGL #{i}: {status}")
    
    print(f"\n[+] Selesai. Sukses: {sukses} | Gagal: {gagal}")
    return sukses > 0
