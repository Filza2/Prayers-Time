from requests import get
import re,os

def header():
    os.system('cls' if os.name=='nt' else 'clear');print('''
╔═╗┬─┐┌─┐┬ ┬┌─┐┬─┐┌─┐  ╔╦╗┬┌┬┐┌─┐
╠═╝├┬┘├─┤└┬┘├┤ ├┬┘└─┐───║ ││││├┤ 
╩  ┴└─┴ ┴ ┴ └─┘┴└─└─┘   ╩ ┴┴ ┴└─┘

    By @Tweakpy - @vv1ck
''')

def url_encode(b):
    try:
        " url Encode from https://stackoverflow.com/a/74211299 "
        URL_RFC_3986={"!": "%21", "#": "%23", "$": "%24", "&": "%26", "'": "%27", "(": "%28", ")": "%29", "*": "%2A", "+": "%2B", ",": "%2C", "/": "%2F", ":": "%3A", ";": "%3B", "=": "%3D", "?": "%3F", "@": "%40", "[": "%5B", "]": "%5D",}
        if type(b)==bytes:b=b.decode(encoding="utf-8") 
        result=bytearray() 
        for i in b:
            if i in URL_RFC_3986:
                for j in URL_RFC_3986[i]:
                    result.append(ord(j))
                continue
            i=bytes(i, encoding="utf-8")
            if len(i)==1:result.append(ord(i))
            else:
                for c in i:
                    c=hex(c)[2:].upper()
                    result.append(ord("%"))
                    result.append(ord(c[0:1]))
                    result.append(ord(c[1:2]))
        result=result.decode(encoding="ascii")
        return result
    except Exception as e:return 0

def PrayerTimes(city):
    try:
        header()
        "https://aladhan.com - Aladhan API"
        "https://www.prayertimes.org"
        r=get(f'https://www.prayertimes.org/?city={url_encode(city) if url_encode(city)!=0 else exit("- Error ")}',headers={'Host': 'www.prayertimes.org','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Te': 'trailers','Connection': 'close'})
        if city in re.findall('<span class="label label-success">(.*?)</span>',r.text):
            data=re.findall("""<tr>
<td>(.*?)</td>
<td class="arial">(.*?)</td>
</tr>""",r.text)
            print(f"""- City : {re.findall('<span class="label label-success">(.*?)</span>',r.text)[0]}\n
- Adhan alfajr   : {data[0][1]}
- Adhan alshuroq : {data[1][1]}
- Adhan alzuhr   : {data[2][1]}
- Adhan alasr    : {data[3][1]}
- Adhan almagrib : {data[4][1]}
- Adhan alisha   : {data[5][1]}
""")
        else:exit('- Error , Check your City Name Or try again later ! ')
    except Exception as e:exit('- Error')
        
def Main():
    header()
    city=input('- Enter The Name of the City or Country : ').strip()# يمكنك ادخال الاسم عربي او انجليزي , You can enter the name in Arabic or English
    PrayerTimes(city)
    
    
    
    
    
    
    
    
Main()
