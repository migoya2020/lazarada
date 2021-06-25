import requests
import time
import random
from random import randint
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import urllib.parse
from time import sleep
from openpyxl.workbook import Workbook

finaldata = []

def getCurrentEpochTime():
    milliseconds = int(round(time.time() * 1000))
    return milliseconds

def getCollina():
    collina = int(round(time.time() * 100000000000000))
    return collina
ses = requests.Session()
mmstat = "https://gm.mmstat.com/fsp.1.1"
headers0 = {'user-agent': 'Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393',
            'accept-language': 'en-GB,en;q=0.5',
            'accept-encoding': 'gzip, deflate, br',
            'content-type': 'text/plain;charset=UTF-8',
            'content-length': '958',
            'origin': 'https://www.lazada.sg',
            'referer': 'https://www.lazada.sg/',
            'te': 'trailers'}
REQUESTBODY = b'{"gmkey":"OTHER","gokey":"c1=24cb9fab896eaeb862cd1e05be46c159&delay=0&hash=&last_pos=0%252C0&msg=Daraz-mm-web%2520%25E9%25A1%25B5%25E9%259D%25A2-%25E9%25AA%258C%25E8%25AF%2581%25E7%25A0%2581&page=https%253A%252F%252Fwww.lazada.sg%252Fcatalog%252F&patch_ver=-&pid=punish-page&query=_keyori%253Dss%2526from%253Dinput%2526page%253D1%2526q%253Dlego%252520super%252520heroes%25252076160%2526sort%253Dpriceasc&raw_ua=Mozilla%252F5.0%2520(Windows%2520NT%25206.0%253B%2520Win64%253B%2520x64)%2520AppleWebKit%252F537.36%2520(KHTML%252C%2520like%2520Gecko)%2520Chrome%252F51.0.2704.79%2520Safari%252F537.36%2520Edge%252F14.14393&referrer=&rel=&scr=1920x1080&spm_a=&spm_b=&title=&tracker_ver=4.0.0&type=11&ua=Mozilla%252F5.0%2520(Windows%2520NT%25206.0%253B%2520Win64%253B%2520x64)%2520AppleWebKit%252F537.36%2520(KHTML%252C%2520like%2520Gecko)%2520Chrome%252F51.0.2704.79%2520Safari%252F537.36%2520Edge%252F14.14393&uid=24cb9fab896eaeb862cd1e05be46c159","logtype":"2"}'
res0 = ses.post(mmstat, headers=headers0, data=REQUESTBODY)
# print(res0.headers)
sca = res0.cookies.get('sca')

url1 = 'https://sg.mmstat.com/v.gif?logtype=1&title=Sorry%2C%20we%20have%20detected%20unusual%20traffic%20from%20your%20network.&pre=&scr=1920x1080&_p_url=https%3A%2F%2Fwww.lazada.sg%2Fcatalog%2F%3F_keyori%3Dss%26from%3Dinput%26page%3D1%26q%3Dlego%2Bsuper%2Bheroes%2B76160%26sort%3Dpriceasc&spm-cnt=0.0.0.0.12ea720bk56Fp8&category=&uidaplus=&aplus&yunid=&&trid=0b1195ac16242090565304668e18a4&asid=AQAAAACgds9gAG8WOQAAAAB6nRh1hY3K2Q==&p=1&o=winVista&b=edge14&s=1920x1080&w=edge&ism=pc&cache=f1950f8&lver=8.15.6&jsver=aplus_std&pver=0.7.11&ps_i=AtvbWCF0BFxy5LNEYujErjyi9S0vs0YE&pc_i=dd1LzJIaYkuiQ2qD4w76tNGWBDqdu383&_p_ref=&_p_usertype=new&utm_channel=NA&ab_cookie=&_p_meta_desc=&_p_meta_robots=&_p_canonical=&tag=0&stag=-2&lstag=-1&_slog=0'
headers0.update({"cookie": sca})
# headers0.update({"cookie": cna})
aptResp = ses.get(url1, headers=headers0)
atpsida = aptResp.cookies.get('atpsida')
cna = aptResp.cookies.get('cna')

apt2_url = 'https://sg.mmstat.com/v.gif?logtype=1&title=lego%20super%20heroes%2076160%20-%20Buy%20lego%20super%20heroes%2076160%20at%20Best%20Price%20in%20Singapore%20%7C%20www.lazada.sg&pre=https%3A%2F%2Fwww.lazada.sg%2Fcatalog%2F%3F_keyori%3Dss%26from%3Dinput%26page%3D1%26q%3Dlego%2Bsuper%2Bheroes%2B76160%26sort%3Dpriceasc&scr=1920x1080&_p_url=https%3A%2F%2Fwww.lazada.sg%2Fcatalog%2F%3F_keyori%3Dss%26from%3Dinput%26page%3D1%26q%3Dlego%2Bsuper%2Bheroes%2B76160%26sort%3Dpriceasc&cna='+cna + \
    '&spm-cnt=a2o42.searchlist.0.0.12ea5675du9NP3&cfgver=1.0&aplus&asid=AQAAAAA67xdgHA3hZAAAAAAcxAAg7RzJQg==&p=1&o=winVista&b=edge14&s=1920x1080&w=edge&ism=pc&cache=ead245&lver=8.15.6&jsver=aplus_int&pver=0.7.11&ps_i=AtvbWCF0BFxy5LNEYujErjyi9S0vs0YE&pc_i=dd1LzJIaYkuiQ2qD4w76tNGWBDqdu383&lzd_pg_type=search&_p_lang=en&_p_ref=&lzd_layout=desktop&_s_engine=HA3&_p_usertype=new&_s_bucket_id=v0&_s_reqNo=30020a5d0d3952278b4f0b68ed0aa250&_s_resultNr=7&_s_internal_term=lego%20super%20heroes%2076160&_s_internal_type=Search%20Results&_s_filters=&utm_channel=NA&undefined=undefined&ab_cookie=&_p_meta_desc=lego%20super%20heroes%2076160%20Singapore%20-%20Shop%20for%20best%20lego%20super%20heroes%2076160%20online%20at%20www.lazada.sg&_p_meta_robots=index%2Cfollow&_p_canonical=https%3A%2F%2Fwww.lazada.sg%2Fcatalog%2F&_hng=SG%257Cen-SG%257CSGD%257C702&tag=1&stag=-1&lstag=-1&_slog=0'
headers0.update({"cookie": "sca="+sca+";"+"atpsida="+atpsida+";"})
apt2Res = ses.get(apt2_url, headers=headers0)
# print(apt2Res.cookies.items())

x5sec_url = '''https://www.lazada.sg/catalog/_____tmd_____/slide?slidedata=%7B%22a%22%3A%22X82Y__be31bf05f5bc16c4a763907b48e1c0af%22%2C%22t%22%3A%2224cb9fab896eaeb862cd1e05be46c159%22%2C%22n%22%3A%22140%23aNrDwv1RzzFcYzo2LxXbwpN8s7a7F7PN6mbFvL7y%2F9YTnb4nX7k0elKp%2Bu1FXWt68W8PqD7E04hGOomnZ%2BODnZO1DCJqlbzxgegh%2BDrbzzcX3OaIlpTzzPzbVXlqlbrxbhUobpJXzFzY228%2BlpYAzMnDFaGLMZ2aMX4tjY1yIqph8Vr%2BlCpg0XKK92Q29QqY%2FkIUYgUz8C29yd5i5Vs32FnRHMtVtN8HQh4kR2ArM580B48Y3fzApuReOQjLN74Csgibm%2FPt9Kzn%2FLdQ5NTei1qy7FVHec60DXNl%2BnZ5FZUJCs94mnY87lf0fh56H9z6OWS%2BIIhUI1G7SLIS%2FobWtfm8g5zdtAgKidmpUaXbKhEMFnM%2Fu7%2Fj3lgEXsevQgNyYWbq1tNBI44CSzk8mIq1%2F0vxZvpWe%2B1piJUy1u4eNnrlDY5IOkqHelRMzF73ikWg4t8P9FemUHUxFTigg6S14ZSYM3a7KJEGjRmkqCHcSFx248wX1lqZ9jG4vBGBQaWhXo9kmcP8UW5%2FnlmG3j8Nq%2Ba3JrzEHoDFoDco4Y6BEYOl9ejE6dWCBl1W8lIqPGZfBFk0aDkb0e8o2ANIzEk9hGeCnqc26zLbZHbEQrk3uZObJGt0kMvTlYcozLOvUKTMB6RCD8PyIjVmieikc6poZna2B3EHHg6GZ7CHCtTJETSYuolj%2FxAtsKBBZSRCYh2Hs2O7MnLGbyHBp4apVlQI4nIGsSO8LmIyRXSWYqMotA%2FW%2BwlQoTqy%2F7E0qi3PzEMw1BAqjoBJCOApJPzQ5UZwkgHW98MoV3homlAoOmDML5ZSII2skFe9DkkvCr%2FhMoVwMxRwcxY9c31AebB0UWhosCJJnY1ZLU4TzGv4H4pQ4qLfv5OuSgamNFMHv52KixN%2FazfGNHGJjeOn%2FoRlCyneE5Qd9%2B8GW1dhIk4e%2BJrVO4%2Bga5KO9kRUMMRxzs5hU1TXmbcHCfzGbs%2FA5Nq0y6Xdkar%2BdrMLFv8NQjsr9yOO5QL%2FMDGILr4HO5p3BHgAwjmL9wQUyRHhCIS4WDGy6jw0NKNih74V%2BNGNflSO91glcgIiUnbZmSabCNUmVOOssOGXutq3GRXLIguSE2ULG09iZbMSlIU0GYTp0EMHCcwKsONznPm0W0MCfO6phHvqsdhC%2BtS5lnNhAHx4QbM%3D%22%2C%22p%22%3A%22%7B%5C%22ncSessionID%5C%22%3A%5C%225e701f057423%5C%22%2C%5C%22umidToken%5C%22%3A%5C%22T2gA4clYee1JZKc_ULNeXoubx4TNYndtv5Tybeb7jw8pXQTqcJ_m3QekFAuJZXokAhE%3D%5C%22%7D%22%2C%22scene%22%3A%22register%22%2C%22asyn%22%3A0%2C%22lang%22%3A%22en-gb%22%2C%22v%22%3A1030%7D&x5secdata=5e0c8e1365474455070961b803bd560607b52cabf5960afff39b64ce58073f78012dae8a376add8f7d5090538e1e563bcb80a1d11280bfd4955c983649d236c9a29fd306cf9530377c982eb362590715eb2bc16b1dbc91ea592f0222d32ec23f1976b91a091e5174a4153ee53f360b269783bbae415916f4e376d892cf8ccf5d68422032707df10bffe42dc58e5a993ec3a8710f61b3b110cf4807feb22670a85af0d5e9efd9d78f0b14f57ce89d43bc26b20b49197390b2a55838aad57f39894b2701c91176ab9378ab1b6e9fc20e13165dd37aa6138b58f4ee6dfa387d87305091dbdd424f20b7a856f5ca145d5d52a58e87f6675d10cea8c836ded2ef5e6fa6ef014b5cd3e16cef7ef1bf63dc1b1836cfd60bef24b7d07ed36b5b58fac926c04c413eb3797839fbf0772110cd4e2ced81c65bebf3b9df46dd6afed6f19989f1494fb2d4c59312a226c44ca7f0d2b36d15d396b4daa1bd48442c5700e2e892a63dc72832ff90b6a1db80083d777fa3fdd3eac5bf7400509807f07e67be6835393290f457efcaf0f68da47fb24ac2d780669346b0dc673bf393fa07750577e3fd8cb1124bff7824ce5ae2937043eb914afed865b37df553413632bda1176599157ba1015c766642213065164fbfbb56cf48ccfd368560bec378da3f1b4a07885aba8be5a6e7a473b86131b42a19d61f&v=034986025553421496'''
headers2 = {
    'authority': 'www.lazada.sg',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.51 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.lazada.sg/catalog/?_keyori=ss&from=input&page=1&q=lego+super+heroes+76160&sort=priceasc',
    'accept-language': 'en-US,en;q=0.9',

}
cust_cookie1 = '_uab_collina='+str(getCollina())+'; t_uid=AMlBY7RwkC08GohRMxCItbSLPr2fb5Yk; t_sid=Zy04Rqzam1vINdiRukB6cDxysdpXi4Rr; utm_channel=NA; cna='+cna
newCookie1 = cust_cookie1+"t_fv="+str(getCurrentEpochTime())+";"+"cna="+cna+";"
headers2.update({"cookie": newCookie1})
res1 = requests.request("GET", x5sec_url, headers=headers2)

x5sec = res1.cookies.get('x5sec')

# print(x5sec)
# print(res1.content)
csr_url = "https://member.lazada.sg/user/api/getCsrfToken"
headers2.update({'referer':csr_url})
headers2.update({'cookie':'_uab_collina='+str(getCollina())+'; t_fv='+str(getCurrentEpochTime())+'; t_uid=AMlBY7RwkC08GohRMxCItbSLPr2fb5Yk; '+'cna='+cna+"; "+'t_sid=Zy04Rqzam1vINdiRukB6cDxysdpXi4Rr; '+'x5sec='+x5sec})
res2 = ses.get(csr_url, headers=headers2)
tb_token = res2.cookies['_tb_token_']
anon_id = res2.cookies['anon_uid']
lzd_sid = res2.cookies['lzd_sid']

cust_cookie2 = 't_uid=AMlBY7RwkC08GohRMxCItbSLPr2fb5Yk;cna='+cna+'; hng=SG|en-SG|SGD|702;client_type=desktop;'
newCookie2 = cust_cookie2+"_tb_token_="+tb_token+";"+"anon_uid="+anon_id+";"+"lzd_sid=" + \
    lzd_sid+";"+"t_fv="+str(getCurrentEpochTime()) + \
    ";"+"Domain=.lazada.sg; Path=/;"+x5sec


url = "https://www.lazada.sg/catalog/?_keyori=ss&from=input&page=1&q=lego+super+heroes+76160&sort=priceasc"

payload = {}
headers3 = {
    'authority': 'www.lazada.sg',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.51 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.lazada.sg/catalog/?_keyori=ss&from=input&page=1&q=lego+super+heroes+76160&sort=priceasc',
    'accept-language': 'en-US,en;q=0.9'

}
headers3.update({"cookie": newCookie2})

keywords = [
            'lego 42121',
            'lego 76160',
            # 'lego 76191',
            # 'lego 71372',
            # 'lego 10941',
            # 'lego 11013',
            # 'lego 76383',
            # 'lego 10951',
            # 'lego 41936',
            # 'lego 42123',
            # 'lego 43191',
            # 'lego 60287',
            # 'lego 60291',
            # 'lego 60304',
            # 'lego 71736',
            # 'lego 31115',
            # 'lego 76901',
            # 'lego 11001',
            # 'lego 10872',
            # 'lego 10920',
            # 'lego 10915',
            # 'lego 75551',
            # 'lego 71742',
            # 'lego 71360',
            # 'lego 71368',
            # 'lego 76165'
            ]
def getProductsDetails(keywords):
    for keyword in keywords:
        keyword_index =keywords.index(keyword)+1
        # print('Index', index)
        keyword_data =[]
        
        try:
            new_string = urllib.parse.quote_plus(keyword)
            keyword_url ='https://www.lazada.sg/catalog/?page=1&?q='+str(new_string)+'&sort=priceasc'
            
            headers3.update({'referer':keyword_url})
            final_response = requests.request("GET", keyword_url, headers=headers3, data=payload)
            print("working on Keyword: ",keyword)
            sleep(10)
            # print(final_response.text)
            soup = BeautifulSoup(final_response.content, "html.parser")
            scripts = soup.select("script")
            pageResults = None
            for script_tag in scripts:
                if "window.pageData" in str(script_tag):
                    pageData = str(script_tag).replace("<script>", "").replace(
                        "</script>", "").replace("window.pageData =", "").rsplit(";", 1)[0].strip()
                    pageData_json = json.loads(pageData)
                    # print(pageData_json)
                    pageResults= pageData_json['mods']["listItems"]
                else:
                    pass
            listItems = pageResults
            for item in listItems:
                try:
                    item["originalPriceShow"]
                    originalPrice = item['originalPriceShow']
                except:
                    originalPrice = 0
                try:
                    item["discount"]
                    discount = item["discount"]
                except:
                    discount = 0
                # keyword_data.append({"sku":keyword_index,"prod_Name": item["name"],"Keyword":keyword, "prod_Id": item["nid"], "prod_url": item["productUrl"],
                #             "image": item["image"], "priceShow": item["priceShow"], "originalPrice": originalPrice, "discount": discount})
                keyword_data.append({"sku":keyword_index,"prod_Name": item["name"],"Keyword":keyword, "noOfResults": len(listItems),"lowestPrice": item["priceShow"]})
            prices=[x["lowestPrice"].split("$")[1].strip() for x in keyword_data]
            # print(min(prices))
            price_index =prices.index(min(prices))
            finaldata.append(keyword_data[price_index])
            
        except:
            raise RuntimeError (f"There has been an error..")
    return

getProductsDetails(keywords)

final_df = pd.DataFrame(finaldata)
final_df.to_excel("lazada-sg-products.xlsx", index=False)
print("We are Done ... ")
