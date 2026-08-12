```python
def legal_warning():
    print("""
  ⚠️  YASAL UYARI
  Bu araç YALNIZCA eğitim ve güvenlik araştırması amaçlıdır.
  Yalnızca size ait veya yazılı izniniz olan sistemlerde kullanın.
  Yetkisiz kullanım suçtur; tüm sorumluluk kullanıcıya aittir.
  Geliştirici her türlü sorumluluğu reddeder.
""")
    input("  [Enter] ile devam et...")
    ## DarkTool.py - DarkTool v4.1 (güncellenmiş, Türkçe menü)
##
import os, sys
import readline
from time import sleep as timeout
from core.DarkCore import *

def parse_selection(sel):
    """'@' = tümünü kur, aksi halde boşlukla ayrılmış seçim listesi."""
    if sel == "@":
        return [str(x) for x in range(1, 201)]
    return sel.split()

def main():
    banner()
    legal_warning()
    print("   [01] Bilgi Toplama")
    print("   [02] Zafiyet Analizi")
    print("   [03] Web Hacking")
    print("   [04] Veritabanı Değerlendirmesi")
    print("   [05] Parola Saldırıları")
    print("   [06] Kablosuz Ağ Saldırıları")
    print("   [07] Tersine Mühendislik")
    print("   [08] Sömürü (Exploit) Araçları")
    print("   [09] Dinleme ve Sahteleme (Sniffing & Spoofing)")
    print("   [10] Raporlama Araçları")
    print("   [11] Adli Bilişim Araçları")
    print("   [12] Stres Testi")
    print("   [13] Linux Dağıtımı Kur")
    print("   [14] Termux Yardımcı Araçları")
    print("   [15] Shell Fonksiyonu [.bashrc]")
    print("   [16] CLI Oyunları Kur")
    print("   [17] Zararlı Yazılım Analizi")
    print("   [18] Derleyici/Yorumlayıcı")
    print("   [19] Sosyal Mühendislik Araçları")
    print("\n   [99] DarkTool'u Güncelle")
    print("   [00] DarkTool'tan Çık\n")
    DarkTool = input("lzmx > set_install ")

    # 01 - Bilgi Toplama
    if DarkTool.strip() == "1" or DarkTool.strip() == "01":
        print("\n    [01] Nmap: Ağ keşfi ve güvenlik denetimi için yardımcı program")
        print("    [02] Red Hawk: Bilgi Toplama, Zafiyet Taraması ve Gezinme (Crawling)")
        print("    [03] D-TECT: Penetrasyon Testi için Hepsi Bir Arada Araç")
        print("    [04] sqlmap: Otomatik SQL injection ve veritabanı ele geçirme aracı")
        print("    [05] Infoga: E-posta Hesap Bilgilerini Toplama Aracı")
        print("    [06] ReconDog: Bilgi Toplama ve Zafiyet Tarama Aracı")
        print("    [07] AndroZenmap")
        print("    [08] sqlmate: SQLmap'in arkadaşı; SQLmap'ten her zaman beklediğinizi yapar")
        print("    [09] AstraNmap: Bir bilgisayar ağındaki ana bilgisayarları ve hizmetleri bulmak için kullanılan güvenlik tarayıcısı")
        print("    [10] MapEye: Hassas GPS Konum Takibi (Android, IOS, Windows telefonlar)")
        print("    [11] Easymap: Nmap Kısayolu")
        print("    [12] BlackBox: Bir Penetrasyon Testi Çerçevesi (Framework)")
        print("    [13] XD3v: Telefonunuzla ilgili tüm temel ayrıntıları öğrenmenizi sağlayan güçlü araç")
        print("    [14] Crips: IP Adresleri, Web Sayfaları ve DNS kayıtları hakkında hızlıca bilgi almak için kullanılan çevrimiçi IP araçları koleksiyonu")
        print("    [15] SIR: Bir Skype Adının bilinen son IP'sini internetten çözer")
        print("    [16] EvilURL: IDN Homograph Saldırısı için unicode kötü amaçlı alan adları oluşturun ve bunları tespit edin")
        print("    [17] Striker: Keşif ve Zafiyet Tarama Paketi")
        print("    [18] Xshell: Araç Seti (ToolKit)")
        print("    [19] OWScan: OVID Web Tarayıcısı")
        print("    [20] OSIF: Açık Kaynak Facebook Bilgi Aracı")
        print("    [21] Devploit: Basit Bilgi Toplama Aracı")
        print("    [22] Namechk: namechk.com tabanlı; 100'den fazla web sitesi, forum ve sosyal ağda kullanıcı adlarını kontrol eden OSINT aracı")
        print("    [23] AUXILE: Web Uygulama Analizi Çerçevesi")
        print("    [24] inther: shodan, censys ve hackertarget kullanarak bilgi toplama")
        print("    [25] GINF: GitHub Bilgi Toplama Aracı")
        print("    [26] GPS Takibi")
        print("    [27] ASU: Facebook Hacking Araç Seti")
        print("    [28] fim: Facebook Görsel İndirici")
        print("    [29] MaxSubdoFinder: Alt Alan Adı (Subdomain) Keşfetme Aracı")
        print("    [30] pwnedOrNot: Ele Geçirilmiş E-posta Hesaplarının Parolalarını Bulmak için OSINT Aracı")
        print("    [31] Mac-Lookup: Belirli bir Mac adresi hakkında bilgi bulur")
        print("    [32] BillCipher: Bir Web Sitesi veya IP adresi için Bilgi Toplama aracı")
        print("    [33] dnsrecon: Güvenlik değerlendirmesi ve ağ sorun giderme")
        print("    [34] zphisher: Otomatik Oltalama (Phishing) Aracı")
        print("    [35] Mr.SIP: SIP Tabanlı Denetim ve Saldırı Aracı")
        print("    [36] Sherlock: Kullanıcı adıyla sosyal medya hesaplarını avlayın")
        print("    [37] userrecon: 75'ten fazla sosyal ağda kullanıcı adlarını bulun")
        print("    [38] PhoneInfoga: Yalnızca ücretsiz kaynaklar kullanarak telefon numaralarını taramak için en gelişmiş araçlardan biri")
        print("    [39] SiteBroker: Bilgi toplama ve penetrasyon testi otomasyonu için platformlar arası python tabanlı yardımcı program")
        print("    [40] maigret: Binlerce siteden kullanıcı adıyla bir kişi hakkında dosya toplayın")
        print("    [41] GatheTOOL: Bilgi Toplama - API hackertarget.com")
        print("    [42] ADB-ToolKit")
        print("    [43] TekDefense-Automater: Automater - IP URL ve MD5 OSINT Analizi")
        print("    [44] EagleEye: Arkadaşlarınızı takip edin. Görsel Tanıma ve Ters Görsel Arama kullanarak Instagram, FB ve Twitter profillerini bulun")
        print("    [45] EyeWitness: Web sitelerinin ekran görüntüsünü almak, sunucu başlık bilgisi sağlamak ve mümkünse varsayılan kimlik bilgilerini belirlemek için tasarlanmıştır")
        print("    [46] InSpy: Python tabanlı LinkedIn numaralandırma aracı")
        print("    [47] Leaked: Sızdırılmış Hash kodları, Parolalar ve E-postalar için kontrol aracı")
        print("    [48] fierce: Bitişik olmayan IP alanını bulmak için DNS keşif aracı")
        print("    [49] gasmask: Bilgi toplama aracı - OSINT")
        print("    [50] osi.ig: Bilgi Toplama (Instagram)")
        print("    [51] proxy-checker: İyi ve kötü proxy'leri kontrol eden basit betik")
        print("\n    [00] Ana menüye dön\n")
        infogathering = input("lzmx > set_install ")
        infogathering = parse_selection(infogathering)
        if len(infogathering) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for infox in infogathering:
            if infox.strip() == "01" or infox.strip() == "1": nmap()
            elif infox.strip() == "02" or infox.strip() == "2": red_hawk()
            elif infox.strip() == "03" or infox.strip() == "3": dtect()
            elif infox.strip() == "04" or infox.strip() == "4": sqlmap()
            elif infox.strip() == "05" or infox.strip() == "5": infoga()
            elif infox.strip() == "06" or infox.strip() == "6": reconDog()
            elif infox.strip() == "07" or infox.strip() == "7": androZenmap()
            elif infox.strip() == "08" or infox.strip() == "8": sqlmate()
            elif infox.strip() == "09" or infox.strip() == "9": astraNmap()
            elif infox.strip() == "10": mapeye()
            elif infox.strip() == "11": easyMap()
            elif infox.strip() == "12": blackbox()
            elif infox.strip() == "13": xd3v()
            elif infox.strip() == "14": crips()
            elif infox.strip() == "15": sir()
            elif infox.strip() == "16": evilURL()
            elif infox.strip() == "17": striker()
            elif infox.strip() == "18": xshell()
            elif infox.strip() == "19": owscan()
            elif infox.strip() == "20": osif()
            elif infox.strip() == "21": devploit()
            elif infox.strip() == "22": namechk()
            elif infox.strip() == "23": auxile()
            elif infox.strip() == "24": inther()
            elif infox.strip() == "25": ginf()
            elif infox.strip() == "26": gpstr()
            elif infox.strip() == "27": asu()
            elif infox.strip() == "28": fim()
            elif infox.strip() == "29": maxsubdofinder()
            elif infox.strip() == "30": pwnedOrNot()
            elif infox.strip() == "31": maclook()
            elif infox.strip() == "32": billcypher()
            elif infox.strip() == "33": dnsrecon()
            elif infox.strip() == "34": zphisher()
            elif infox.strip() == "35": mrsip()
            elif infox.strip() == "36": sherlock()
            elif infox.strip() == "37": userrecon()
            elif infox.strip() == "38": phoneinfoga()
            elif infox.strip() == "39": sitebroker()
            elif infox.strip() == "40": maigret()
            elif infox.strip() == "41": gathetool()
            elif infox.strip() == "42": adbtk()
            elif infox.strip() == "43": tekdefense()
            elif infox.strip() == "44": eagleeye()
            elif infox.strip() == "45": eyewitness()
            elif infox.strip() == "46": inspy()
            elif infox.strip() == "47": leaked()
            elif infox.strip() == "48": fierce()
            elif infox.strip() == "49": gasmask()
            elif infox.strip() == "50": osi_ig()
            elif infox.strip() == "51": proxy_checker()
            elif infox.strip() == "00" or infox.strip() == "0": restart_program()
            else: print("\nHATA: Geçersiz Giriş");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)

    # 02 - Zafiyet Analizi
    elif DarkTool.strip() == "2" or DarkTool.strip() == "02":
        print("\n    [01] Nmap: Ağ keşfi ve güvenlik denetimi için yardımcı program")
        print("    [02] AndroZenmap")
        print("    [03] AstraNmap: Bir bilgisayar ağındaki ana bilgisayarları ve hizmetleri bulmak için kullanılan güvenlik tarayıcısı")
        print("    [04] Easymap: Nmap Kısayolu")
        print("    [05] Red Hawk: Bilgi Toplama, Zafiyet Taraması ve Gezinme (Crawling)")
        print("    [06] D-TECT: Penetrasyon Testi için Hepsi Bir Arada Araç")
        print("    [07] Damn Small SQLi Scanner: 100 satırdan daha az kodla yazılmış, tam işlevsel bir SQL injection zafiyet tarayıcısı (GET ve POST parametrelerini destekler)")
        print("    [08] SQLiv: Devasa SQL injection zafiyet tarayıcısı")
        print("    [09] sqlmap: Otomatik SQL injection ve veritabanı ele geçirme aracı")
        print("    [10] sqlscan: Hızlı SQL Tarayıcı, Dorker, PHP Webshell enjektörü")
        print("    [11] Wordpresscan: Python ile yeniden yazılmış WPScan + bazı WPSeku fikirleri")
        print("    [12] WPScan: Ücretsiz wordPress güvenlik tarayıcısı")
        print("    [13] sqlmate: SQLmap'in arkadaşı; SQLmap'ten her zaman beklediğinizi yapar")
        print("    [14] termux-wordpresscan")
        print("    [15] TM-scanner: termux için web sitesi zafiyet tarayıcısı")
        print("    [16] Rang3r: Çoklu İş Parçacıklı (Multi Thread) IP + Port Tarayıcı")
        print("    [17] Striker: Keşif ve Zafiyet Tarama Paketi")
        print("    [18] Routersploit: Gömülü Cihazlar için Sömürü Çerçevesi (Exploitation Framework)")
        print("    [19] Xshell: Araç Seti (ToolKit)")
        print("    [20] SH33LL: Shell Tarayıcı")
        print("    [21] BlackBox: Bir Penetrasyon Testi Çerçevesi (Framework)")
        print("    [22] XAttacker: Web Sitesi Zafiyet Tarayıcısı ve Otomatik Sömürücü")
        print("    [23] OWScan: OVID Web Tarayıcısı")
        print("    [24] XPL-SEARCH: Birden fazla exploit veritabanında exploit arayın")
        print("    [25] AndroBugs_Framework: Geliştiricilerin veya hackerların Android uygulamalarındaki potansiyel güvenlik açıklarını bulmasına yardımcı olan verimli bir Android zafiyet tarayıcısı")
        print("    [26] Clickjacking-Tester: Web sitesinin clickjacking'e açık olup olmadığını kontrol etmek ve poc oluşturmak için tasarlanmış python betiği")
        print("    [27] Sn1per: Saldırı Yüzeyi Yönetim Platformu | Sn1perSecurity LLC")
        print("\n    [00] Ana menüye dön\n")
        vulnsys = input("lzmx > set_install ")
        vulnsys = parse_selection(vulnsys)
        if len(vulnsys) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for vulnx in vulnsys:   # DÜZELTME: orijinalde 'vulnsys' yazıyordu, çoklu seçim bozuktu
            if vulnx.strip() == "01" or vulnx.strip() == "1": nmap()
            elif vulnx.strip() == "02" or vulnx.strip() == "2": androZenmap()
            elif vulnx.strip() == "03" or vulnx.strip() == "3": astraNmap()
            elif vulnx.strip() == "04" or vulnx.strip() == "4": easyMap()
            elif vulnx.strip() == "05" or vulnx.strip() == "5": red_hawk()
            elif vulnx.strip() == "06" or vulnx.strip() == "6": dtect()
            elif vulnx.strip() == "07" or vulnx.strip() == "7": dsss()
            elif vulnx.strip() == "08" or vulnx.strip() == "8": sqliv()
            elif vulnx.strip() == "09" or vulnx.strip() == "9": sqlmap()
            elif vulnx.strip() == "10": sqlscan()
            elif vulnx.strip() == "11": wordpreSScan()
            elif vulnx.strip() == "12": wpscan()
            elif vulnx.strip() == "13": sqlmate()
            elif vulnx.strip() == "14": wordpresscan()
            elif vulnx.strip() == "15": tmscanner()
            elif vulnx.strip() == "16": rang3r()
            elif vulnx.strip() == "17": striker()
            elif vulnx.strip() == "18": routersploit()
            elif vulnx.strip() == "19": xshell()
            elif vulnx.strip() == "20": sh33ll()
            elif vulnx.strip() == "21": blackbox()
            elif vulnx.strip() == "22": xattacker()
            elif vulnx.strip() == "23": owscan()
            elif vulnx.strip() == "24": xplsearch()
            elif vulnx.strip() == "25": androbugs()
            elif vulnx.strip() == "26": clickjacking()
            elif vulnx.strip() == "27": sn1per()
            elif vulnx.strip() == "00" or vulnx.strip() == "0": restart_program()
            else: print("\nHATA: Geçersiz Giriş");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)

    # 03 - Web Hacking
    elif DarkTool.strip() == "3" or DarkTool.strip() == "03":
        print("\n    [01] sqlmap: Otomatik SQL injection ve veritabanı ele geçirme aracı")
        print("    [02] WebDAV: WebDAV Dosya Yükleme Sömürücüsü")
        print("    [03] MaxSubdoFinder: Alt Alan Adı (Subdomain) Keşfetme Aracı")
        print("    [04] Webdav Toplu Sömürü (Mass Exploit)")
        print("    [05] Atlas: Hızlı SQLMap Tamper Önerici")
        print("    [06] sqldump: sql sonuç sitelerini kolayca dökümle")
        print("    [07] Websploit: Gelişmiş bir MiTM Çerçevesi")
        print("    [08] sqlmate: SQLmap'in arkadaşı; SQLmap'ten her zaman beklediğinizi yapar")
        print("    [09] inther: shodan, censys ve hackertarget kullanarak bilgi toplama")
        print("    [10] HPB: HTML Sayfa Oluşturucu")
        print("    [11] Xshell: Araç Seti (ToolKit)")
        print("    [12] SH33LL: Shell Tarayıcı")
        print("    [13] XAttacker: Web Sitesi Zafiyet Tarayıcısı ve Otomatik Sömürücü")
        print("    [14] XSStrike: En gelişmiş XSS Tarayıcısı")
        print("    [15] Breacher: Gelişmiş çoklu iş parçacıklı admin paneli bulucu")
        print("    [16] OWScan: OVID Web Tarayıcısı")
        print("    [17] ko-dork: Basit zafiyetli web tarayıcısı")
        print("    [18] ApSca: Güçlü web penetrasyon uygulaması")
        print("    [19] amox: Sözlük saldırısıyla sitede yerleşik backdoor veya shell bulun")
        print("    [20] FaDe: kindeditor, fckeditor ve webdav ile sahte deface")
        print("    [21] AUXILE: Auxile Çerçevesi")
        print("    [22] xss-payload-list: Siteler Arası Betik (XSS) Zafiyet Payload Listesi")
        print("    [23] Xadmin: Admin Panel Bulucu")
        print("    [24] CMSeeK: CMS Algılama ve Sömürme Paketi - WordPress, Joomla, Drupal ve 180'den fazla diğer CMS'i tarayın")
        print("    [25] CMSmap: En popüler CMS'lerin güvenlik kusurlarını tespit etme sürecini otomatikleştiren python açık kaynak CMS tarayıcısı")
        print("    [26] CrawlBox: Web dizinini kaba kuvvetle (brute-force) denemenin kolay yolu")
        print("    [27] LFISuite: Tamamen Otomatik LFI Sömürücü (+ Reverse Shell) ve Tarayıcı")
        print("    [28] Parsero: Robots.txt denetim aracı")
        print("    [29] Sn1per: Saldırı Yüzeyi Yönetim Platformu | Sn1perSecurity LLC")
        print("    [30] Sublist3r: Penetrasyon testçileri için hızlı alt alan adı numaralandırma aracı")
        print("    [31] WP-plugin-scanner: WordPress tabanlı bir web sitesinde yüklü eklentileri listeleme aracı")
        print("    [32] WhatWeb: Yeni nesil web tarayıcı")
        print("    [33] fuxploider: Dosya yükleme zafiyeti tarayıcısı ve sömürme aracı")
        print("\n    [00] Ana menüye dön\n")
        webhack = input("lzmx > set_install ")
        webhack = parse_selection(webhack)
        if len(webhack) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for webhx in webhack:
            if webhx.strip() == "01" or webhx.strip() == "1": sqlmap()
            elif webhx.strip() == "02" or webhx.strip() == "2": webdav()
            elif webhx.strip() == "03" or webhx.strip() == "3": maxsubdofinder()
            elif webhx.strip() == "04" or webhx.strip() == "4": webmassploit()
            elif webhx.strip() == "05" or webhx.strip() == "5": atlas()
            elif webhx.strip() == "06" or webhx.strip() == "6": sqldump()
            elif webhx.strip() == "07" or webhx.strip() == "7": websploit()
            elif webhx.strip() == "08" or webhx.strip() == "8": sqlmate()
            elif webhx.strip() == "09" or webhx.strip() == "9": inther()
            elif webhx.strip() == "10": hpb()
            elif webhx.strip() == "11": xshell()
            elif webhx.strip() == "12": sh33ll()
            elif webhx.strip() == "13": xattacker()
            elif webhx.strip() == "14": xsstrike()
            elif webhx.strip() == "15": breacher()
            elif webhx.strip() == "16": owscan()
            elif webhx.strip() == "17": kodork()
            elif webhx.strip() == "18": apsca()
            elif webhx.strip() == "19": amox()
            elif webhx.strip() == "20": fade()
            elif webhx.strip() == "21": auxile()
            elif webhx.strip() == "22": xss_payload_list()
            elif webhx.strip() == "23": xadmin()
            elif webhx.strip() == "24": cmseek()
            elif webhx.strip() == "25": cmsmap()
            elif webhx.strip() == "26": crawlbox()
            elif webhx.strip() == "27": lfisuite()
            elif webhx.strip() == "28": parsero()
            elif webhx.strip() == "29": sn1per()
            elif webhx.strip() == "30": sublist3r()
            elif webhx.strip() == "31": wppluginscanner()
            elif webhx.strip() == "32": whatweb()
            elif webhx.strip() == "33": fuxploider()
            elif webhx.strip() == "00" or webhx.strip() == "0": restart_program()
            else: print("\nHATA: Geçersiz Giriş");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)

    # 04 - Veritabanı Değerlendirmesi
    elif DarkTool.strip() == "4" or DarkTool.strip() == "04":
        print("\n    [01] DbDat: DbDat, bir veritabanının güvenliğini değerlendirmek için çok sayıda kontrol gerçekleştirir")
        print("    [02] sqlmap: Otomatik SQL injection ve veritabanı ele geçirme aracı")
        print("    [03] NoSQLMap: Otomatik NoSQL veritabanı numaralandırma ve web uygulaması sömürme aracı")
        print("    [04] audit_couchdb: CouchDB sunucusundaki büyük veya küçük güvenlik sorunlarını tespit edin")
        print("    [05] mongoaudit: MongoDB örneklerinizin düzgün şekilde korunup korunmadığını öğrenmenizi sağlayan otomatik pentesting aracı")
        print("\n    [00] Ana menüye dön\n")
        dbssm = input("lzmx > set_install ")
        dbssm = parse_selection(dbssm)
        if len(dbssm) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for dbsx in dbssm:
            if dbsx.strip() == "01" or dbsx.strip() == "1": dbdat()
            elif dbsx.strip() == "02" or dbsx.strip() == "2": sqlmap()
            elif dbsx.strip() == "03" or dbsx.strip() == "3": nosqlmap()
            elif dbsx.strip() == "04" or dbsx.strip() == "4": audit_couchdb()
            elif dbsx.strip() == "05" or dbsx.strip() == "5": mongoaudit()
            elif dbsx.strip() == "00" or dbsx.strip() == "0": restart_program()
            else: print("\nHATA: Geçersiz Giriş");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)

    # 05 - Parola Saldırıları
    elif DarkTool.strip() == "5" or DarkTool.strip() == "05":
        print("\n    [01] Cupp: Profil bilgilerine göre akıllı ve güçlü wordlist üretir")
        print("    [02] Hash-Buster: Hash türünü bulur ve kırar")
        print("    [03] InstaHack: Instagram hesap güvenlik testi aracı")
        print("    [04] indonesian-wordlist: Endonezya wordlist koleksiyonu")
        print("    [05] Facebook Brute Force: Facebook kaba kuvvet aracı (3)")
        print("    [06] Hydra: Birçok servisi destekleyen giriş kırıcı (logon cracker)")
        print("    [07] Black Hydra: Facebook hesapları için kaba kuvvet aracı")
        print("    [08] John the Ripper: Parola denetimi ve kurtarma aracı")
        print("    [09] hashcat: Dünyanın en hızlı ve en gelişmiş parola kurtarma aracı")
        print("    [10] cewl: Web sitesinden özel wordlist üretme aracı")
        print("\n    [00] Ana menüye dön\n")
        passatk = input("lzmx > set_install ")
        passatk = parse_selection(passatk)
        if len(passatk) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for passx in passatk:
            if passx.strip() == "01" or passx.strip() == "1": cupp()
            elif passx.strip() == "02" or passx.strip() == "2": hash_buster()
            elif passx.strip() == "03" or passx.strip() == "3": instaHack()
            elif passx.strip() == "04" or passx.strip() == "4": indonesian_wordlist()
            elif passx.strip() == "05" or passx.strip() == "5": fbBrute()
            elif passx.strip() == "06" or passx.strip() == "6": hydra()
            elif passx.strip() == "07" or passx.strip() == "7": black_hydra()
            elif passx.strip() == "08" or passx.strip() == "8": john()
            elif passx.strip() == "09" or passx.strip() == "9": hashcat()
            elif passx.strip() == "10": cewl()
            elif passx.strip() == "00" or passx.strip() == "0": restart_program()
            else: print("\nHATA: Geçersiz Giriş");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)

    # 06 - Kablosuz Ağ Saldırıları
    elif DarkTool.strip() == "6" or DarkTool.strip() == "06":
        print("\n    [01] Aircrack-ng: Kablosuz ağ denetim paketi")
        print("    [02] Wifite2: Otomatik wifi saldırı aracı")
        print("    [03] Fluxion: Sosyal mühendislik tabanlı WPA/WPA2 saldırı aracı")
        print("    [04] Wifiphisher: Rogue AP ile wifi kimlik avı aracı")
        print("    [05] Pixiewps: WPS offline pin saldırı aracı")
        print("    [06] Reaver: WPS kaba kuvvet aracı")
        print("    [07] mdk3/mdk4: Kablosuz ağ DoS ve saldırı aracı")
        print("    [08] Airgeddon: Çok fonksiyonlu wifi denetim betiği")
        print("    [09] Fern Wifi Cracker: GUI wifi güvenlik denetim aracı")
        print("    [10] Wifresti: WiFi şifre kurtarma aracı")
        print("\n    [00] Ana menüye dön\n")
        wireles = input("lzmx > set_install ")
        wireles = parse_selection(wireles)
        if len(wireles) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for wirex in wireles:
            if wirex.strip() == "01" or wirex.strip() == "1": aircrack()
            elif wirex.strip() == "02" or wirex.strip() == "2": wifite2()
            elif wirex.strip() == "03" or wirex.strip() == "3": fluxion()
            elif wirex.strip() == "04" or wirex.strip() == "4": wifiphisher()
            elif wirex.strip() == "05" or wirex.strip() == "5": pixiewps()
            elif wirex.strip() == "06" or wirex.strip() == "6": reaver()
            elif wirex.strip() == "07" or wirex.strip() == "7": mdk3()
            elif wirex.strip() == "08" or wirex.strip() == "8": airgeddon()
            elif wirex.strip() == "09" or wirex.strip() == "9": fern()
            elif wirex.strip() == "10": wifresti()
            elif wirex.strip() == "00" or wirex.strip() == "0": restart_program()
            else: print("\nHATA: Geçersiz Giriş");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)

    # 07 - Tersine Mühendislik
    elif DarkTool.strip() == "7" or DarkTool.strip() == "07":
        print("\n    [01] Apktool: APK decode/rebuild aracı")
        print("    [02] jadx: Java/APK decompiler (DEX -> Java kaynak kodu)")
        print("    [03] dex2jar: DEX dosyalarını JAR'a çevirir")
        print("    [04] Bytecode Viewer: Çoklu decompiler GUI aracı")
        print("    [05] smali/baksmali: DEX assembler/disassembler")
        print("    [06] APKLeaks: APK'dan gizli anahtar ve URI tarama")
        print("\n    [00] Ana menüye dön\n")
        revers = input("lzmx > set_install ")
        revers = parse_selection(revers)
        if len(revers) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for revx in revers:
            if revx.strip() == "01" or revx.strip() == "1": apktool()
            elif revx.strip() == "02" or revx.strip() == "2": jadx()
            elif revx.strip() == "03" or revx.strip() == "3": dex2jar()
            elif revx.strip() == "04" or revx.strip() == "4": bytecode_viewer()
            elif revx.strip() == "05" or revx.strip() == "5": smali()
            elif revx.strip() == "06" or revx.strip() == "6": apkleaks()
            elif revx.strip() == "00" or revx.strip() == "0": restart_program()
            else: print("\nHATA: Geçersiz Giriş");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)

    # 08 - Sömürü (Exploit) Araçları
    elif DarkTool.strip() == "8" or DarkTool.strip() == "08":
        print("\n    [01] Metasploit: Penetrasyon testi framework'ü")
        print("    [02] Commix: Komut enjeksiyonu otomatik sömürü aracı")
        print("    [03] Routersploit: Gömülü cihaz sömürü framework'ü")
        print("    [04] Websploit: Gelişmiş MiTM framework'ü")
        print("    [05] SearchSploit: Exploit-DB yerel arama aracı")
        print("    [06] BeEF: Tarayıcı sömürü framework'ü")
        print("    [07] Evilginx2: Phishing için reverse proxy aracı")
        print("\n    [00] Ana menüye dön\n")
        exploit = input("lzmx > set_install ")
        exploit = parse_selection(exploit)
        if len(exploit) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for explx in exploit:
            if explx.strip() == "01" or explx.strip() == "1": metasploit()
            elif explx.strip() == "02" or explx.strip() == "2": commix()
            elif explx.strip() == "03" or explx.strip() == "3": routersploit()
            elif explx.strip() == "04" or explx.strip() == "4": websploit()
            elif explx.strip() == "05" or explx.strip() == "5": searchsploit()
            elif explx.strip() == "06" or explx.strip() == "6": beef()
            elif explx.strip() == "07" or explx.strip() == "7": evilginx2()
            elif explx.strip() == "00" or explx.strip() == "0": restart_program()
            else: print("\nHATA: Geçersiz Giriş");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)

    # 09 - Dinleme ve Sahteleme
    elif DarkTool.strip() == "9" or DarkTool.strip() == "09":
        print("\n    [01] Wireshark: Ağ protokol analizörü")
        print("    [02] tcpdump: Komut satırı paket yakalayıcı")
        print("    [03] Ettercap: MiTM saldırı paketi")
        print("    [04] Bettercap: Gelişmiş ağ saldırı ve izleme framework'ü")
        print("    [05] dsniff: Ağ dinleme araç koleksiyonu")
        print("    [06] MITMproxy: HTTPS için etkileşimli MiTM proxy")
        print("    [07] Macchanger: MAC adresi değiştirici")
        print("    [08] Netool: MiTM araç kutusu")
        print("\n    [00] Ana menüye dön\n")
        sniff = input("lzmx > set_install ")
        sniff = parse_selection(sniff)
        if len(sniff) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for snfx in sniff:
            if snfx.strip() == "01" or snfx.strip() == "1": wireshark()
            elif snfx.strip() == "02" or snfx.strip() == "2": tcpdump()
            elif snfx.strip() == "03" or snfx.strip() == "3": ettercap()
            elif snfx.strip() == "04" or snfx.strip() == "4": bettercap()
            elif snfx.strip() == "05" or snfx.strip() == "5": dsniff()
            elif snfx.strip() == "06" or snfx.strip() == "6": mitmproxy()
            elif snfx.strip() == "07" or snfx.strip() == "7": macchanger()
            elif snfx.strip() == "08" or snfx.strip() == "8": netool()
            elif snfx.strip() == "00" or snfx.strip() == "0": restart_program()
            else: print("\nHATA: Geçersiz Giriş");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)

    # 10 - Raporlama Araçları
    elif DarkTool.strip() == "10":
        print("\n    [01] Dradis: Penetrasyon testi raporlama framework'ü")
        print("    [02] Pipal: Parola analiz ve istatistik aracı")
        print("    [03] CherryTree: Not alma ve raporlama aracı")
        print("\n    [00] Ana menüye dön\n")
        report = input("lzmx > set_install ")
        report = parse_selection(report)
        if len(report) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for repx in report:
            if repx.strip() == "01" or repx.strip() == "1": dradis()
            elif repx.strip() == "02" or repx.strip() == "2": pipal()
            elif repx.strip() == "03" or repx.strip() == "3": cherrytree()
            elif repx.strip() == "00" or repx.strip() == "0": restart_program()
            else: print("\nHATA: Geçersiz Giriş");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)

    # 11 - Adli Bilişim Araçları
    elif DarkTool.strip() == "11":
        print("\n    [01] Autopsy: Disk görüntüsü adli analiz aracı")
        print("    [02] Guymager: Disk görüntüleme aracı")
        print("    [03] dc3dd: Gelişmiş dd kopyalama aracı")
        print("    [04] ddrescue: Kurtarma odaklı disk kopyalama aracı")
        print("    [05] Binwalk: Firmware analiz aracı")
        print("    [06] Foremost: Silinmiş dosya kurtarma aracı")
        print("\n    [00] Ana menüye dön\n")
        forensic = input("lzmx > set_install ")
        forensic = parse_selection(forensic)
        if len(forensic) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for forx in forensic:
            if forx.strip() == "01" or forx.strip() == "1": autopsy()
            elif forx.strip() == "02" or forx.strip() == "2": guymager()
            elif forx.strip() == "03" or forx.strip() == "3": dc3dd()
            elif forx.strip() == "04" or forx.strip() == "4": ddrescue()
            elif forx.strip() == "05" or forx.strip() == "5": binwalk()
            elif forx.strip() == "06" or forx.strip() == "6": foremost()
            elif forx.strip() == "00" or forx.strip() == "0": restart_program()
            else: print("\nHATA: Geçersiz Giriş");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)

    # 12 - Stres Testi
    elif DarkTool.strip() == "12":
        print("\n    [01] Torshammer: Tor tabanlı HTTP DoS aracı")
        print("    [02] Slowloris: Yavaş HTTP DoS aracı")
        print("    [03] GoldenEye: HTTP DoS aracı")
        print("    [04] Xerxes: Hızlı HTTP DoS aracı")
        print("    [05] Planetwork-DDOS: Basit DDoS aracı")
        print("    [06] HULK: HTTP kaba kuvvet DoS aracı")
        print("    [07] Fl00d ve Fl00d2: Flood saldırı betikleri")
        print("\n    [00] Ana menüye dön\n")
        stress = input("lzmx > set_install ")
        stress = parse_selection(stress)
        if len(stress) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for strx in stress:
            if strx.strip() == "01" or strx.strip() == "1": torshammer()
            elif strx.strip() == "02" or strx.strip() == "2": slowloris()
            elif strx.strip() == "03" or strx.strip() == "3": goldeneye()
            elif strx.strip() == "04" or strx.strip() == "4": xerxes()
            elif strx.strip() == "05" or strx.strip() == "5": planetwork_ddos()
            elif strx.strip() == "06" or strx.strip() == "6": hulk()
            elif strx.strip() == "07" or strx.strip() == "7": fl00d12()
            elif strx.strip() == "00" or strx.strip() == "0": restart_program()
            else: print("\nHATA: Geçersiz Giriş");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)

    # 13 - Linux Dağıtımı Kur
    elif DarkTool.strip() == "13":
        print("\n    [01] Kali Nethunter: Kali araçlarını Termux'a kurar")
        print("    [02] Ubuntu: proot-distro ile Ubuntu")
        print("    [03] Debian: proot-distro ile Debian")
        print("    [04] Parrot OS: proot-distro ile Parrot")
        print("    [05] BlackArch: proot-distro ile BlackArch")
        print("    [06] Alpine: proot-distro ile Alpine")
        print("\n    [00] Ana menüye dön\n")
        distro = input("lzmx > set_install ")
        distro = parse_selection(distro)
        if len(distro) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for disx in distro:
            if disx.strip() == "01" or disx.strip() == "1": nethunter()
            elif disx.strip() == "02" or disx.strip() == "2": ubuntu()
            elif disx.strip() == "03" or disx.strip() == "3": debian()
            elif disx.strip() == "04" or disx.strip() == "4": parrot()
            elif disx.strip() == "05" or disx.strip() == "5": blackarch()
            elif disx.strip() == "06" or disx.strip() == "6": alpine()
            elif disx.strip() == "00" or disx.strip() == "0": restart_program()
            else: print("\nHATA: Geçersiz Giriş");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)

    # 14 - Termux Yardımcı Araçları
    elif DarkTool.strip() == "14":
        print("\n    [01] Termux-API: Telefon donanım API erişimi")
        print("    [02] Neofetch: Sistem bilgi ekranı")
        print("    [03] htop: Etkileşimli süreç yöneticisi")
        print("    [04] cmatrix: Matrix efekti")
        print("    [05] sl: Yanlış 'ls' için tren animasyonu")
        print("    [06] figlet: ASCII sanat yazı üretici")
        print("    [07] toilet: Renkli ASCII sanat yazı üretici")
        print("    [08] rxfetch: Hafif sistem bilgi aracı")
        print("    [09] screenfetch: Sistem bilgi aracı")
        print("\n    [00] Ana menüye dön\n")
        termutil = input("lzmx > set_install ")
        termutil = parse_selection(termutil)
        if len(termutil) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for tutx in termutil:
            if tutx.strip() == "01" or tutx.strip() == "1": termux_api()
            elif tutx.strip() == "02" or tutx.strip() == "2": neofetch()
            elif tutx.strip() == "03" or tutx.strip() == "3": htop()
            elif tutx.strip() == "04" or tutx.strip() == "4": cmatrix()
            elif tutx.strip() == "05" or tutx.strip() == "5": sl()
            elif tutx.strip() == "06" or tutx.strip() == "6": figlet()
            elif tutx.strip() == "07" or tutx.strip() == "7": toilet()
            elif tutx.strip() == "08" or tutx.strip() == "8": rxfetch()
            elif tutx.strip() == "09" or tutx.strip() == "9": screenfetch()
            elif tutx.strip() == "00" or tutx.strip() == "0": restart_program()
            else: print("\nHATA: Geçersiz Giriş");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)

    # 15 - Shell Fonksiyonu [.bashrc]
    elif DarkTool.strip() == "15":
        print("\n    [01] bashrc: .bashrc dosyasına yararlı alias ve fonksiyonlar ekler")
        print("\n    [00] Ana menüye dön\n")
        bashrcx = input("lzmx > set_install ")
        bashrcx = parse_selection(bashrcx)
        if len(bashrcx) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for bashx in bashrcx:
            if bashx.strip() == "01" or bashx.strip() == "1": bashrc()
            elif bashx.strip() == "00" or bashx.strip() == "0": restart_program()
            else: print("\nHATA: Geçersiz Giriş");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)

    # 16 - CLI Oyunları Kur
    elif DarkTool.strip() == "16":
        print("\n    [01] Moon-Buggy: Araç sürme oyunu")
        print("    [02] Ninvaders: Uzay istilacıları oyunu")
        print("    [03] Pacman4Console: Terminalde Pac-Man oyunu")
        print("    [04] nSnake: Terminalde yılan oyunu")
        print("    [05] Greed: Terminal tabanlı yemek toplama oyunu")
        print("    [06] Bastet: Terminalde tetris oyunu")
        print("    [07] vitetris: Terminalde tetris oyunu (2)")
        print("\n    [00] Ana menüye dön\n")
        cligame = input("lzmx > set_install ")
        cligame = parse_selection(cligame)
        if len(cligame) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for clix in cligame:
            if clix.strip() == "01" or clix.strip() == "1": moonbuggy()
            elif clix.strip() == "02" or clix.strip() == "2": ninvaders()
            elif clix.strip() == "03" or clix.strip() == "3": pacman()
            elif clix.strip() == "04" or clix.strip() == "4": nsnake()
            elif clix.strip() == "05" or clix.strip() == "5": greed()
            elif clix.strip() == "06" or clix.strip() == "6": bastet()
            elif clix.strip() == "07" or clix.strip() == "7": vitetris()
            elif clix.strip() == "00" or clix.strip() == "0": restart_program()
            else: print("\nHATA: Geçersiz Giriş");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)

    # 17 - Zararlı Yazılım Analizi
    elif DarkTool.strip() == "17":
        print("\n    [01] ClamAV: Açık kaynak antivirüs motoru")
        print("    [02] Rkhunter: Rootkit tespit aracı")
        print("    [03] Chkrootkit: Yerel rootkit tespit aracı")
        print("    [04] Lynis: Güvenlik denetim aracı")
        print("    [05] YARA: Zararlı yazılım desen eşleştirme aracı")
        print("    [06] ExifTool: Meta veri okuma/yazma aracı")
        print("    [07] strings (binutils): İkili dosyalardan okunabilir dizeleri çıkarır")
        print("\n    [00] Ana menüye dön\n")
        malware = input("lzmx > set_install ")
        malware = parse_selection(malware)
        if len(malware) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for mlwx in malware:
            if mlwx.strip() == "01" or mlwx.strip() == "1": clamav()
            elif mlwx.strip() == "02" or mlwx.strip() == "2": rkhunter()
            elif mlwx.strip() == "03" or mlwx.strip() == "3": chkrootkit()
            elif mlwx.strip() == "04" or mlwx.strip() == "4": lynis()
            elif mlwx.strip() == "05" or mlwx.strip() == "5": yara()
            elif mlwx.strip() == "06" or mlwx.strip() == "6": exiftool()
            elif mlwx.strip() == "07" or mlwx.strip() == "7": strings()
            elif mlwx.strip() == "00" or mlwx.strip() == "0": restart_program()
            else: print("\nHATA: Geçersiz Giriş");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)

    # 18 - Derleyici/Yorumlayıcı
    elif DarkTool.strip() == "18":
        print("\n    [01] Python 3: Yorumlayıcı (genellikle önceden kuruludur)")
        print("    [02] Node.js: JavaScript çalışma ortamı")
        print("    [03] Clang/GCC: C/C++ derleyici")
        print("    [04] Ruby: Yorumlayıcı")
        print("    [05] PHP: Yorumlayıcı")
        print("    [06] Perl: Yorumlayıcı")
        print("    [07] Go: Derleyici")
        print("    [08] Rust: Derleyici")
        print("    [09] OpenJDK: Java JDK")
        print("    [10] Lua: Yorumlayıcı")
        print("    [11] Kotlin: Derleyici")
        print("\n    [00] Ana menüye dön\n")
        compilex = input("lzmx > set_install ")
        compilex = parse_selection(compilex)
        if len(compilex) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for cmp_x in compilex:
            if cmp_x.strip() == "01" or cmp_x.strip() == "1": python3()
            elif cmp_x.strip() == "02" or cmp_x.strip() == "2": nodejs()
            elif cmp_x.strip() == "03" or cmp_x.strip() == "3": clang()
            elif cmp_x.strip() == "04" or cmp_x.strip() == "4": ruby()
            elif cmp_x.strip() == "05" or cmp_x.strip() == "5": php()
            elif cmp_x.strip() == "06" or cmp_x.strip() == "6": perl()
            elif cmp_x.strip() == "07" or cmp_x.strip() == "7": golang()
            elif cmp_x.strip() == "08" or cmp_x.strip() == "8": rust()
            elif cmp_x.strip() == "09" or cmp_x.strip() == "9": openjdk()
            elif cmp_x.strip() == "10": lua()
            elif cmp_x.strip() == "11": kotlin()
            elif cmp_x.strip() == "00" or cmp_x.strip() == "0": restart_program()
            else: print("\nHATA: Geçersiz Giriş");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)

    # 19 - Sosyal Mühendislik Araçları
    elif DarkTool.strip() == "19":
        print("\n    [01] SocialFish: Instagram ve GitHub için kimlik avı aracı")
        print("    [02] HiddenEye: Gelişmiş kimlik avı aracı")
        print("    [03] Shellphish: Sosyal medya kimlik avı araçları")
        print("    [04] SayCheese: Kamera açan kimlik avı sayfası")
        print("    [05] MaskPhish: URL maskeleme aracı")
        print("    [06] BlackEye: Kimlik avı site üretici")
        print("    [07] Zphisher: Otomatik oltalama aracı (güncel)")
        print("\n    [00] Ana menüye dön\n")
        social = input("lzmx > set_install ")
        social = parse_selection(social)
        if len(social) > 1:
            writeStatus(1)
        else:
            writeStatus(0)
        for socx in social:
            if socx.strip() == "01" or socx.strip() == "1": socialfish()
            elif socx.strip() == "02" or socx.strip() == "2": hiddeneye()
            elif socx.strip() == "03" or socx.strip() == "3": shellphish()
            elif socx.strip() == "04" or socx.strip() == "4": saycheese()
            elif socx.strip() == "05" or socx.strip() == "5": maskphish()
            elif socx.strip() == "06" or socx.strip() == "6": blackeye()
            elif socx.strip() == "07" or socx.strip() == "7": zphisher()
            elif socx.strip() == "00" or socx.strip() == "0": restart_program()
            else: print("\nHATA: Geçersiz Giriş");timeout(1);restart_program()
        if readStatus():
            writeStatus(0)

    # 99 - DarkTool'u Güncelle
    elif DarkTool.strip() == "99":
        print("\nDarkTool güncelleniyor...")
        update_DarkTool()

    # 00 - Çıkış
    elif DarkTool.strip() == "00" or DarkTool.strip() == "0":
        sys.exit()

    else:
        print("\nHATA: Geçersiz Giriş")
        timeout(1)
        restart_program()

if __name__ == "__main__":
    main()