import requests

url = "https://www.lazada.sg/catalog/?_keyori=ss&from=input&page=1&q=lego+super+heroes+76160&sort=priceasc"

payload={}
headers = {
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
  'cookie': 'hng=SG|en-SG|SGD|702; hng.sig=ryBKXOqZIsp9xOQ3YsZRgD7f-p0UaGB2pZ4BbZM8uEc; t_fv=1624217449634; t_uid=aPIbbcevLHMTiiPvWcmbnuJYpmRgdmgK; t_sid=UNHQS8zCa2n7YSeCzzx8KbIjHEcEDGAh; utm_channel=NA; cna=VjhTGUJYOWsCAWmgDvmKudIZ; x5sec=7b22617365727665722d6c617a6164613b32223a226130353063653665613630373638393936633666386131303038306331366234434f6d75766f5947454d5767702f4c682b2b4f6f377745776e4f484873674d3d227d; _tb_token_=ff534b3b5b1eb; anon_uid=043de4f40408e09259f946d3444ad461; lzd_sid=1725e8b009d858996398b9852e215ea7'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
