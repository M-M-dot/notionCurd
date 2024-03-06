import requests
import json

class PageDatabase: 
  def __init__(self,database_id):
    self.NOTION_API_KEY = 'secret_RLHQMBg7eBvv8D1PraFdlzQ5hX9yyueD0RhkVH234XY'
    self.DATABASE_ID = database_id
    self.url = 'https://api.notion.com/v1/pages'
    self.headers = {
    'Authorization': f'Bearer {self.NOTION_API_KEY}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
    }

  def addPagedata(self,date,key,rich_texts): 
        # 发送 POST 请求
    page = self.constructDBPageData(date,key,rich_texts)
    response = requests.post(self.url, headers=self.headers, data=json.dumps(page))
    # 打印响应
    return(response.text)
  def constructDBPageData(self,date,key,rich_texts):
    data = {
      "parent": { 
            "database_id": self.DATABASE_ID },
      "icon": {
        "emoji": "🥬"
      },
      "properties": {
          "Name":{
            "title": [
                {
                    "type": "text",
                    "text": {
                    "content": f"{key}"
                    }
                }
                ]	
      },
    "Description":{"rich_text":rich_texts
      },
      "cell type": {
          "select": {
              "name": f"{key}",
                }
            },       
      "Date": {
              "date": {
                    "start": date
              } 
            },
      
      }
    }
    return data
