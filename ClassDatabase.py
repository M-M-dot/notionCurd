import requests
import json
import random
import logging
import requests
from datetime import datetime
# 请求头
class DataBase: 
    def __init__(self,PAGE_ID,NOTION_API_KEY,dataBaseName,cellOptions,cover):
        self.NOTION_API_KEY = NOTION_API_KEY
        self.PageID = PAGE_ID
        self.url = 'https://api.notion.com/v1/databases/'
        self.headers = {
            'Authorization': f'Bearer {NOTION_API_KEY}',
            'Content-Type': 'application/json',
            'Notion-Version': '2022-06-28'
        }
        self.dataBaseName = dataBaseName
        respos = json.loads(self.createDatabase(cellOptions,cover))
        self.dataBaseID = respos["id"]

    ## 定义数据库
    def create_data(self,cellOptions,cover): 
        notion_colors = [
            "gray", "brown", "orange", "yellow", 
            "green", "blue", "purple", "pink", "red", 
        ]
        dictsli = []
        for t in cellOptions: 
            dicts = {"color":random.sample(notion_colors, 1)[0]}
            dicts["name"] = t 
            dictsli.append(dicts)
        print(dictsli)
        data = {
        "parent": {
            "type": "page_id",
            "page_id": PAGE_ID
        },
        "icon": {
            "type": "emoji",
                "emoji": "📝"
        },
        "cover": {
            "type": "external",
            "external": {
                "url": cover
            }
        },
        "title": [
            {
                "type": "text",
                "text": {
                    "content": self.dataBaseName,
                    "link": None
                }
            }
        ],
        "properties": {
            "Name": {
                "title": {}
            },
            "Description": {
                "rich_text": {}
            },
            "Date": {
                "date": {}
            },
            "cell type": {
                "type": "select",
                "select": {
                    "options": dictsli
                }
            }
        }
        }
        return data
    def createDatabase(self,cellOptions,cover):
        data = self.create_data(cellOptions,cover)
        # 发送 POST 请求
        response = requests.post(self.url, headers=self.headers, data=json.dumps(data))

        # 打印响应
        return response.text 

NOTION_API_KEY = 'secret_RLHQMBg7eBvv8D1PraFdlzQ5hX9yyueD0RhkVH234XY'
PAGE_ID = '4f0a58fb7bd94843b978ca9b6283157d'
dataBasenName="conclusion"
cover= "https://website.domain/images/image.png"
cellOptions = ["学习工作","社会经验","心情","身体","生活日常"]
database = DataBase(PAGE_ID,NOTION_API_KEY,dataBasenName,cellOptions,cover)

print(database.dataBaseID)
