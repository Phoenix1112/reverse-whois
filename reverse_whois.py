import sys
import requests
import time
#programı aşağıdaki gibi çalıştır (tırnak içerisinde yazan ana domain adresinin "Registrant Organization" veya "Admin Organization" bölümünde yazan gerçek bilgisidir. diğer domainleri bu bilgiye göre match edecektir
#cat domains.txt | python3 reverse_whois.py "Uber Technologies, Inc."

try:
        for i in sys.stdin.read().split("\n"):
                if i:
                        time.sleep(3)
                        req = requests.get(f"https://who.is/whois/{i}", timeout=10)
                        if str(sys.argv[1]) in req.text:
                                print(i)
                        else:
                                req = requests.get(f"https://www.whois.com/whois/{i}", timeout=10)
                                if str(sys.argv[1]) in req.text:
                                        print(i)
except:
        pass
