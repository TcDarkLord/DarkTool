#!/usr/bin/env python3
# ============================================================
#  DarkTool v5.0 - Termux Pentest Araç Kurulum Aracı
#  Eğitim ve güvenlik araştırması amaçlıdır.
#  Yalnızca size ait veya yazılı izin aldığınız sistemlerde kullanın.
# ============================================================

import os
import sys
import json
import urllib.request
from time import sleep as timeout

current_dir = os.getcwd()
prefix = os.getenv("PREFIX") or ""
TMP = os.path.join(prefix, "tmp") if prefix else "/tmp"

DarkTool_banner = (
    "██████╗  █████╗ ██████╗ ██╗  ██╗████████╗ ██████╗  ██████╗ ██╗     \n"
    "██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝╚══██╔══╝██╔═══██╗██╔═══██╗██║     \n"
    "██║  ██║███████║██████╔╝█████╔╝    ██║   ██║   ██║██║   ██║██║     \n"
    "██║  ██║██╔══██║██╔══██╗██╔═██╗    ██║   ██║   ██║██║   ██║██║     \n"
    "██████╔╝██║  ██║██║  ██║██║  ██╗   ██║   ╚██████╔╝╚██████╔╝███████╗\n"
    "╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝"
)

main_menu = """
    ============================================
       DarkTool v5.0 - Termux Pentest Araçları
    ============================================
    [01] Bilgi Toplama
    [02] Zafiyet Analizi
    [03] Web Hacking
    [04] Veritabanı Değerlendirmesi
    [05] Parola Saldırıları
    [06] Kablosuz Ağ Saldırıları
    [07] Tersine Mühendislik
    [08] Sömürü Araçları
    [09] Dinleme ve Sahteleme
    [10] Raporlama Araçları
    [11] Adli Bilişim Araçları
    [12] Stres Testi
    [13] Linux Dağıtımı Kur
    [14] Termux Yardımcı Araçları
    [15] Shell Fonksiyonu [.bashrc]
    [16] CLI Oyunları
    [17] Zararlı Yazılım Analizi
    [18] Derleyici/Yorumlayıcı
    [19] Sosyal Mühendislik Araçları
    --------------------------------------------
    [98] TÜM ARAÇLARI KUR
    [99] DarkTool'u Güncelle
    [00] Çıkış
    ============================================
"""

backtomenu_banner = """
  [99] Ana menüye dön
  [00] DarkTool'tan çık
"""

legal_text = """
  [!] YASAL UYARI / SORUMLULUK REDDİ

  DarkTool YALNIZCA eğitim ve güvenlik araştırması amaçlıdır.
  Bu aracı yalnızca size ait veya yazılı izin aldığınız
  sistemlerde kullanın.

  Yetkisiz kullanım, bulunduğunuz ülkenin yasalarına göre
  SUÇ teşkil edebilir. Tüm sorumluluk kullanıcıya aittir.

  Geliştirici(ler) hiçbir zarar, veri kaybı veya hukuki
  yaptırımdan sorumlu tutulamaz.

  Bu aracı kullanarak bu koşulları kabul etmiş sayılırsınız.
"""

configBase = "[HOME] = ~"
configFile = os.path.join(current_dir, "DarkTool.conf")
cache_1 = os.path.join(TMP, "DarkTool_1")

def writeStatus(statusId):
    try:
        with open(cache_1, "w") as f:
            f.write(str(statusId))
    except Exception:
        pass

def readStatus():
    try:
        with open(cache_1, "r") as f:
            return f.read() == "1"
    except (IOError, OSError):
        return False

def checkConfigFile():
    if os.path.exists(configFile):
        if os.path.isdir(configFile):
            os.system(f"rm -rf {configFile}")
            open(configFile, "w").write(configBase)
    else:
        open(configFile, "w").write(configBase)

def loadConfigFile():
    checkConfigFile()
    home = "~"
    try:
        with open(configFile, "r") as f:
            for line in f.read().splitlines():
                if "=" in line and line.split("=")[0].strip() == "[HOME]":
                    home = line.split("=", 1)[1].strip()
                    break
    except Exception:
        home = "~"
    return home

homeDir = loadConfigFile()

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def backtomenu_option():
    if not readStatus():
        print(backtomenu_banner)
        try:
            secim = input("DarkTool > ")
        except (KeyboardInterrupt, EOFError):
            sys.exit()
        if secim == "99":
            restart_program()
        elif secim in ("0", "00"):
            sys.exit()
        else:
            print("\nHATA: Geçersiz Giriş")
            timeout(2)
            restart_program()

def banner():
    print(DarkTool_banner)

def shell(cmd):
    os.system(cmd)

def _sh(cmd):
    os.system(cmd)

def gh_latest_asset(repo, pattern):
    api = f"https://api.github.com/repos/{repo}/releases/latest"
    try:
        req = urllib.request.Request(api, headers={"User-Agent": "DarkTool"})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.load(r)
        for a in data.get("assets", []):
            if pattern.lower() in a["name"].lower():
                return a["browser_download_url"], a["name"]
    except Exception as e:
        print(f"    ! GitHub API hatası: {e}")
    return None, None

def install_release(repo, pattern, binname, findname=None):
    findname = findname or binname
    shell("pkg install -y curl unzip tar > /dev/null 2>&1")
    url, fname = gh_latest_asset(repo, pattern)
    if not url:
        print("    ! Sürüm bulunamadı (repo adını veya mimariyi kontrol edin).")
        return
    print(f"    * {fname} indiriliyor...")
    shell(f"curl -sL -o {TMP}/{fname} '{url}'")
    shell(f"rm -rf {TMP}/lzrel && mkdir -p {TMP}/lzrel")
    if fname.endswith(".zip"):
        shell(f"unzip -o -q {TMP}/{fname} -d {TMP}/lzrel")
    else:
        shell(f"tar -xzf {TMP}/{fname} -C {TMP}/lzrel")
    shell(f"find {TMP}/lzrel -type f -name '{findname}' -exec chmod +x {{}} \\; -exec mv -f {{}} {prefix}/bin/{binname} \\;")
    shell(f"rm -rf {TMP}/lzrel {TMP}/{fname}")
    if os.path.exists(f"{prefix}/bin/{binname}"):
        print(f"    * {binname} -> $PREFIX/bin/ kuruldu.")
    else:
        print(f"    ! {binname} kurulamadı; dosya adı kalıbını kontrol edin.")

def _run(name, apt=None, pip=None, clone=None, curl=None, mv=None,
         cmd=None, note=None, start=None, post=None, release=None):
    print(f"\n    [+] {name} kuruluyor...")
    if note:
        print(f"    ! Not: {note}")
    if apt:
        print(f"    * Paketler: {apt}")
        shell(f"pkg install -y {apt} > /dev/null 2>&1")
    if pip:
        print(f"    * pip: {pip}")
        shell(f"python -m pip install {pip} > /dev/null 2>&1")
    if release:
        repo, pattern, binname = release
        install_release(repo, pattern, binname)
    if clone:
        reponame = clone.rstrip("/").split("/")[-1]
        print(f"    * Klonlanıyor: {reponame}")
        shell(f"cd {homeDir} && git clone --depth 1 {clone} > /dev/null 2>&1")
        if not os.path.isdir(os.path.join(os.path.expanduser(homeDir), reponame)):
            print(f"    ! Klonlama başarısız oldu: {clone}")
    if curl:
        fname = curl.split("/")[-1].split("?")[0]
        print(f"    * İndiriliyor: {fname}")
        shell(f"curl -sL -O '{curl}'")
    if mv:
        shell(mv)
    if post:
        shell(post)
    if cmd:
        print("    * Ek kurulum adımları çalıştırılıyor...")
        shell(cmd)
    if start:
        print(f"    * Kullanım: {start}")
    print(f"    [✓] {name} tamamlandı.")
    timeout(1)

def parse_selection(text):
    secim = []
    for part in text.replace(",", " ").split():
        if "-" in part:
            try:
                a, b = part.split("-")
                if a.isdigit() and b.isdigit():
                    secim += [str(i) for i in range(int(a), int(b) + 1)]
                    continue
            except ValueError:
                pass
        secim.append(part)
    return secim

def update_DarkTool():
    print("\n    [+] DarkTool güncelleniyor...")
    shell(f"cd {current_dir} && git pull origin main 2>/dev/null || git pull origin master 2>/dev/null")
    print("    [✓] Güncelleme tamamlandı.")
    timeout(2)
    restart_program()

def first_run():
    flag = os.path.join(os.path.expanduser("~"), ".darktool_firstrun")
    if os.path.exists(flag):
        return
    os.system("clear")
    print(legal_text)
    input("\n[Enter] ile devam et...")
    os.system("clear")
    print("\n    [+] İlk kurulum yapılıyor (temel paketler)...\n")
    shell("pkg update -y > /dev/null 2>&1")
    shell("pkg install -y git python curl wget unzip tar > /dev/null 2>&1")
    open(flag, "w").close()
    print("    [✓] Temel paketler kuruldu.\n")
    timeout(2)

# ============================================================
#  BÖLÜM 2/3 - Araç Kurulum Fonksiyonları
# ============================================================

# -------- 01 Bilgi Toplama --------
def nmap():
    _run("Nmap", apt="nmap", start="nmap -sV <hedef>")

def sqlmap():
    _run("sqlmap", apt="python", pip="sqlmap", start="sqlmap -u <hedef-url> --batch")

def red_hawk():
    _run("RED HAWK", apt="git php", clone="https://github.com/Tuhinshubhra/RED_HAWK",
         start=f"cd {homeDir}/RED_HAWK && php red_hawk.php")

def theharvester():
    _run("theHarvester", apt="python", pip="theHarvester",
         start="theHarvester -d ornek.com -b all")

def sherlock():
    _run("Sherlock", apt="python", pip="sherlock-project", start="sherlock kullanici_adi")

def maigret():
    _run("Maigret", apt="python", pip="maigret", start="maigret kullanici_adi")

def userrecon():
    _run("UserRecon", apt="git", clone="https://github.com/thelinuxchoice/userrecon",
         start=f"cd {homeDir}/userrecon && bash userrecon.sh")

def phoneinfoga():
    _run("PhoneInfoga", release=("sundowndev/phoneinfoga", "linux_arm64.tar.gz", "phoneinfoga"),
         start="phoneinfoga scan -n +90XXXXXXXXXX")

def sublist3r():
    _run("Sublist3r", apt="git python", clone="https://github.com/aboul3la/Sublist3r",
         cmd=f"cd {homeDir}/Sublist3r && pip install -r requirements.txt",
         start=f"python3 {homeDir}/Sublist3r/sublist3r.py -d ornek.com")

def dnsrecon():
    _run("DNSRecon", apt="git python", clone="https://github.com/darkoperator/dnsrecon",
         post=f"python -m pip install -r {homeDir}/dnsrecon/requirements.txt",
         start=f"python {homeDir}/dnsrecon/dnsrecon.py -d ornek.com")

def fierce():
    _run("Fierce", apt="python", pip="fierce", start="fierce --domain ornek.com")

def dnsx():
    _run("dnsx", release=("projectdiscovery/dnsx", "linux_arm64.zip", "dnsx"),
         start="dnsx -d ornek.com")

def subfinder():
    _run("Subfinder", release=("projectdiscovery/subfinder", "linux_arm64.zip", "subfinder"),
         start="subfinder -d ornek.com")

def httpx():
    _run("httpx", release=("projectdiscovery/httpx", "linux_arm64.zip", "httpx"),
         start="httpx -l hedefler.txt")

def osintgram():
    _run("Osintgram", apt="git python", clone="https://github.com/Datalux/Osintgram",
         cmd=f"cd {homeDir}/Osintgram && pip install -r requirements.txt",
         start=f"cd {homeDir}/Osintgram && python3 main.py")

def h8mail():
    _run("h8mail", apt="python", pip="h8mail", start="h8mail -t hedef@mail.com")

# -------- 02 Zafiyet Analizi --------
def dsss():
    _run("DSSS (Damn Small SQLi Scanner)", apt="git python",
         clone="https://github.com/stamparm/DSSS",
         start=f"python3 {homeDir}/DSSS/dsss.py -u <hedef-url>")

def sqliv():
    _run("SQLiv", apt="git python", clone="https://github.com/the-robot/sqliv",
         note="Python 2 gerektirir; repo arşivlenmiş durumda.")

def sqlscan():
    _run("sqlscan", apt="git php", clone="https://github.com/Cvar1984/sqlscan",
         note="PHP gerektirir.", start=f"cd {homeDir}/sqlscan && php sqlscan.php")

def wordpreSScan():
    _run("Wordpresscan", apt="git python", clone="https://github.com/swisskyrepo/Wordpresscan",
         cmd=f"cd {homeDir}/Wordpresscan && pip install -r requirements.txt",
         note="Python 2 gerektirir; repo arşivlenmiş durumda.")

def wpscan():
    _run("WPScan", apt="ruby curl", cmd="gem install wpscan",
         note="Güncel resmi kurulum yolu: gem.",
         start="wpscan --url <site>")

def wordpresscan():
    _run("termux-wordpresscan", apt="git nmap figlet",
         clone="https://github.com/silverhat007/termux-wordpresscan",
         cmd=f"cd {homeDir}/termux-wordpresscan && chmod +x * && sh install.sh",
         start="wordpresscan")

def tmscanner():
    _run("TM-scanner", apt="git", clone="https://github.com/Gameye98/TM-scanner",
         note="URL doğrulanmadı; gerekiyorsa düzeltin.")

def rang3r():
    _run("Rang3r", apt="git python", clone="https://github.com/floriankunushevci/rang3r",
         note="Python 2 gerektirir; repo arşivlenmiş durumda.")

def routersploit():
    _run("Routersploit", apt="git python",
         clone="https://github.com/threat9/routersploit",
         cmd=f"cd {homeDir}/routersploit && pip install -r requirements.txt",
         note="Repo arşivlendi; python2 bağımlılıkları modern Termux'ta eksik olabilir.",
         start=f"cd {homeDir}/routersploit && python2 rsf.py")

def sh33ll():
    _run("SH33LL", apt="git python", clone="https://github.com/LOoLzeC/SH33LL",
         note="Python 2 gerektirir; arşivlenmiş durumda.")

def xattacker():
    _run("XAttacker", apt="git php", clone="https://github.com/Moham3dRiahi/XAttacker",
         note="PHP gerektirir.", start=f"cd {homeDir}/XAttacker && php xattacker.php")

def xplsearch():
    _run("XPL-SEARCH", apt="git", clone="https://github.com/Gameye98/XPL-SEARCH",
         note="URL doğrulanmadı; gerekiyorsa düzeltin.")

def androbugs():
    _run("AndroBugs_Framework", apt="git python", clone="https://github.com/AndroBugs/AndroBugs_Framework",
         note="Python 2 gerektirir; arşivlenmiş durumda.",
         start=f"cd {homeDir}/AndroBugs_Framework && python2 androbugs.py -f <apk>")

def clickjacking():
    _run("Clickjacking-Tester", apt="git python", clone="https://github.com/Gameye98/Clickjacking-Tester",
         note="URL doğrulanmadı; gerekiyorsa düzeltin.")

def sn1per():
    _run("Sn1per", apt="git", clone="https://github.com/1N3/Sn1per",
         note="Root/Kali gerektirir; Termux'ta çalışmaz, Kali önerilir.")

# -------- 03 Web Hacking --------
def webdav():
    _run("WebDAV (davscan)", apt="git perl",
         clone="https://github.com/VeNoMouS/davscan",
         note="Orijinal webdav.py bağlantısı ölü; yerine davscan kuruluyor.",
         start=f"cd {homeDir}/davscan && perl davscan.pl -t <hedef-url>")

def webmassploit():
    _run("Webdav Toplu Sömürü", apt="git python",
         note="Orijinal Pastebin betiği kaldırıldı; toplu WebDAV kontrolü için davscan kullanın.")

def atlas():
    _run("Atlas", apt="git python", clone="https://github.com/m4ll0k/Atlas",
         note="Python 2 gerektirir; arşivlenmiş durumda.")

def sqldump():
    _run("sqldump", apt="git python",
         curl="https://gist.githubusercontent.com/Gameye98/76076c9a282a6f32749894d5368024a6/raw/6f9e754f2f81ab2b8efda30603dc8306c65bd651/sqldump.py",
         mv=f"mkdir -p {homeDir}/sqldump && chmod +x sqldump.py && mv sqldump.py {homeDir}/sqldump",
         note="Gist hâlâ erişilebilir; bağlantı koparsa manuel indirin.",
         start=f"python2 {homeDir}/sqldump/sqldump.py")

def websploit():
    _run("Websploit", apt="git python", clone="https://github.com/The404Hacking/websploit",
         note="Python 2 gerektirir; arşivlenmiş durumda.")

def hpb():
    _run("HPB (HTML Pages Builder)", apt="git php", clone="https://github.com/Cvar1984/HPB",
         note="URL doğrulanmadı; gerekiyorsa düzeltin.")

def xsstrike():
    _run("XSStrike", apt="git python", clone="https://github.com/s0md3v/XSStrike",
         cmd=f"cd {homeDir}/XSStrike && pip install -r requirements.txt",
         start=f"python3 {homeDir}/XSStrike/xsstrike.py -u <hedef-url>")

def breacher():
    _run("Breacher", apt="git python", clone="https://github.com/0xInfection/Breacher",
         cmd=f"cd {homeDir}/Breacher && pip install -r requirements.txt",
         start=f"python3 {homeDir}/Breacher/breacher.py -u <site>")

def kodork():
    _run("ko-dork", apt="git python", clone="https://github.com/Cvar1984/ko-dork",
         note="URL doğrulanmadı; gerekiyorsa düzeltin.")

def apsca():
    _run("ApSca", apt="git python", clone="https://github.com/Gameye98/ApSca",
         note="URL doğrulanmadı; gerekiyorsa düzeltin.")

def amox():
    _run("amox", apt="git", clone="https://github.com/Gameye98/amox",
         note="URL doğrulanmadı; gerekiyorsa düzeltin.")

def fade():
    _run("FaDe", apt="git", clone="https://github.com/Gameye98/FaDe",
         note="URL doğrulanmadı; gerekiyorsa düzeltin.")

def xss_payload_list():
    _run("xss-payload-list", apt="git", clone="https://github.com/payloadbox/xss-payload-list",
         note="Yalnızca payload listesi indirilir (araç değil).")

def xadmin():
    _run("Xadmin", apt="git", clone="https://github.com/Gameye98/Xadmin",
         note="URL doğrulanmadı; gerekiyorsa düzeltin.")

def cmseek():
    _run("CMSeeK", apt="git python", clone="https://github.com/Tuhinshubhra/CMSeeK",
         cmd=f"cd {homeDir}/CMSeeK && pip install -r requirements.txt",
         start=f"python3 {homeDir}/CMSeeK/cmseek.py -u <hedef-url>")

def cmsmap():
    _run("CMSmap", apt="git python", clone="https://github.com/Dionach/CMSmap",
         cmd=f"cd {homeDir}/CMSmap && pip install -r requirements.txt",
         start=f"python3 {homeDir}/CMSmap/cmsmap.py -u <hedef-url>")

def crawlbox():
    _run("CrawlBox", apt="git python", clone="https://github.com/Gameye98/CrawlBox",
         note="URL doğrulanmadı; gerekiyorsa düzeltin.")

def lfisuite():
    _run("LFISuite", apt="git python", clone="https://github.com/D35m0nd142/LFISuite",
         note="Python 2 gerektirir; arşivlenmiş durumda.")

def parsero():
    _run("Parsero", apt="git python", clone="https://github.com/beelze-br/parserso",
         note="Python 2 gerektirir; arşivlenmiş durumda.")

def wppluginscanner():
    _run("WP-plugin-scanner", apt="git python", clone="https://github.com/ChamalMP/WP-plugin-scanner",
         start=f"python3 {homeDir}/WP-plugin-scanner/wp_plugin_scanner.py <site>")

def whatweb():
    _run("WhatWeb", apt="whatweb", start="whatweb <hedef-url>")

def fuxploider():
    _run("fuxploider", apt="git python", clone="https://github.com/almandin/fuxploider",
         cmd=f"cd {homeDir}/fuxploider && pip install -r requirements.txt",
         start=f"python3 {homeDir}/fuxploider/fuxploider.py --url <hedef-url>")

# -------- 04 Veritabanı Değerlendirmesi --------
def dbdat():
    _run("DbDat", apt="git python", clone="https://github.com/wireghoul/dbdatformat",
         note="Python 2 gerektirir; arşivlenmiş durumda.")

def nosqlmap():
    _run("NoSQLMap", apt="git python", clone="https://github.com/codingo/NoSQLMap",
         note="Python 2 gerektirir; arşivlenmiş durumda.")

def audit_couchdb():
    _run("audit_couchdb", apt="git python", clone="https://github.com/ccurtin/audit_couchdb",
         note="Python 2 gerektirir; arşivlenmiş durumda.")

def mongoaudit():
    _run("mongoaudit", apt="git python", clone="https://github.com/stamparm/mongoaudit",
         note="Python 2 gerektirir; arşivlenmiş durumda.")

# -------- 05 Parola Saldırıları --------
def cupp():
    _run("Cupp", apt="git python", clone="https://github.com/Mebus/cupp",
         start=f"python3 {homeDir}/cupp/cupp.py -i")

def hash_buster():
    _run("Hash-Buster", apt="git python", clone="https://github.com/s0md3v/Hash-Buster",
         start=f"python3 {homeDir}/Hash-Buster/hash.py -s <hash>")

def instaHack():
    _run("InstaHack", apt="git python", clone="https://github.com/Slayeri4/instahack",
         note="Yalnızca kendi hesaplarınızda test edin.")

def indonesian_wordlist():
    _run("indonesian-wordlist", apt="git", clone="https://github.com/geovedi/indonesian-wordlist")

def fbBrute():
    _run("Facebook Brute Force 3", apt="curl python",
         curl="https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/facebook3.py",
         mv=f"mkdir -p {homeDir}/facebook-brute-3 && mv facebook3.py {homeDir}/facebook-brute-3",
         note="Eski betik; Facebook'un güvenlik önlemleri nedeniyle çalışmayabilir.")

def hydra():
    _run("Hydra", apt="tur-repo", cmd="pkg install -y thc-hydra", start="hydra -h")

def black_hydra():
    _run("Black Hydra", apt="git tur-repo", clone="https://github.com/Gameye98/Black-Hydra",
         cmd="pkg install -y thc-hydra")

def john():
    _run("John the Ripper", apt="john", start="john --help")

def hashcat():
    _run("hashcat", apt="hashcat", start="hashcat --help")

def cewl():
    _run("cewl", apt="cewl", start="cewl <hedef-url> -w wordlist.txt")

# -------- 06 Kablosuz Ağ Saldırıları --------
def aircrack():
    _run("Aircrack-ng", apt="aircrack-ng", start="aircrack-ng")

def wifite2():
    _run("Wifite2", apt="git python", clone="https://github.com/derv82/wifite2",
         cmd=f"cd {homeDir}/wifite2 && pip install -r requirements.txt",
         start=f"python3 {homeDir}/wifite2/wifite.py")

def fluxion():
    _run("Fluxion", apt="git", clone="https://github.com/FluxionNetwork/fluxion",
         note="Kablosuz kartınız monitor modunu desteklemelidir.")

def wifiphisher():
    _run("Wifiphisher", apt="git python", clone="https://github.com/wifiphisher/wifiphisher",
         note="Termux'ta sınırlı çalışır; Kali önerilir.")

def pixiewps():
    _run("Pixiewps", apt="pixiewps", start="pixiewps")

def reaver():
    _run("Reaver", apt="reaver", start="reaver -i wlan0 -b <bssid>")

def mdk3():
    _run("mdk3/mdk4", apt="mdk4", start="mdk4 --help")

def airgeddon():
    _run("Airgeddon", apt="git", clone="https://github.com/v1s1t0r1sh3r3/airgeddon",
         start=f"bash {homeDir}/airgeddon/airgeddon.sh")

def fern():
    _run("Fern Wifi Cracker", apt="git python", clone="https://github.com/savio-code/fern-wifi-cracker",
         note="GUI gerektirir; Termux'ta çalışmaz.")

def wifresti():
    _run("Wifresti", apt="git python", clone="https://github.com/LionSec/wifresti",
         note="Python 2 gerektirir.",
         start=f"python2 {homeDir}/wifresti/wifresti.py")

# -------- 07 Tersine Mühendislik --------
def apktool():
    _run("Apktool", apt="apktool", start="apktool")

def jadx():
    _run("jadx", apt="jadx", start="jadx -d cikti <apk>")

def dex2jar():
    _run("dex2jar", apt="dex2jar", start="d2j-dex2jar <apk>")

def bytecode_viewer():
    _run("Bytecode Viewer", apt="git", clone="https://github.com/Konloch/bytecode-viewer",
         note="Java ve GUI gerektirir; Termux'ta sınırlı.")

def smali():
    _run("smali/baksmali", apt="smali baksmali", start="baksmali d <dex>")

def apkleaks():
    _run("APKLeaks", apt="git python", clone="https://github.com/dwisiswant0/apkleaks",
         cmd=f"cd {homeDir}/apkleaks && pip install -r requirements.txt",
         start=f"apkleaks -f <apk>")

# -------- 08 Sömürü Araçları --------
def metasploit():
    _run("Metasploit", apt="metasploit", start="msfconsole",
         note="Termux resmi paketi; büyük indirmedir, sabırlı olun.")

def commix():
    _run("Commix", apt="git python", clone="https://github.com/commixproject/commix",
         start=f"python3 {homeDir}/commix/commix.py --help")

def searchsploit():
    _run("SearchSploit", apt="exploitdb", start="searchsploit <arama>")

def beef():
    _run("BeEF", apt="git ruby", clone="https://github.com/beefproject/beef",
         cmd=f"cd {homeDir}/beef && ./install",
         note="Tarayıcı GUI'si gerektirir.")

def evilginx2():
    _run("Evilginx2", apt="git golang", clone="https://github.com/kgretzky/evilginx2",
         cmd=f"cd {homeDir}/evilginx2 && go build -o evilginx2 .")

# -------- 09 Dinleme ve Sahteleme --------
def wireshark():
    _run("Wireshark", apt="wireshark", note="Termux'ta yalnızca tshark (CLI) çalışır.", start="tshark")

def tcpdump():
    _run("tcpdump", apt="tcpdump", start="tcpdump")

def ettercap():
    _run("Ettercap", apt="ettercap", note="Root gerektirir.", start="ettercap -T")

def bettercap():
    _run("Bettercap", apt="bettercap", start="bettercap")

def dsniff():
    _run("dsniff", apt="dsniff", start="arpspoof -i wlan0 <hedef> <hedef2>")

def mitmproxy():
    _run("MITMproxy", apt="python", pip="mitmproxy", start="mitmproxy")

def macchanger():
    _run("Macchanger", apt="macchanger", start="macchanger -r wlan0")

def netool():
    _run("Netool", apt="git python", clone="https://github.com/Gameye98/Netool",
         note="URL doğrulanmadı; gerekiyorsa düzeltin.")

# -------- 10 Raporlama Araçları --------
def dradis():
    _run("Dradis", apt="git ruby", clone="https://github.com/dradis/dradis-ce",
         note="Ağır kurulum; Termux yerine Kali önerilir.")

def pipal():
    _run("Pipal", apt="git ruby", clone="https://github.com/digininja/pipal",
         start=f"ruby {homeDir}/pipal/pipal.rb <wordlist>")

def cherrytree():
    _run("CherryTree", apt="cherrytree", note="GUI gerektirir; Termux'ta çalışmaz.")

# -------- 11 Adli Bilişim Araçları --------
def autopsy():
    _run("Autopsy", apt="git", clone="https://github.com/sleuthkit/autopsy",
         note="GUI gerektirir; Termux'ta çalışmaz.")

def guymager():
    _run("Guymager", apt="guymager", note="GUI gerektirir; Termux'ta çalışmaz.")

def dc3dd():
    _run("dc3dd", apt="dc3dd", start="dc3dd if=/dev/... of=/dev/...")

def ddrescue():
    _run("ddrescue", apt="ddrescue", start="ddrescue /dev/... /dev/...")

def binwalk():
    _run("Binwalk", apt="binwalk", start="binwalk <dosya>")

def foremost():
    _run("Foremost", apt="foremost", start="foremost -i <dosya> -o <cikti-dizini>")

# -------- 12 Stres Testi --------
def torshammer():
    _run("Torshammer", apt="git python", clone="https://github.com/dotfighter/torshammer",
         note="Python 2 gerektirir; repo arşivlenmiş durumda.")

def slowloris():
    _run("Slowloris", apt="git python", clone="https://github.com/gkbrk/slowloris",
         start=f"python3 {homeDir}/slowloris/slowloris.py <hedef>")

def goldeneye():
    _run("GoldenEye", apt="git python", clone="https://github.com/jseidl/GoldenEye",
         start=f"python3 {homeDir}/GoldenEye/goldeneye.py <hedef-url>")

def xerxes():
    _run("Xerxes", apt="git clang", clone="https://github.com/baraalmasri/xerxes",
         cmd=f"cd {homeDir}/xerxes && clang xerxes.c -o xerxes",
         start=f"{homeDir}/xerxes/xerxes")

def planetwork_ddos():
    _run("Planetwork-DDOS", apt="git python", clone="https://github.com/Hydra7/Planetwork-DDOS",
         note="Python 2 gerektirir; repo arşivlenmiş durumda.")

def hulk():
    _run("HULK", apt="git python", clone="https://github.com/grafov/hulk",
         start=f"python3 {homeDir}/hulk/hulk.py <hedef-url>")

def fl00d12():
    _run("Fl00d ve Fl00d2", apt="python curl",
         curl="https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d.py",
         cmd=f"mkdir -p {homeDir}/fl00d && mv fl00d.py {homeDir}/fl00d && curl -k -L -O https://raw.githubusercontent.com/Gameye98/Gameye98.github.io/master/scripts/fl00d2.py && mv fl00d2.py {homeDir}/fl00d")

# -------- 13 Linux Dağıtımı Kur --------
def nethunter():
    _run("Kali Nethunter", apt="git wget",
         curl="https://raw.githubusercontent.com/Hax4us/Nethunter-In-Termux/master/kalinethunter",
         cmd="chmod +x kalinethunter && ./kalinethunter")

def ubuntu():
    _run("Ubuntu", apt="proot-distro", cmd="proot-distro install ubuntu",
         start="proot-distro login ubuntu")

def debian():
    _run("Debian", apt="proot-distro", cmd="proot-distro install debian",
         start="proot-distro login debian")

def parrot():
    _run("Parrot OS", apt="proot-distro", cmd="proot-distro install parrot",
         start="proot-distro login parrot")

def blackarch():
    _run("BlackArch", apt="proot-distro", cmd="proot-distro install blackarch",
         start="proot-distro login blackarch")

def alpine():
    _run("Alpine", apt="proot-distro", cmd="proot-distro install alpine",
         start="proot-distro login alpine")

# -------- 14 Termux Yardımcı Araçları --------
def termux_api():
    _run("Termux-API", apt="termux-api", start="termux-battery-status")

def neofetch():
    _run("Neofetch", apt="neofetch", start="neofetch")

def htop():
    _run("htop", apt="htop", start="htop")

def cmatrix():
    _run("cmatrix", apt="cmatrix", start="cmatrix")

def sl():
    _run("sl", apt="sl", start="sl")

def figlet():
    _run("figlet", apt="figlet", start="figlet DarkTool")

def toilet():
    _run("toilet", apt="toilet", start="toilet DarkTool")

def rxfetch():
    _run("rxfetch", apt="git bash", clone="https://github.com/amanishef/rxfetch",
         cmd=f"chmod +x {homeDir}/rxfetch/rxfetch",
         start=f"{homeDir}/rxfetch/rxfetch")

def screenfetch():
    _run("screenfetch", apt="screenfetch", start="screenfetch")

# -------- 15 Shell Fonksiyonu [.bashrc] --------
def bashrc():
    print("\n###### .bashrc güncelleniyor")
    _sh("echo \"alias la='ls -la'\" >> ~/.bashrc")
    _sh("echo \"alias ll='ls -l'\" >> ~/.bashrc")
    _sh("echo \"alias lzmx='cd ~/DarkTool && python DarkTool.py'\" >> ~/.bashrc")
    print('###### Tamamlandi')
    print("###### Aktiflestirmek icin: source ~/.bashrc")
    backtomenu_option()

# -------- 16 CLI Oyunları --------
def moonbuggy():
    _run("Moon-Buggy", apt="moon-buggy", start="moon-buggy")

def ninvaders():
    _run("Ninvaders", apt="ninvaders", start="ninvaders")

def pacman():
    _run("Pacman4Console", apt="pacman4console", start="pacman4console")

def nsnake():
    _run("nSnake", apt="nsnake", start="nsnake")

def greed():
    _run("Greed", apt="greed", start="greed")

def bastet():
    _run("Bastet", apt="bastet", start="bastet")

def vitetris():
    _run("vitetris", apt="vitetris", start="vitetris")

# -------- 17 Zararlı Yazılım Analizi --------
def clamav():
    _run("ClamAV", apt="clamav", start="clamscan <dosya>")

def rkhunter():
    _run("Rkhunter", apt="rkhunter", start="rkhunter --check")

def chkrootkit():
    _run("Chkrootkit", apt="chkrootkit", start="chkrootkit")

def lynis():
    _run("Lynis", apt="lynis", start="lynis audit system")

def yara():
    _run("YARA", apt="yara", start="yara <kural-dosyasi> <hedef-dosya>")

def exiftool():
    _run("ExifTool", apt="exiftool", start="exiftool <dosya>")

def strings():
    _run("strings (binutils)", apt="binutils", start="strings <dosya>")

# -------- 18 Derleyici/Yorumlayıcı --------
def python3():
    _run("Python 3", apt="python", start="python3")

def nodejs():
    _run("Node.js", apt="nodejs", start="node -v")

def clang():
    _run("Clang/GCC", apt="clang", start="clang --version")

def ruby():
    _run("Ruby", apt="ruby", start="ruby -v")

def php():
    _run("PHP", apt="php", start="php -v")

def perl():
    _run("Perl", apt="perl", start="perl -v")

def golang():
    _run("Go", apt="golang", start="go version")

def rust():
    _run("Rust", apt="rust", start="rustc --version")

def openjdk():
    _run("OpenJDK", apt="openjdk-17", start="java -version")

def lua():
    _run("Lua", apt="lua", start="lua -v")

def kotlin():
    _run("Kotlin", apt="kotlin", start="kotlin -version")

# -------- 19 Sosyal Mühendislik Araçları --------
def socialfish():
    _run("SocialFish", apt="git python", clone="https://github.com/UndeadSec/SocialFish",
         cmd=f"cd {homeDir}/SocialFish && pip install -r requirements.txt",
         start=f"python3 {homeDir}/SocialFish/SocialFish.py <ip> <port>")

def hiddeneye():
    _run("HiddenEye", apt="git python", clone="https://github.com/DarkSecDevelopers/HiddenEye",
         note="Repo arşivlenmiş durumda; bağımlılıklar eksik kalabilir.")

def shellphish():
    _run("Shellphish", apt="git", clone="https://github.com/thelinuxchoice/shellphish",
         start=f"bash {homeDir}/shellphish/shellphish.sh")

def saycheese():
    _run("SayCheese", apt="git", clone="https://github.com/thelinuxchoice/saycheese",
         start=f"bash {homeDir}/saycheese/saycheese.sh")

def maskphish():
    _run("MaskPhish", apt="git", clone="https://github.com/jaykali/maskphish",
         start=f"bash {homeDir}/maskphish/maskphish.sh")

def blackeye():
    _run("BlackEye", apt="git", clone="https://github.com/thelinuxchoice/blackeye",
         start=f"bash {homeDir}/blackeye/blackeye.sh")

def zphisher():
    _run("Zphisher", apt="git", clone="https://github.com/htr-tech/zphisher",
         start=f"bash {homeDir}/zphisher/zphisher.sh")

# ============================================================
#  BÖLÜM 3/3 - Menüler ve Ana Program
# ============================================================

ALL_TOOLS = [
    nmap, sqlmap, red_hawk, theharvester, sherlock, maigret, userrecon,
    phoneinfoga, sublist3r, dnsrecon, fierce, dnsx, subfinder, httpx,
    osintgram, h8mail,
    dsss, sqliv, sqlscan, wordpreSScan, wpscan, wordpresscan, tmscanner,
    rang3r, routersploit, sh33ll, xattacker, xplsearch, androbugs,
    clickjacking, sn1per,
    webdav, webmassploit, atlas, sqldump, websploit, hpb, xsstrike,
    breacher, kodork, apsca, amox, fade, xss_payload_list, xadmin,
    cmseek, cmsmap, crawlbox, lfisuite, parsero, wppluginscanner,
    whatweb, fuxploider,
    dbdat, nosqlmap, audit_couchdb, mongoaudit,
    cupp, hash_buster, instaHack, indonesian_wordlist, fbBrute, hydra,
    black_hydra, john, hashcat, cewl,
    aircrack, wifite2, fluxion, wifiphisher, pixiewps, reaver, mdk3,
    airgeddon, fern, wifresti,
    apktool, jadx, dex2jar, bytecode_viewer, smali, apkleaks,
    metasploit, commix, searchsploit, beef, evilginx2,
    wireshark, tcpdump, ettercap, bettercap, dsniff, mitmproxy,
    macchanger, netool,
    dradis, pipal, cherrytree,
    autopsy, guymager, dc3dd, ddrescue, binwalk, foremost,
    torshammer, slowloris, goldeneye, xerxes, planetwork_ddos, hulk, fl00d12,
    nethunter, ubuntu, debian, parrot, blackarch, alpine,
    termux_api, neofetch, htop, cmatrix, sl, figlet, toilet, rxfetch, screenfetch,
    moonbuggy, ninvaders, pacman, nsnake, greed, bastet, vitetris,
    clamav, rkhunter, chkrootkit, lynis, yara, exiftool, strings,
    python3, nodejs, clang, ruby, php, perl, golang, rust, openjdk, lua, kotlin,
    socialfish, hiddeneye, shellphish, saycheese, maskphish, blackeye, zphisher,
]

def install_all():
    print("\n    [!] TUM ARACLAR KURULUYOR (uzun surebilir)...")
    print("    [!] Durdurmak icin Ctrl+C\n")
    timeout(3)
    for tool in ALL_TOOLS:
        try:
            tool()
        except KeyboardInterrupt:
            print("\n    [!] Kurulum kullanici tarafindan durduruldu.")
            break
        except Exception as e:
            print(f"    ! Hata: {tool.__name__}: {e}")
    print("\n    [✓] Tum araclar tamamlandi.")
    input("\n[Enter] ile ana menuye don...")

def cat1_bilgi():
    print("""
    [01] Nmap                [02] sqlmap              [03] RED HAWK
    [04] theHarvester        [05] Sherlock            [06] Maigret
    [07] UserRecon           [08] PhoneInfoga         [09] Sublist3r
    [10] DNSRecon            [11] Fierce              [12] dnsx
    [13] Subfinder           [14] httpx               [15] Osintgram
    [16] h8mail
    --------------------------------------------
    [00] Ana menuye don
""")
    sec = parse_selection(input("DarkTool > set_install "))
    for x in sec:
        if x in ("01","1"): nmap()
        elif x in ("02","2"): sqlmap()
        elif x in ("03","3"): red_hawk()
        elif x in ("04","4"): theharvester()
        elif x in ("05","5"): sherlock()
        elif x in ("06","6"): maigret()
        elif x in ("07","7"): userrecon()
        elif x in ("08","8"): phoneinfoga()
        elif x in ("09","9"): sublist3r()
        elif x == "10": dnsrecon()
        elif x == "11": fierce()
        elif x == "12": dnsx()
        elif x == "13": subfinder()
        elif x == "14": httpx()
        elif x == "15": osintgram()
        elif x == "16": h8mail()
        elif x in ("00","0"): return
        else: print("\nHATA: Gecersiz Giris"); timeout(1)
    backtomenu_option()

def cat2_zafiyet():
    print("""
    [01] DSSS                 [02] SQLiv                [03] sqlscan
    [04] Wordpresscan         [05] WPScan               [06] termux-wordpresscan
    [07] TM-scanner           [08] Rang3r               [09] Routersploit
    [10] SH33LL               [11] XAttacker            [12] XPL-SEARCH
    [13] AndroBugs            [14] Clickjacking-Tester  [15] Sn1per
    --------------------------------------------
    [00] Ana menuye don
""")
    sec = parse_selection(input("DarkTool > set_install "))
    for x in sec:
        if x in ("01","1"): dsss()
        elif x in ("02","2"): sqliv()
        elif x in ("03","3"): sqlscan()
        elif x in ("04","4"): wordpreSScan()
        elif x in ("05","5"): wpscan()
        elif x in ("06","6"): wordpresscan()
        elif x in ("07","7"): tmscanner()
        elif x in ("08","8"): rang3r()
        elif x in ("09","9"): routersploit()
        elif x == "10": sh33ll()
        elif x == "11": xattacker()
        elif x == "12": xplsearch()
        elif x == "13": androbugs()
        elif x == "14": clickjacking()
        elif x == "15": sn1per()
        elif x in ("00","0"): return
        else: print("\nHATA: Gecersiz Giris"); timeout(1)
    backtomenu_option()

def cat3_web():
    print("""
    [01] WebDAV (davscan)     [02] Webmassploit         [03] Atlas
    [04] sqldump              [05] Websploit            [06] HPB
    [07] XSStrike             [08] Breacher             [09] ko-dork
    [10] ApSca                [11] amox                 [12] FaDe
    [13] xss-payload-list     [14] Xadmin               [15] CMSeeK
    [16] CMSmap               [17] CrawlBox             [18] LFISuite
    [19] Parsero              [20] WP-plugin-scanner    [21] WhatWeb
    [22] fuxploider
    --------------------------------------------
    [00] Ana menuye don
""")
    sec = parse_selection(input("DarkTool > set_install "))
    for x in sec:
        if x in ("01","1"): webdav()
        elif x in ("02","2"): webmassploit()
        elif x in ("03","3"): atlas()
        elif x in ("04","4"): sqldump()
        elif x in ("05","5"): websploit()
        elif x in ("06","6"): hpb()
        elif x in ("07","7"): xsstrike()
        elif x in ("08","8"): breacher()
        elif x in ("09","9"): kodork()
        elif x == "10": apsca()
        elif x == "11": amox()
        elif x == "12": fade()
        elif x == "13": xss_payload_list()
        elif x == "14": xadmin()
        elif x == "15": cmseek()
        elif x == "16": cmsmap()
        elif x == "17": crawlbox()
        elif x == "18": lfisuite()
        elif x == "19": parsero()
        elif x == "20": wppluginscanner()
        elif x == "21": whatweb()
        elif x == "22": fuxploider()
        elif x in ("00","0"): return
        else: print("\nHATA: Gecersiz Giris"); timeout(1)
    backtomenu_option()

def cat4_db():
    print("""
    [01] DbDat
    [02] NoSQLMap
    [03] audit_couchdb
    [04] mongoaudit
    --------------------------------------------
    [00] Ana menuye don
""")
    sec = parse_selection(input("DarkTool > set_install "))
    for x in sec:
        if x in ("01","1"): dbdat()
        elif x in ("02","2"): nosqlmap()
        elif x in ("03","3"): audit_couchdb()
        elif x in ("04","4"): mongoaudit()
        elif x in ("00","0"): return
        else: print("\nHATA: Gecersiz Giris"); timeout(1)
    backtomenu_option()

def cat5_parola():
    print("""
    [01] Cupp                 [02] Hash-Buster          [03] InstaHack
    [04] indonesian-wordlist  [05] FB Brute Force 3     [06] Hydra
    [07] Black Hydra          [08] John the Ripper      [09] hashcat
    [10] cewl
    --------------------------------------------
    [00] Ana menuye don
""")
    sec = parse_selection(input("DarkTool > set_install "))
    for x in sec:
        if x in ("01","1"): cupp()
        elif x in ("02","2"): hash_buster()
        elif x in ("03","3"): instaHack()
        elif x in ("04","4"): indonesian_wordlist()
        elif x in ("05","5"): fbBrute()
        elif x in ("06","6"): hydra()
        elif x in ("07","7"): black_hydra()
        elif x in ("08","8"): john()
        elif x in ("09","9"): hashcat()
        elif x == "10": cewl()
        elif x in ("00","0"): return
        else: print("\nHATA: Gecersiz Giris"); timeout(1)
    backtomenu_option()

def cat6_wifi():
    print("""
    [01] Aircrack-ng          [02] Wifite2              [03] Fluxion
    [04] Wifiphisher          [05] Pixiewps             [06] Reaver
    [07] mdk3/mdk4            [08] Airgeddon            [09] Fern
    [10] Wifresti
    --------------------------------------------
    [00] Ana menuye don
""")
    sec = parse_selection(input("DarkTool > set_install "))
    for x in sec:
        if x in ("01","1"): aircrack()
        elif x in ("02","2"): wifite2()
        elif x in ("03","3"): fluxion()
        elif x in ("04","4"): wifiphisher()
        elif x in ("05","5"): pixiewps()
        elif x in ("06","6"): reaver()
        elif x in ("07","7"): mdk3()
        elif x in ("08","8"): airgeddon()
        elif x in ("09","9"): fern()
        elif x == "10": wifresti()
        elif x in ("00","0"): return
        else: print("\nHATA: Gecersiz Giris"); timeout(1)
    backtomenu_option()

def cat7_re():
    print("""
    [01] Apktool              [02] jadx                 [03] dex2jar
    [04] Bytecode Viewer      [05] smali/baksmali       [06] APKLeaks
    --------------------------------------------
    [00] Ana menuye don
""")
    sec = parse_selection(input("DarkTool > set_install "))
    for x in sec:
        if x in ("01","1"): apktool()
        elif x in ("02","2"): jadx()
        elif x in ("03","3"): dex2jar()
        elif x in ("04","4"): bytecode_viewer()
        elif x in ("05","5"): smali()
        elif x in ("06","6"): apkleaks()
        elif x in ("00","0"): return
        else: print("\nHATA: Gecersiz Giris"); timeout(1)
    backtomenu_option()

def cat8_exploit():
    print("""
    [01] Metasploit           [02] Commix               [03] SearchSploit
    [04] BeEF                 [05] Evilginx2
    --------------------------------------------
    [00] Ana menuye don
""")
    sec = parse_selection(input("DarkTool > set_install "))
    for x in sec:
        if x in ("01","1"): metasploit()
        elif x in ("02","2"): commix()
        elif x in ("03","3"): searchsploit()
        elif x in ("04","4"): beef()
        elif x in ("05","5"): evilginx2()
        elif x in ("00","0"): return
        else: print("\nHATA: Gecersiz Giris"); timeout(1)
    backtomenu_option()

def cat9_dinleme():
    print("""
    [01] Wireshark/tshark     [02] tcpdump              [03] Ettercap
    [04] Bettercap            [05] dsniff               [06] MITMproxy
    [07] Macchanger           [08] Netool
    --------------------------------------------
    [00] Ana menuye don
""")
    sec = parse_selection(input("DarkTool > set_install "))
    for x in sec:
        if x in ("01","1"): wireshark()
        elif x in ("02","2"): tcpdump()
        elif x in ("03","3"): ettercap()
        elif x in ("04","4"): bettercap()
        elif x in ("05","5"): dsniff()
        elif x in ("06","6"): mitmproxy()
        elif x in ("07","7"): macchanger()
        elif x in ("08","8"): netool()
        elif x in ("00","0"): return
        else: print("\nHATA: Gecersiz Giris"); timeout(1)
    backtomenu_option()

def cat10_rapor():
    print("""
    [01] Dradis
    [02] Pipal
    [03] CherryTree
    --------------------------------------------
    [00] Ana menuye don
""")
    sec = parse_selection(input("DarkTool > set_install "))
    for x in sec:
        if x in ("01","1"): dradis()
        elif x in ("02","2"): pipal()
        elif x in ("03","3"): cherrytree()
        elif x in ("00","0"): return
        else: print("\nHATA: Gecersiz Giris"); timeout(1)
    backtomenu_option()

def cat11_adli():
    print("""
    [01] Autopsy              [02] Guymager             [03] dc3dd
    [04] ddrescue             [05] Binwalk              [06] Foremost
    --------------------------------------------
    [00] Ana menuye don
""")
    sec = parse_selection(input("DarkTool > set_install "))
    for x in sec:
        if x in ("01","1"): autopsy()
        elif x in ("02","2"): guymager()
        elif x in ("03","3"): dc3dd()
        elif x in ("04","4"): ddrescue()
        elif x in ("05","5"): binwalk()
        elif x in ("06","6"): foremost()
        elif x in ("00","0"): return
        else: print("\nHATA: Gecersiz Giris"); timeout(1)
    backtomenu_option()

def cat12_stres():
    print("""
    [01] Torshammer           [02] Slowloris            [03] GoldenEye
    [04] Xerxes               [05] Planetwork-DDOS      [06] HULK
    [07] Fl00d / Fl00d2
    --------------------------------------------
    [00] Ana menuye don
""")
    sec = parse_selection(input("DarkTool > set_install "))
    for x in sec:
        if x in ("01","1"): torshammer()
        elif x in ("02","2"): slowloris()
        elif x in ("03","3"): goldeneye()
        elif x in ("04","4"): xerxes()
        elif x in ("05","5"): planetwork_ddos()
        elif x in ("06","6"): hulk()
        elif x in ("07","7"): fl00d12()
        elif x in ("00","0"): return
        else: print("\nHATA: Gecersiz Giris"); timeout(1)
    backtomenu_option()

def cat13_distro():
    print("""
    [01] Kali Nethunter       [02] Ubuntu               [03] Debian
    [04] Parrot OS            [05] BlackArch            [06] Alpine
    --------------------------------------------
    [00] Ana menuye don
""")
    sec = parse_selection(input("DarkTool > set_install "))
    for x in sec:
        if x in ("01","1"): nethunter()
        elif x in ("02","2"): ubuntu()
        elif x in ("03","3"): debian()
        elif x in ("04","4"): parrot()
        elif x in ("05","5"): blackarch()
        elif x in ("06","6"): alpine()
        elif x in ("00","0"): return
        else: print("\nHATA: Gecersiz Giris"); timeout(1)
    backtomenu_option()

def cat14_util():
    print("""
    [01] Termux-API           [02] Neofetch             [03] htop
    [04] cmatrix              [05] sl                   [06] figlet
    [07] toilet               [08] rxfetch              [09] screenfetch
    --------------------------------------------
    [00] Ana menuye don
""")
    sec = parse_selection(input("DarkTool > set_install "))
    for x in sec:
        if x in ("01","1"): termux_api()
        elif x in ("02","2"): neofetch()
        elif x in ("03","3"): htop()
        elif x in ("04","4"): cmatrix()
        elif x in ("05","5"): sl()
        elif x in ("06","6"): figlet()
        elif x in ("07","7"): toilet()
        elif x in ("08","8"): rxfetch()
        elif x in ("09","9"): screenfetch()
        elif x in ("00","0"): return
        else: print("\nHATA: Gecersiz Giris"); timeout(1)
    backtomenu_option()

def cat15_bashrc():
    bashrc()

def cat16_oyun():
    print("""
    [01] Moon-Buggy           [02] Ninvaders            [03] Pacman4Console
    [04] nSnake               [05] Greed                [06] Bastet
    [07] vitetris
    --------------------------------------------
    [00] Ana menuye don
""")
    sec = parse_selection(input("DarkTool > set_install "))
    for x in sec:
        if x in ("01","1"): moonbuggy()
        elif x in ("02","2"): ninvaders()
        elif x in ("03","3"): pacman()
        elif x in ("04","4"): nsnake()
        elif x in ("05","5"): greed()
        elif x in ("06","6"): bastet()
        elif x in ("07","7"): vitetris()
        elif x in ("00","0"): return
        else: print("\nHATA: Gecersiz Giris"); timeout(1)
    backtomenu_option()

def cat17_malware():
    print("""
    [01] ClamAV               [02] Rkhunter             [03] Chkrootkit
    [04] Lynis                [05] YARA                 [06] ExifTool
    [07] strings (binutils)
    --------------------------------------------
    [00] Ana menuye don
""")
    sec = parse_selection(input("DarkTool > set_install "))
    for x in sec:
        if x in ("01","1"): clamav()
        elif x in ("02","2"): rkhunter()
        elif x in ("03","3"): chkrootkit()
        elif x in ("04","4"): lynis()
        elif x in ("05","5"): yara()
        elif x in ("06","6"): exiftool()
        elif x in ("07","7"): strings()
        elif x in ("00","0"): return
        else: print("\nHATA: Gecersiz Giris"); timeout(1)
    backtomenu_option()

def cat18_derleyici():
    print("""
    [01] Python 3             [02] Node.js              [03] Clang/GCC
    [04] Ruby                 [05] PHP                  [06] Perl
    [07] Go                   [08] Rust                 [09] OpenJDK
    [10] Lua                  [11] Kotlin
    --------------------------------------------
    [00] Ana menuye don
""")
    sec = parse_selection(input("DarkTool > set_install "))
    for x in sec:
        if x in ("01","1"): python3()
        elif x in ("02","2"): nodejs()
        elif x in ("03","3"): clang()
        elif x in ("04","4"): ruby()
        elif x in ("05","5"): php()
        elif x in ("06","6"): perl()
        elif x in ("07","7"): golang()
        elif x in ("08","8"): rust()
        elif x in ("09","9"): openjdk()
        elif x == "10": lua()
        elif x == "11": kotlin()
        elif x in ("00","0"): return
        else: print("\nHATA: Gecersiz Giris"); timeout(1)
    backtomenu_option()

def cat19_social():
    print("""
    [01] SocialFish           [02] HiddenEye            [03] Shellphish
    [04] SayCheese            [05] MaskPhish            [06] BlackEye
    [07] Zphisher
    --------------------------------------------
    [00] Ana menuye don
""")
    sec = parse_selection(input("DarkTool > set_install "))
    for x in sec:
        if x in ("01","1"): socialfish()
        elif x in ("02","2"): hiddeneye()
        elif x in ("03","3"): shellphish()
        elif x in ("04","4"): saycheese()
        elif x in ("05","5"): maskphish()
        elif x in ("06","6"): blackeye()
        elif x in ("07","7"): zphisher()
        elif x in ("00","0"): return
        else: print("\nHATA: Gecersiz Giris"); timeout(1)
    backtomenu_option()

def main():
    first_run()
    while True:
        os.system("clear")
        banner()
        print(main_menu)
        try:
            secim = input("DarkTool > ").strip()
        except (KeyboardInterrupt, EOFError):
            sys.exit()
        if secim in ("1", "01"):
            cat1_bilgi()
        elif secim in ("2", "02"):
            cat2_zafiyet()
        elif secim in ("3", "03"):
            cat3_web()
        elif secim in ("4", "04"):
            cat4_db()
        elif secim in ("5", "05"):
            cat5_parola()
        elif secim in ("6", "06"):
            cat6_wifi()
        elif secim in ("7", "07"):
            cat7_re()
        elif secim in ("8", "08"):
            cat8_exploit()
        elif secim in ("9", "09"):
            cat9_dinleme()
        elif secim == "10":
            cat10_rapor()
        elif secim == "11":
            cat11_adli()
        elif secim == "12":
            cat12_stres()
        elif secim == "13":
            cat13_distro()
        elif secim == "14":
            cat14_util()
        elif secim == "15":
            cat15_bashrc()
        elif secim == "16":
            cat16_oyun()
        elif secim == "17":
            cat17_malware()
        elif secim == "18":
            cat18_derleyici()
        elif secim == "19":
            cat19_social()
        elif secim == "98":
            install_all()
        elif secim == "99":
            update_DarkTool()
        elif secim in ("0", "00"):
            sys.exit()
        else:
            print("\nHATA: Gecersiz Giris")
            timeout(2)

if __name__ == "__main__":
    main()
