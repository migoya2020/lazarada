import requests
import time

def getCurrentEpochTime():
    milliseconds = int(round(time.time() * 1000))
    return milliseconds

x5sec_url = '''https://www.lazada.sg/catalog/_____tmd_____/slide?slidedata=%7B%22a%22%3A%22X82Y__be31bf05f5bc16c4a763907b48e1c0af%22%2C%22t%22%3A%2224cb9fab896eaeb862cd1e05be46c159%22%2C%22n%22%3A%22140%23aNrDwv1RzzFcYzo2LxXbwpN8s7a7F7PN6mbFvL7y%2F9YTnb4nX7k0elKp%2Bu1FXWt68W8PqD7E04hGOomnZ%2BODnZO1DCJqlbzxgegh%2BDrbzzcX3OaIlpTzzPzbVXlqlbrxbhUobpJXzFzY228%2BlpYAzMnDFaGLMZ2aMX4tjY1yIqph8Vr%2BlCpg0XKK92Q29QqY%2FkIUYgUz8C29yd5i5Vs32FnRHMtVtN8HQh4kR2ArM580B48Y3fzApuReOQjLN74Csgibm%2FPt9Kzn%2FLdQ5NTei1qy7FVHec60DXNl%2BnZ5FZUJCs94mnY87lf0fh56H9z6OWS%2BIIhUI1G7SLIS%2FobWtfm8g5zdtAgKidmpUaXbKhEMFnM%2Fu7%2Fj3lgEXsevQgNyYWbq1tNBI44CSzk8mIq1%2F0vxZvpWe%2B1piJUy1u4eNnrlDY5IOkqHelRMzF73ikWg4t8P9FemUHUxFTigg6S14ZSYM3a7KJEGjRmkqCHcSFx248wX1lqZ9jG4vBGBQaWhXo9kmcP8UW5%2FnlmG3j8Nq%2Ba3JrzEHoDFoDco4Y6BEYOl9ejE6dWCBl1W8lIqPGZfBFk0aDkb0e8o2ANIzEk9hGeCnqc26zLbZHbEQrk3uZObJGt0kMvTlYcozLOvUKTMB6RCD8PyIjVmieikc6poZna2B3EHHg6GZ7CHCtTJETSYuolj%2FxAtsKBBZSRCYh2Hs2O7MnLGbyHBp4apVlQI4nIGsSO8LmIyRXSWYqMotA%2FW%2BwlQoTqy%2F7E0qi3PzEMw1BAqjoBJCOApJPzQ5UZwkgHW98MoV3homlAoOmDML5ZSII2skFe9DkkvCr%2FhMoVwMxRwcxY9c31AebB0UWhosCJJnY1ZLU4TzGv4H4pQ4qLfv5OuSgamNFMHv52KixN%2FazfGNHGJjeOn%2FoRlCyneE5Qd9%2B8GW1dhIk4e%2BJrVO4%2Bga5KO9kRUMMRxzs5hU1TXmbcHCfzGbs%2FA5Nq0y6Xdkar%2BdrMLFv8NQjsr9yOO5QL%2FMDGILr4HO5p3BHgAwjmL9wQUyRHhCIS4WDGy6jw0NKNih74V%2BNGNflSO91glcgIiUnbZmSabCNUmVOOssOGXutq3GRXLIguSE2ULG09iZbMSlIU0GYTp0EMHCcwKsONznPm0W0MCfO6phHvqsdhC%2BtS5lnNhAHx4QbM%3D%22%2C%22p%22%3A%22%7B%5C%22ncSessionID%5C%22%3A%5C%225e701f057423%5C%22%2C%5C%22umidToken%5C%22%3A%5C%22T2gA4clYee1JZKc_ULNeXoubx4TNYndtv5Tybeb7jw8pXQTqcJ_m3QekFAuJZXokAhE%3D%5C%22%7D%22%2C%22scene%22%3A%22register%22%2C%22asyn%22%3A0%2C%22lang%22%3A%22en-gb%22%2C%22v%22%3A1030%7D&x5secdata=5e0c8e1365474455070961b803bd560607b52cabf5960afff39b64ce58073f78012dae8a376add8f7d5090538e1e563bcb80a1d11280bfd4955c983649d236c9a29fd306cf9530377c982eb362590715eb2bc16b1dbc91ea592f0222d32ec23f1976b91a091e5174a4153ee53f360b269783bbae415916f4e376d892cf8ccf5d68422032707df10bffe42dc58e5a993ec3a8710f61b3b110cf4807feb22670a85af0d5e9efd9d78f0b14f57ce89d43bc26b20b49197390b2a55838aad57f39894b2701c91176ab9378ab1b6e9fc20e13165dd37aa6138b58f4ee6dfa387d87305091dbdd424f20b7a856f5ca145d5d52a58e87f6675d10cea8c836ded2ef5e6fa6ef014b5cd3e16cef7ef1bf63dc1b1836cfd60bef24b7d07ed36b5b58fac926c04c413eb3797839fbf0772110cd4e2ced81c65bebf3b9df46dd6afed6f19989f1494fb2d4c59312a226c44ca7f0d2b36d15d396b4daa1bd48442c5700e2e892a63dc72832ff90b6a1db80083d777fa3fdd3eac5bf7400509807f07e67be6835393290f457efcaf0f68da47fb24ac2d780669346b0dc673bf393fa07750577e3fd8cb1124bff7824ce5ae2937043eb914afed865b37df553413632bda1176599157ba1015c766642213065164fbfbb56cf48ccfd368560bec378da3f1b4a07885aba8be5a6e7a473b86131b42a19d61f&v=034986025553421496'''

payload={}
headers1 = {
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
cust_cookie1='_uab_collina=162420906464852886455375; t_uid=dd1LzJIaYkuiQ2qD4w76tNGWBDqdu383; t_sid=AtvbWCF0BFxy5LNEYujErjyi9S0vs0YE; utm_channel=NA; cna=qGRWGaAGK1kCAcXoPfgWqu5o'
newCookie1 =cust_cookie1+"t_fv="+str(getCurrentEpochTime())+";"
headers1.update({"cookie":newCookie1})
res1 = requests.request("GET", x5sec_url, headers=headers1, data=payload)

print(res1.headers['bx-x5sec'].split(" ")[0].strip())
