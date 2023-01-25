from entity.Restaurant import Restaurant
from crawlers.GrubHub import GrubHub

storeId = 2809951
ghcrawler = GrubHub
auth = ghcrawler.getAuth()
store = ghcrawler.getData(storeId, auth) 
print(store.watch());
