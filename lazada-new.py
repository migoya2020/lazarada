import requests

reqUrl = "https://www.lazada.sg/catalog/?ajax=true&page=1&q=lego%2042121"

headersList = {
 "authority": "www.lazada.sg",
 "accept": "application/json, text/plain, */*",
 "accept-language": "en",
 "referer": "https://www.lazada.sg/catalog/?q=lego+42121",

 "sec-ch-ua-mobile": "?0",
 "sec-ch-ua-platform": "Linux",
 "sec-fetch-dest": "empty",
 "sec-fetch-mode": "cors",
 "sec-fetch-site": "same-origin",
 "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
 "x-csrf-token": "3175317a5580e",
 "x-requested-with": "XMLHttpRequest" 
}

payload = ""

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

print(response.json())