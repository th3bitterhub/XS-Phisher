<div align="center">

```
 __  _____     ___ _    _    _            
 \ \/ / __|___| _ \ |_ (_)__| |_  ___ _ _ 
  >  <\__ \___|  _/ ' \| (_-< ' \/ -_) '_|
 /_/\_\___/   |_| |_||_|_/__/_||_\___|_|  
```

**A Modern Automated Web-Phishing Tool For Red Teaming**

![Version](https://img.shields.io/badge/version-0.9v-purple)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20Termux-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

</div>

---

> ⚠️ **Disclaimer:** XS-Phisher is intended **strictly for educational purposes, authorized red team operations, and security awareness training**. Do not use this tool against any system or individual without explicit written permission. Misuse of this tool is illegal and unethical. The authors are not responsible for any damage or legal consequences arising from misuse.

---

## 📖 About

XS-Phisher is an automated web phishing simulation builder designed for red team operations, security testing, and awareness training scenarios.

Create, customize, and generate realistic credential harvesting pages through a guided workflow — without manual setup or repetitive configuration. Built for controlled environments to evaluate human-factor security posture and phishing resilience.

**Modular. Automated. Red-Team Ready.**

---

## ✨ Features

- 20+ pre-built phishing page templates (Facebook, Instagram, Google, Discord, and more)
- Custom template cloner — clone any website by URL
- Discord webhook integration for credential capture
- Tunnel support via **Cloudflared** and **LocalXpose**
- Localhost mode for internal network testing
- Termux (Android) support
- Simple settings menu with webhook management

---

## 🖥️ Supported Templates

| # | Site | # | Site |
|---|------|---|------|
| 01 | Facebook | 11 | Twitch |
| 02 | Instagram | 12 | Snapchat |
| 03 | Netflix | 13 | Reddit |
| 04 | Google | 14 | Roblox |
| 05 | Microsoft | 15 | Xbox |
| 06 | Paypal | 16 | Playstation |
| 07 | Twitter | 17 | LandBank |
| 08 | TikTok | 18 | Spotify |
| 09 | Discord | 19 | GitHub |
| 10 | MediaFire | 20 | DropBox |
| 99 | Custom Template | — | — |

---

## 📋 Requirements

- Python 3.8+
- PHP
- Apache2
- curl

---

## ⚙️ Installation

**Clone the repository:**
```bash
git clone https://github.com/yourusername/xs-phisher.git
cd xs-phisher
```

**Install Python dependencies:**
```bash
pip install -r requirements.txt
```

**On Termux (Android):**
```bash
pkg install python php apache2 curl
pip install -r requirements.txt
```

> Dependencies like PHP and Apache2 can also be auto-installed from the tool's setup on first run.

---

## 🚀 Usage

```bash
python main.py
```

### Main Menu

```
(1) Start Building   — Choose a phishing template and launch
(2) About            — Info about the tool
(3) Settings         — Configure webhooks and preferences
(4) Exit
```

### Tunnel Options

When starting a phishing session, you'll be prompted to choose a tunnel method:

```
[01] Localhost        — LAN/local network only
[02] Cloudflared      — Public URL, auto-detects tunnel
[03] LocalXpose       — Public URL, max 15 minutes (free tier)
```

### Discord Webhook Setup

1. Go to **Settings → Add Discord Webhook**
2. Paste your Discord webhook URL
3. Enable webhooks via **Settings → Use Webhook → yes**

Captured credentials will be sent directly to your Discord channel.

---

## 📁 Project Structure

```
xs-phisher/
├── main.py              # Main entry point
├── settings.json        # Auto-generated config file
├── .server/             # Server binaries (cloudflared, loclx)
│   └── www/             # Active served site
├── .websites/           # Built-in phishing templates
└── .custom-sites/       # Cloned custom templates
```

---

## 👥 Authors
- **bithub**
- **ac1x**
- **bsux**

---

## ⭐ Support

If you find this project useful, consider leaving a star on the repo!
