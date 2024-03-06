import requests
import json
NOTION_API_KEY = 'secret_RLHQMBg7eBvv8D1PraFdlzQ5hX9yyueD0RhkVH234XY'
DATABASE_ID = 'f996056e8d5a496789a8c3fb937a8855'
url = 'https://api.notion.com/v1/databases/'
# 请求头
headers = {
    'Authorization': f'Bearer {NOTION_API_KEY}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}
data ={
    "parent": {
        "type": "page_id",
        "page_id": DATABASE_ID
    },
    "icon": {
    	"type": "emoji",
			"emoji": "📝"
  	},
  	"cover": {
  		"type": "external",
    	"external": {
    		"url": "https://website.domain/images/image.png"
    	}
  	},
    "title": [
        {
            "type": "text",
            "text": {
                "content": "Grocery List",
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
        "In stock": {
            "checkbox": {}
        },
        "Food group": {
            "select": {
                "options": [
                    {
                        "name": "🥦Vegetable",
                        "color": "green"
                    },
                    {
                        "name": "🍎Fruit",
                        "color": "red"
                    },
                    {
                        "name": "💪Protein",
                        "color": "yellow"
                    }
                ]
            }
        },
        "Price": {
            "number": {
                "format": "dollar"
            }
        },
        "Last ordered": {
            "date": {}
        },
        "Store availability": {
            "type": "multi_select",
            "multi_select": {
                "options": [
                    {
                        "name": "Duc Loi Market",
                        "color": "blue"
                    },
                    {
                        "name": "Rainbow Grocery",
                        "color": "gray"
                    },
                    {
                        "name": "Nijiya Market",
                        "color": "purple"
                    },
                    {
                        "name": "Gus'\''s Community Market",
                        "color": "yellow"
                    }
                ]
            }
        },
        "+1": {
            "people": {}
        },
        "Photo": {
            "files": {}
        }
    }
}
# 发送 POST 请求
response = requests.post(url, headers=headers, data=json.dumps(data))

# 打印响应
print(response.text)