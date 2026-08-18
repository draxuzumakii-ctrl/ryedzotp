#!/usr/bin/env python3
# main.py - SPAM MACHINE

import sys
import os
from datetime import datetime
from colorama import Fore, Style, init

# Initialize
init(autoreset=True)

# Import
from config import *
from database import *
from engine import main as engine_main

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def banner():
    print(f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗
║                    {Fore.YELLOW}SPAM MACHINE v{VERSION}{Fore.CYAN}                       ║
║                    {Fore.WHITE}Multi-Fitur Spammer{Fore.CYAN}                          ║
╠══════════════════════════════════════════════════════════════╣
║  {Fore.GREEN}Author  {Fore.CYAN}: {Fore.WHITE}{AUTHOR:<30}{Fore.CYAN}              ║
║  {Fore.GREEN}Telegram{Fore.CYAN}: {Fore.WHITE}{get_telegram_admin():<30}{Fore.CYAN}              ║
║  {Fore.GREEN}WhatsApp{Fore.CYAN}: {Fore.WHITE}{get_whatsapp_admin():<30}{Fore.CYAN}              ║
╚══════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}""")

def get_formatted_datetime():
    now = datetime.now()
    days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    months = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
              "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    return f"{days[now.weekday()]}, {now.day} {months[now.month-1]} {now.year}"

def show_stats():
    premium, trial = get_user_stats()
    total = premium + trial
    print(f"{Fore.CYAN}Total Pengguna : {Fore.WHITE}{total}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}├─ Premium     : {Fore.GREEN}{premium}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}└─ Trial       : {Fore.YELLOW}{trial}{Style.RESET_ALL}")

def show_buy_guide(device_id):
    clear_screen()
    banner()
    print(f"\n{Fore.CYAN}PANDUAN PEMBELIAN LISENSI PREMIUM{Style.RESET_ALL}\n")
    print(f"{Fore.WHITE}Keuntungan Premium:{Style.RESET_ALL}")
    print(f"  {Fore.GREEN}•{Style.RESET_ALL} Akses FULL semua fitur")
    print(f"  {Fore.GREEN}•{Style.RESET_ALL} Unlimited penggunaan")
    print(f"  {Fore.GREEN}•{Style.RESET_ALL} Update tools terbaru")
    print(f"  {Fore.GREEN}•{Style.RESET_ALL} Dukungan prioritas\n")
    print(f"{Fore.CYAN}Harga: {Fore.GREEN}Rp. {get_license_price():,}{Style.RESET_ALL}\n")
    print(f"{Fore.YELLOW}Cara Pembelian:{Style.RESET_ALL}")
    print(f"  1. Chat admin via WhatsApp/Telegram")
    print(f"  2. Kirim Device ID Anda")
    print(f"  3. Bayar via QRIS")
    print(f"  4. Tunggu aktivasi\n")
    print(f"{Fore.CYAN}Kontak Admin:{Style.RESET_ALL}")
    print(f"  WhatsApp: {Fore.GREEN}{get_whatsapp_admin()}{Style.RESET_ALL}")
    print(f"  Telegram: {Fore.WHITE}{get_telegram_admin()}{Style.RESET_ALL}\n")
    print(f"{Fore.CYAN}Device ID Anda:{Style.RESET_ALL}")
    print(f"  {Fore.WHITE}{device_id}{Style.RESET_ALL}\n")
    input(f"{Fore.CYAN}Tekan Enter untuk kembali...{Style.RESET_ALL}")

def main():
    device_id = get_device_id()
    user = check_user(device_id)
    
    if not user:
        user = create_user(device_id)
        print(f"{Fore.GREEN}[+] User baru dibuat dengan kuota trial {user['quota']}x{Style.RESET_ALL}")
    
    while True:
        clear_screen()
        banner()
        print(f"{Fore.CYAN}{get_formatted_datetime()}{Style.RESET_ALL}\n")
        show_stats()
        print()
        
        if user["status"] == "trial":
            print(f"{Fore.YELLOW}Mode: TRIAL (Sisa kuota: {user['quota']}/{get_trial_quota()}){Style.RESET_ALL}")
            print(f"{Fore.CYAN}[1]{Style.RESET_ALL} Jalankan Spam Machine")
            print(f"{Fore.CYAN}[2]{Style.RESET_ALL} Beli Premium")
            print(f"{Fore.CYAN}[0]{Style.RESET_ALL} Keluar")
        else:
            print(f"{Fore.GREEN}Mode: PREMIUM (Unlimited){Style.RESET_ALL}")
            print(f"{Fore.CYAN}[1]{Style.RESET_ALL} Jalankan Spam Machine")
            print(f"{Fore.CYAN}[0]{Style.RESET_ALL} Keluar")
        
        pilihan = input(f"\n{Fore.YELLOW}[?] Pilih menu: {Style.RESET_ALL}").strip()
        
        if pilihan == "0":
            print(f"\n{Fore.RED}[+] Keluar...{Style.RESET_ALL}")
            sys.exit(0)
        
        elif pilihan == "1":
            if user["status"] == "trial":
                if user["quota"] <= 0:
                    print(f"\n{Fore.RED}[!] Kuota habis!{Style.RESET_ALL}")
                    input(f"{Fore.CYAN}Tekan Enter untuk melihat panduan pembelian...{Style.RESET_ALL}")
                    show_buy_guide(device_id)
                    user = check_user(device_id)
                    continue
                
                engine_main()
                use_quota(device_id)
                user = check_user(device_id)
            else:
                engine_main()
        
        elif pilihan == "2" and user["status"] == "trial":
            show_buy_guide(device_id)
            user = check_user(device_id)
        
        else:
            print(f"\n{Fore.RED}[!] Pilihan tidak valid!{Style.RESET_ALL}")
            input(f"{Fore.CYAN}Tekan Enter...{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
