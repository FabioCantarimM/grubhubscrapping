import requests
import json
from entity.Restaurant import Restaurant



def getAuth():
    url = 'https://api-gtm.grubhub.com/auth'

    payload = json.dumps({
        'brand': 'GRUBHUB',
        'client_id': 'beta_UmWlpstzQSFmocLy3h1UieYcVST',
        'device_id': 1260388942,
        'refresh_token': '250ec8d6-0446-465d-a262-e4de1d51635c'
    })

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8',
        'origin' : 'https://www.grubhub.com',
        'referer': 'https://www.grubhub.com/',
        'Accept' : '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'accept-language': 'en-US,en;q=0.9,pt;q=0.8',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
    }

    try:
        req = requests.request('POST', url, headers=headers, data=payload).json()
    except requests.exceptions.HTTPError as e:
        print (e.response.text)

    return req['session_handle']['access_token']
    

def getData( storeId:int, auth:str):
    url= f'https://api-gtm.grubhub.com/restaurants/{storeId}?version=4&variationId=rtpFreeItems&orderType=standard&locationMode=delivery'

    headers = {
        'authorization': f'Bearer {auth}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'content-type': 'application/json;charset=UTF-8',
        'origin' : 'https://www.grubhub.com',
        'referer': 'https://www.grubhub.com/',
        'Accept' : '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'accept-language': 'en-US,en;q=0.9,pt;q=0.8',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
    }
    
    req = requests.request('GET', url, headers=headers).json()

    storeInfos = {
        'storeId': req['restaurant']['id'],
        'name': req['restaurant']['name'],
        'address': req['restaurant']['address']['street_address'],
        'city': req['restaurant']['address']['locality'],
        'state': req['restaurant']['address']['region'],
        'category': req['restaurant']['cuisines'],
        'stars': req['restaurant']['rating']['rating_value'],
        'review_count': req['restaurant']['rating']['rating_count'],
        }

    menuItems = []
    menuSubItems = []

    for menu in req['restaurant']['menu_category_list']:
        for item in menu['menu_item_list']:
            elem = {
                'id': item.get('id'),
                'category_name': item['menu_category_name'],
                'item_name': item['name'],
                'item_description': item['description'],
                'item_price': item['price']['amount'],
            }
            menuItems.append(elem)
            for choice in item['choice_category_list']:
                options = []
                for option in choice['choice_option_list']:
                    item = {
                        'option_name': option['description'],
                        'option_price': option['price']['amount']
                    }
                    options.append(item)
                choice = {
                    'product_id': elem['id'],
                    'modifier_id': choice['id'],
                    'group_name': choice['name'],
                    'modifier_min': choice['min_choice_options'],
                    'modifier_max': choice['max_choice_options'],
                    'options': options
                }
                menuSubItems.append(choice)
                
    return Restaurant(storeInfos, menuItems, menuSubItems)

storeId = 2809951
auth = getAuth()
store = getData(storeId, auth) 
print(store.watch());
