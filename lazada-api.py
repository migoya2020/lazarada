import requests
import time
def getCurrentEpochTime():
    milliseconds = int(round(time.time() * 1000))
    return milliseconds
  
  
c = "https://acs-m.lazada.sg/h5/mtop.lazada.homepage.service/1.0/?jsv=2.6.1&appKey=24677475&t="+str(getCurrentEpochTime())+"&sign=fee81b0725078e0ab6d09be0c24df241&api=mtop.lazada.homepage.service&v=1.0&timeout=8000&x-i18n-language=en&x-i18n-regionID=SG&dataType=json&type=originaljson&data=%7B%22language%22%3A%22en-SG%22%2C%22regionID%22%3A%22SG%22%2C%22platform%22%3A%22pc%22%2C%22userID%22%3A%22%22%2C%22anonUID%22%3A%22c328b6f1fe06a9af1cf8fcf407f1aa80%22%2C%22deviceID%22%3A%22%22%2C%22voyagerVersion%22%3A%222%22%2C%22pageNo%22%3A0%2C%22isbackup%22%3Atrue%2C%22backupParams%22%3A%22language%2CregionID%2Cplatform%2CpageNo%22%2C%22pcSlot%22%3A%22200%22%2C%22mobileSlot%22%3A%22200%22%2C%22appId%22%3A%22icms-zebra-5000357-2586207%22%2C%22_pvuuid%22%3A1624228890397%2C%22terminalType%22%3A1%7D"

payload={}
headers = {
  'authority': 'acs-m.lazada.sg',
  'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
  'accept': 'application/json',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.51 Safari/537.36',
  'content-type': 'application/x-www-form-urlencoded',
  'origin': 'https://www.lazada.sg',
  'sec-fetch-site': 'same-site',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://www.lazada.sg/',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'hng=SG|en-SG|SGD|702; hng.sig=ryBKXOqZIsp9xOQ3YsZRgD7f-p0UaGB2pZ4BbZM8uEc; t_fv=1624217449634; t_uid=aPIbbcevLHMTiiPvWcmbnuJYpmRgdmgK; cna=VjhTGUJYOWsCAWmgDvmKudIZ; lzd_cid=738e586c-3347-483b-c1ee-a2004375b35b; lzd_sid=167b771a67e5e4f8c278d654c632b568; anon_uid=c328b6f1fe06a9af1cf8fcf407f1aa80; _tb_token_=e8653d553e41e; t_sid=3f6YVgPpSrJosRMPJlFF2MWYpiMqhJCn; _m_h5_tk=40ee0b33703778ea31c025c663331d78_1624236587634; _m_h5_tk_enc=6a71eb6ef6cc06619466ebeacad7358a; _gcl_au=1.1.781780803.1624227948; _fbp=fb.1.1624227949964.1578674430; xlly_s=1; utm_origin=https://www.google.com/; utm_channel=SEO; JSID=14bb0a0127df79a9f0c983d77b57aa25; CSRFT=76b555703ef1b; TID=3ed59d4fd79e81dc87346d866f02bd38; _lang=en_US; gmp_sid=-1; _uetsid=76cd2c60d21611eb9930a943abe1f140; _uetvid=5e998690d0fc11eb8076a7d36cd16c4b; tfstk=c3IdB3vWHqvCmOJO3wUgP5Uvb4SdZ6VJ1vOo2J50_EXu3wiRi2jcDrZQRLGpXRC..; l=eBTcUrdnjehNEdjjBOfwourza77OYIRAguPzaNbMiOCPO3fem-iPW6Onsg8wCnMNh6rDR3JmCf-TBeYBYI2FYSbYeCZxMjHmn; isg=BCwsf8cXYDBGUnQO0Xsdv5Ov_QNe5dCPfEMNlIZtZ1dMkcybrvcHHfYnsUEpGQjn; _tb_token_=ff534b3b5b1eb; anon_uid=043de4f40408e09259f946d3444ad461; lzd_sid=1725e8b009d858996398b9852e215ea7'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
