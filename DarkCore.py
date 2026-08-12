## lzmcore.py - DarkTool'un kullanışlı modülü (v5.0)
##
import os, sys, json, urllib.request
from time import sleep as timeout

current_dir = os.getcwd()
DarkTool_banner = """
 _
( )
| |       _ _  ____  _   _   ___ ___   _   _
| |  _  /'_` )(_  ,)( ) ( )/' _ ` _ `\( ) ( )(`\/')
| |_( )( (_| | /'/_ | (_) || ( ) ( ) || (_) | >  <
(____/'`\__,_)(____)`\__, |(_) (_) (_)`\___/'(_/\_)
                    ( )_| |
                    `\___/'
"""
backtomenu_banner = """
  [99] Ana menüye dön
  [00] DarkTool'tan çık
"""

prefix = os.getenv("PREFIX")
configBase = "[HOME] = ~"
configFile = "../DarkTool.conf"
cache_1 = prefix+"/tmp/DarkTool_1"

def repo_check(sources_list):
    if os.path.isfile(os.getenv("PREFIX")+"/etc/apt/sources.list.d/"+sources_list):
        return True
    return False

def writeStatus(statusId):
    open(cache_1,"w").write(str(statusId))

def readStatus():
    try:
        statusId = open(cache_1,"r").read()
        return statusId == "1"
    except IOError:
        return False

def checkConfigFile():
    if os.path.exists(configFile):
        if os.path.isdir(configFile):
            os.system(f"rm -rf {configFile}")
            open(configFile,"w").write(configBase)
    else:
        open(configFile,"w").write(configBase)

def loadConfigFile():
    checkConfigFile()
    lfile = "~"
    try:
        lfile = [x.split("=")[-1].strip() for x in open(configFile,"r").splitlines() if x.split("=")[0].strip() == "[HOME]"][0]
    except Exception:
        lfile = "~"
    return lfile

homeDir = loadConfigFile()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def backtomenu_option():
    if not readStatus():
        print(backtomenu_banner)
        backtomenu = input("lzmx > ")
        if backtomenu == "99":
            restart_program()
        elif backtomenu in ("0", "00"):
            sys.exit()
        else:
            print("\nHATA: Geçersiz Giriş")
            timeout(2)
            restart_program()

def banner():
    print(DarkTool_banner)

def shell(cmd):
    os.system(cmd)

def gh_latest_asset(repo, pattern):
    api = f"https://api.github.com/repos/{repo}/releases/latest"
    try:
        req = urllib.request.Request(api, headers={"User-Agent": "DarkTool"})
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.load(r)
        for a in data.get("assets", []):
            if pattern in a["name"]:
                return a["browser_download_url"], a["name"]
    except Exception as e:
        print(f"    ! GitHub API hatası: {e}")
    return None, None

def install_release(repo, pattern, binname, findname=None):
    findname = findname or binname
    shell("pkg install -y curl unzip > /dev/null 2>&1")
    url, fname = gh_latest_asset(repo, pattern)
    if not url:
        print("    ! Sürüm bulunamadı (repo adını veya mimariyi kontrol edin).")
        return
    print(f"    * {fname} indiriliyor...")
    shell(f"curl -sL -o /tmp/{fname} '{url}'")
    shell("rm -rf /tmp/lzrel && mkdir -p /tmp/lzrel")
    if fname.endswith(".zip"):
        shell(f"unzip -o -q /tmp/{fname} -d /tmp/lzrel")
    else:
        shell(f"tar -xzf /tmp/{fname} -C /tmp/lzrel")
    shell(f"find /tmp/lzrel -type f -name '{findname}' -exec chmod +x {{}} \\; -exec mv {{}} $PREFIX/bin/{binname} \\;")
    shell(f"rm -rf /tmp/lzrel /tmp/{fname}")
    if os.path.exists(f"{prefix}/bin/{binname}"):
        print(f"    * {binname} -> $PREFIX/bin/ kuruldu.")

# ---------------- KATEGORİLER ----------------
CATS = {
 1: "Bilgi Toplama", 2: "Zafiyet Analizi", 3: "Web Hacking",
 4: "Veritabanı Değerlendirmesi", 5: "Parola Saldırıları", 6: "Kablosuz Ağ Saldırıları",
 7: "Tersine Mühendislik", 8: "Sömürü Araçları", 9: "Dinleme ve Sahteleme",
 10: "Raporlama Araçları", 11: "Adli Bilişim Araçları", 12: "Stres Testi",
 13: "Linux Dağıtımı Kur", 14: "Termux Yardımcı Araçları", 15: "Shell Fonksiyonu [.bashrc]",
 16: "CLI Oyunları", 17: "Zararlı Yazılım Analizi", 18: "Derleyici/Yorumlayıcı",
 19: "Sosyal Mühendislik Araçları",
}

# c   = kategoriler (bir araç birden çok kategoride görünebilir)
# d   = açıklama
# pkg = Termux paketleri (pkg install -y)
# pip = pip paketleri (python -m pip install)
# repo= git clone edilecek GitHub repoları (kullanıcı/depo)
# need= paket bağımlılıkları
# pre = kurulumdan önce çalışacak komut
# post= kurulumdan sonra çalışacak komut ({home} -> homeDir)
# release = (kullanıcı/depo, asset kalıbı, ikili adı) GitHub release indirme
# shfunc = .myshfunc/*.sh dosyasını .bashrc'ye ekle
# run  = başlatma komutu (bilgi amaçlı)
TOOLS = {
 # --- 01 Bilgi Toplama ---
 "nmap":        {"c":[1,2], "d":"Nmap: Ağ keşfi ve güvenlik denetimi", "pkg":["nmap"], "run":"nmap"},
 "sqlmap":      {"c":[1,2,3,4], "d":"sqlmap: Otomatik SQL injection ve veritabanı ele geçirme", "pip":["sqlmap"], "run":"sqlmap"},
 "red_hawk":    {"c":[1], "d":"RED HAWK: Bilgi toplama, zafiyet taraması ve gezinme", "need":["git","php"], "repo":["Tuhinshubhra/RED_HAWK"], "run":"cd ~/RED_HAWK && php red_hawk.php"},
 "theharvester":{"c":[1], "d":"theHarvester: E-posta, alt alan adı ve IP OSINT toplayıcı", "pip":["theHarvester"], "run":"theHarvester -d ornek.com -b all"},
 "sherlock":    {"c":[1], "d":"Sherlock: Kullanıcı adıyla sosyal medya hesap avcılığı", "pip":["sherlock-project"], "run":"sherlock kullanici_adi"},
 "maigret":     {"c":[1], "d":"Maigret: Kullanıcı adıyla binlerce siteden dosya toplama", "pip":["maigret"], "run":"maigret kullanici_adi"},
 "userrecon":   {"c":[1], "d":"UserRecon: 75+ sosyal ağda kullanıcı adı tespiti", "need":["git"], "repo":["thelinuxchoice/userrecon"], "run":"cd ~/userrecon && bash userrecon.sh"},
 "phoneinfoga": {"c":[1], "d":"PhoneInfoga: Ücretsiz kaynaklarla telefon numarası OSINT", "release":("sundowndev/phoneinfoga","linux_arm64.tar.gz","phoneinfoga"), "run":"phoneinfoga scan -n +90XXXXXXXXXX"},
 "sublist3r":   {"c":[1], "d":"Sublist3r: Hızlı alt alan adı numaralandırma", "pip":["sublist3r"], "run":"sublist3r -d ornek.com"},
 "dnsrecon":    {"c":[1], "d":"DNSRecon: DNS keşfi ve güvenlik değerlendirmesi", "need":["git","python"], "repo":["darkoperator/dnsrecon"], "post":"python -m pip install -r {home}/dnsrecon/requirements.txt", "run":"python ~/dnsrecon/dnsrecon.py -d ornek.com"},
 "fierce":      {"c":[1], "d":"Fierce: Bitişik olmayan IP alanı DNS keşfi", "pip":["fierce"], "run":"fierce --domain ornek.com"},
 "dnsx":        {"c":[1], "d":"dnsx: Hızlı ve esnek DNS sorgu aracı", "release":("projectdiscovery/dnsx","linux_arm64.zip","dnsx"), "run":"dnsx -d ornek.com"},
 "subfinder":   {"c":[1], "d":"Subfinder: Pasif alt alan adı keşfi", "release":("projectdiscovery/subfinder","linux_arm64.zip","subfinder"), "run":"subfinder -d ornek.com"},
 "httpx":       {"c":[1,3], "d":"httpx: Hızlı HTTP prob aracı", "release":("projectdiscovery/httpx","linux_arm64.zip","httpx"), "run":"httpx -l hedefler.txt"},
 "osintgram":   {"c":[1], "d":"Osintgram: Instagram OSINT aracı", "need":["git","python"], "repo":["Datalux/Osintgram"], "post":"python -m pip install -r {home}/Osintgram/requirements.txt", "run":"cd ~/Osintgram && python3 main.py"},
 "h8mail":      {"c":[1], "d":"h8mail: E-posta sızıntısı ve OSINT aracı", "pip":["h8mail"], "run":"h8mail -t hedef@mail.com"},

 # ============ 02 - ZAFİYET ANALİZİ ============
def dsss():
    _run("DSSS (Damn Small SQLi Scanner)", apt="git python",
         clone="https://github.com/stamparm/DSSS",
         start="python3 dsss.py -u <hedef-url>")

def sqliv():
    _run("SQLiv", apt="git python", clone="https://github.com/the-robot/sqliv",
         note="Python 2 gerektirir; repo arşivlenmiş durumda.")

def sqlscan():
    _run("sqlscan", apt="git php", clone="https://github.com/Cvar1984/sqlscan",
         note="PHP gerektirir.", start="php sqlscan.php")

def wordpreSScan():
    _run("Wordpresscan", apt="git python", clone="https://github.com/swisskyrepo/Wordpresscan",
         cmd=f"cd {homeDir}/Wordpresscan && pip install -r requirements.txt",
         note="Python 2 gerektirir; repo arşivlenmiş durumda.")

def wpscan():
    _run("WPScan", apt="ruby curl",
         cmd="gem install wpscan",
         note="Eski git clone yöntemi kaldırıldı; güncel resmi yol: gem.",
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
         start="python2 rsf.py")

def sh33ll():
    _run("SH33LL", apt="git python", clone="https://github.com/LOoLzeC/SH33LL",
         note="Python 2 gerektirir; arşivlenmiş durumda.")

def xattacker():
    _run("XAttacker", apt="git php", clone="https://github.com/Moham3dRiahi/XAttacker",
         note="PHP gerektirir.", start="php xattacker.php")

def xplsearch():
    _run("XPL-SEARCH", apt="git", clone="https://github.com/Gameye98/XPL-SEARCH",
         note="URL doğrulanmadı; gerekiyorsa düzeltin.")

def androbugs():
    _run("AndroBugs_Framework", apt="git python", clone="https://github.com/AndroBugs/AndroBugs_Framework",
         note="Python 2 gerektirir; arşivlenmiş durumda.",
         start="python2 androbugs.py -f <apk>")

def clickjacking():
    _run("Clickjacking-Tester", apt="git python", clone="https://github.com/Gameye98/Clickjacking-Tester",
         note="URL doğrulanmadı; gerekiyorsa düzeltin.")

def sn1per():
    _run("Sn1per", apt="git", clone="https://github.com/1N3/Sn1per",
         note="Root/Kali gerektirir; Termux'ta çalışmaz, Kali önerilir.")

# ============ 03 - WEB HACKING ============
def webdav():
    _run("WebDAV (davscan)", apt="git perl",
         clone="https://github.com/VeNoMouS/davscan",
         note="Orijinal webdav.py (Pastebin) bağlantısı ölü; yerine WebDAV yöntem tarayıcısı davscan kuruluyor.",
         start="perl davscan.pl -t <hedef-url>")

def webmassploit():
    _run("Webdav Toplu Sömürü",
         apt="git python",
         note="Orijinal Pastebin betiği (K1VYVHxX) kaldırıldı; araç kullanımdan kaldırıldı. Toplu WebDAV kontrolü için davscan kullanın: perl davscan.pl -t <url>")

def atlas():
    _run("Atlas", apt="git python", clone="https://github.com/m4ll0k/Atlas",
         note="Python 2 gerektirir; arşivlenmiş durumda.")

def sqldump():
    _run("sqldump", apt="git python",
         curl="https://gist.githubusercontent.com/Gameye98/76076c9a282a6f32749894d5368024a6/raw/6f9e754f2f81ab2b8efda30603dc8306c65bd651/sqldump.py",
         mv=f"mkdir -p {homeDir}/sqldump && chmod +x sqldump.py && mv sqldump.py {homeDir}/sqldump",
         note="Gist hâlâ erişilebilir durumda; bağlantı koparsa manuel indirin.",
         start="python2 sqldump.py")

def websploit():
    _run("Websploit", apt="git python", clone="https://github.com/The404Hacking/websploit",
         note="Python 2 gerektirir; arşivlenmiş durumda.")

def hpb():
    _run("HPB (HTML Pages Builder)", apt="git php", clone="https://github.com/Cvar1984/HPB",
         note="URL doğrulanmadı; gerekiyorsa düzeltin.")

def xsstrike():
    _run("XSStrike", apt="git python", clone="https://github.com/s0md3v/XSStrike",
         cmd=f"cd {homeDir}/XSStrike && pip install -r requirements.txt",
         start="python3 xsstrike.py -u <hedef-url>")

def breacher():
    _run("Breacher", apt="git python", clone="https://github.com/0xInfection/Breacher",
         cmd=f"cd {homeDir}/Breacher && pip install -r requirements.txt",
         start="python3 breacher.py -u <site>")

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
         start="python3 cmseek.py -u <hedef-url>")

def cmsmap():
    _run("CMSmap", apt="git python", clone="https://github.com/Dionach/CMSmap",
         cmd=f"cd {homeDir}/CMSmap && pip install -r requirements.txt",
         start="python3 cmsmap.py -u <hedef-url>")

def crawlbox():
    _run("CrawlBox", apt="git python", clone="https://github.com/Gameye98/CrawlBox",
         note="URL doğrulanmadı; gerekiyorsa düzeltin.")

def lfisuite():
    _run("LFISuite", apt="git python", clone="https://github.com/D35m0nd142/LFISuite",
         note="Python 2 gerektirir; arşivlenmiş durumda.")

def parsero():
    _run("Parsero", apt="git python", clone="https://github.com/beelze-br/parserso",
         note="Python 2 gerektirir; arşivlenmiş durumda.")

def sublist3r():
    _run("Sublist3r", apt="git python", clone="https://github.com/aboul3la/Sublist3r",
         cmd=f"cd {homeDir}/Sublist3r && pip install -r requirements.txt",
         start="python3 sublist3r.py -d <alan-adı>")

def wppluginscanner():
    _run("WP-plugin-scanner", apt="git python", clone="https://github.com/ChamalMP/WP-plugin-scanner",
         start="python3 wp_plugin_scanner.py <site>")

def whatweb():
    _run("WhatWeb", apt="whatweb", start="whatweb <hedef-url>")

def fuxploider():
    _run("fuxploider", apt="git python", clone="https://github.com/almandin/fuxploider",
         cmd=f"cd {homeDir}/fuxploider && pip install -r requirements.txt",
         start="python3 fuxploider.py --url <hedef-url>")

# ============ 04 - VERİTABANI DEĞERLENDİRMESİ ============
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
 # ============ 05 - PAROLA SALDIRILARI ============
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
    _run("Hydra", apt="tur-repo", cmd="apt install -y thc-hydra", start="hydra -h")

def black_hydra():
    _run("Black Hydra", apt="git tur-repo", clone="https://github.com/Gameye98/Black-Hydra",
         cmd="apt install -y thc-hydra")

def john():
    _run("John the Ripper", apt="john", start="john --help")

def hashcat():
    _run("hashcat", apt="hashcat", start="hashcat --help")

def cewl():
    _run("cewl", apt="cewl", start="cewl <hedef-url> -w wordlist.txt")

# ============ 06 - KABLOSUZ AĞ SALDIRILARI ============
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
         start=f"python2 {homeDir}/wifresti/wifresti.py")

# ============ 07 - TERSİNE MÜHENDİSLİK ============
def apktool():
    _run("Apktool", apt="apktool", start="apktool")

def jadx():
    _run("jadx", apt="jadx", start="jadx -d çıktı <apk>")

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

# ============ 08 - SÖMÜRÜ (EXPLOIT) ARAÇLARI ============
# (routersploit ve websploit zaten Parça 2'de tanımlı)
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

# ============ 09 - DİNLEME VE SAHTELEME ============
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

# ============ 10 - RAPORLAMA ARAÇLARI ============
def dradis():
    _run("Dradis", apt="git ruby", clone="https://github.com/dradis/dradis-ce",
         note="Ağır kurulum; Termux yerine Kali önerilir.")

def pipal():
    _run("Pipal", apt="git ruby", clone="https://github.com/digininja/pipal",
         start=f"ruby {homeDir}/pipal/pipal.rb <wordlist>")

def cherrytree():
    _run("CherryTree", apt="cherrytree", note="GUI gerektirir; Termux'ta çalışmaz.")

# ============ 11 - ADLİ BİLİŞİM ARAÇLARI ============
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
    _run("Foremost", apt="foremost", start="foremost -i <dosya> -o <çıktı-dizini>")

# ============ 12 - STRES TESTİ ============
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

# ============ 13 - LINUX DAĞITIMI KUR ============
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

# ============ 14 - TERMUX YARDIMCI ARAÇLARI ============
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

# ============ 15 - SHELL FONKSİYONU [.bashrc] ============
def bashrc():
    print("\n###### .bashrc güncelleniyor")
    _sh("echo \"alias la='ls -la'\" >> ~/.bashrc")
    _sh("echo \"alias ll='ls -l'\" >> ~/.bashrc")
    _sh("echo \"alias lzmx='cd ~/DarkTool && python DarkTool.py'\" >> ~/.bashrc")
    print('###### Tamamlandı')
    print("###### Aktifleştirmek için: source ~/.bashrc")
    backtomenu_option()

# ============ 16 - CLI OYUNLARI KUR ============
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

# ============ 17 - ZARARLI YAZILIM ANALİZİ ============
def clamav():
    _run("ClamAV", apt="clamav", start="clamscan <dosya>")

def rkhunter():
    _run("Rkhunter", apt="rkhunter", start="rkhunter --check")

def chkrootkit():
    _run("Chkrootkit", apt="chkrootkit", start="chkrootkit")

def lynis():
    _run("Lynis", apt="lynis", start="lynis audit system")

def yara():
    _run("YARA", apt="yara", start="yara <kural-dosyası> <hedef-dosya>")

def exiftool():
    _run("ExifTool", apt="exiftool", start="exiftool <dosya>")

def strings():
    _run("strings (binutils)", apt="binutils", start="strings <dosya>")

# ============ 18 - DERLEYİCİ/YORUMLAYICI ============
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

# ============ 19 - SOSYAL MÜHENDİSLİK ARAÇLARI ============
# (zphisher zaten Bölüm 01'de tanımlı)
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
    # ============ YASAL UYARI (EĞİTİM AMAÇLI) ============
def legal_warning():
    os.system("clear")
    print("""
  ⚠️  YASAL UYARI / SORUMLULUK REDDİ

  DarkTool YALNIZCA eğitim ve güvenlik araştırması amaçlıdır.
  Bu aracı yalnızca size ait veya yazılı izin aldığınız
  sistemlerde kullanın.

  Yetkisiz kullanım, bulunduğunuz ülkenin yasalarına göre
  SUÇ teşkil edebilir. Tüm sorumluluk kullanıcıya aittir.

  Geliştirici(ler) hiçbir zarar, veri kaybı veya hukuki
  yaptırımdan sorumlu tutulamaz.

  Bu aracı kullanarak bu koşulları kabul etmiş sayılırsınız.
""")
    input("  [Enter] ile devam et...")