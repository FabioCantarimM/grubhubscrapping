obj = {
    "name": "Fabio Melo",
    "age": 34,
    "address": {
        "streetname": "Willis Roberto Banks",
        "streetnumber": 549,
        "moreInfos": "81c"
    }
}


test = {
    "name": obj.get("name"),
    "ruas": obj.get("address").get("streetname")
}


print(test);