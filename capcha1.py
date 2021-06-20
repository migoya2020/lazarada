import requests

url = "https://cf.aliyun.com/nocaptcha/initialize.jsonp?a=&t=1624001109737202096957151624183196184179&scene=&lang=cn&v=v1.2.20&href=https%3A%2F%2Fwww.lazada.sg%2Fcatalog%2F&comm={}&callback=initializeJsonp_047983710768132326"

payload={}
headers = {
  'authority': 'cf.aliyun.com',
  'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.51 Safari/537.36',
  'accept': '*/*',
  'sec-fetch-site': 'cross-site',
  'sec-fetch-mode': 'no-cors',
  'sec-fetch-dest': 'script',
  'referer': 'https://www.lazada.sg/',
  'accept-language': 'en-US,en;q=0.9'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
initializeJsonp_047983710768132326({"success":true,"result":{"msg":"fail","success":false}});