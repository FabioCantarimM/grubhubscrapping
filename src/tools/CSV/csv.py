import csv
import os
from entity.Restaurant import Restaurant

def getFileName(rest: Restaurant, add: str):
    return f"files/{rest['info']['storeId']}_{add}.csv"

def getHeaders(rest: Restaurant, section: str):
    return list(rest[section][0].keys())

def createFile(data: Restaurant):
    nameMenu = getFileName(data, 'menu')
    nameOption = getFileName(data, 'options')
    headersMenu = getHeaders(data, 'menu')
    headersOption = getHeaders(data, 'option')
    make_sure_path_exists("files")
    with open(nameMenu, 'w', encoding='UTF8') as f:
            writer = csv.DictWriter(f, fieldnames=headersMenu, delimiter='|',  dialect=csv.excel_tab)
            writer.writeheader()
            writer.writerows(data["menu"])
    with open(nameOption, 'w', encoding='UTF8') as f:
            writer = csv.DictWriter(f, fieldnames=headersOption, delimiter='|',  dialect=csv.excel_tab)
            writer.writeheader()
            writer.writerows(data["option"])
    
    return {
        "storeId": data["info"]["storeId"],
        "name": data["info"]["name"],
        "menuPath": nameMenu,
        "optionFilePath": nameOption
    }



def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if not os.path.isdir(path):
            raise