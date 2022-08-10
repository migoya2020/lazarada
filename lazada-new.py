from time import sleep
import requests
import urllib.parse
import pandas as pd


target_keywords = []
finaldata = []


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



def prepairKeywords(file_name:str):
    keywords_df = pd.read_excel(file_name, sheet_name='Sheet1')
    mylist =keywords_df.to_dict('records')
    print("keyword: ", mylist[0])
    target_keywords.extend(mylist)
    print("Total Keywords :", len(mylist))
    return

def getProductsDetails(keywords):
    for keyword in keywords:
        try:
            new_string = urllib.parse.quote(keyword['keyword'])
            # new_string = urllib.parse.quote('lego 10951')
            reqUrl = "https://www.lazada.sg/catalog/?ajax=true&page=1&q="+new_string+"&sort=priceasc"
            print("working on keyword: ",keyword['keyword'])
            
            final_response = requests.request("GET", reqUrl, headers=headersList)
            print(final_response)
            sleep(6)
            pageResults=final_response.json()            
            # assert len(listItems) !=None, "Results items in Zero"
            if pageResults is not  None:
                try:
                    listItems=pageResults['mods']['listItems']
                    print("Total results: ", len(listItems))
                    lowest_price_item = listItems[0]                                       
                    # finaldata.append({"Sku":product['sku'],'Name': product['name'],"Keyword":keyword,"No_Of_Results": len(listItems),"Product_Name": lowest_price_item["name"], "Lowest_Price": lowest_price_item["priceShow"]})
                    finaldata.append({"Sku":keyword['sku'],'Name': keyword['name'],"Keyword":keyword['keyword'],"No_Of_Results": len(listItems),"Product_Name": lowest_price_item["name"], "Lowest_Price": lowest_price_item["priceShow"]})           
                except:
                    print("Total results: ", 0)
                    finaldata.append({"Sku":keyword['sku'],'Name': keyword['name'],"Keyword":keyword['keyword'],"No_Of_Results": 'n/a',"Product_Name": 'n/a', "Lowest_Price": 'n/a'})
                    
        except(Exception) as error:    
            print("Error: ",error) 
            print(final_response.content) 
            # convert the results into excel file
            final_df = pd.DataFrame(finaldata)
            final_df.to_excel("lazada-sg-products.xlsx", index=False)      
            raise RuntimeError (f"There has been an error.. Check output file for what we have collected so far.")

    return


prepairKeywords(file_name='Keyword_lego.xlsx')
getProductsDetails(target_keywords)



