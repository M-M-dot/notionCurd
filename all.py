from ClassDatabase import DataBase
from datetime import datetime
from ClassNewPage import PageDatabase
from ClassTransfer import Page
NOTION_API_KEY = 'secret_RLHQMBg7eBvv8D1PraFdlzQ5hX9yyueD0RhkVH234XY'

PAGE_ID = '4f0a58fb7bd94843b978ca9b6283157d' #database 所在的pageid 
dataBasenName="conclusion"
cover= "https://website.domain/images/image.png"
cellOptions = ["学习工作","社会经验","心情","身体","生活日常"]
database = DataBase(PAGE_ID,NOTION_API_KEY,dataBasenName,cellOptions,cover)
DatabaseID = database.dataBaseID

SoucePAGE_ID = '15b8fc30-fee2-4afe-8658-ed0e5b0c03dc'
transfer = Page(PAGE_ID,NOTION_API_KEY)
keys,values,dates = transfer.get_page_content(cellOptions,False)
print(len(keys)==len(values))
print(len(dates)==len(values))
respos = transfer.insert_into_database(DatabaseID,keys,values,dates)
