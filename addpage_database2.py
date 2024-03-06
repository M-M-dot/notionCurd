import requests
import json
NOTION_API_KEY = 'secret_RLHQMBg7eBvv8D1PraFdlzQ5hX9yyueD0RhkVH234XY'
DATABASE_ID = 'aee0c26b6a6e45719b1dfc1a4b7bbdc4'
url = 'https://api.notion.com/v1/pages'
# 请求头
headers = {
    'Authorization': f'Bearer {NOTION_API_KEY}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}

data = {
	"parent": { 
        "database_id": DATABASE_ID },
  "icon": {
  	"emoji": "🥬"
  },
	"cover": {
		"external": {
			"url": "https://upload.wikimedia.org/wikipedia/commons/6/62/Tuscankale.jpg"
		}
	},
  "properties": {
      "Name":{
        "title": [
            {
                "type": "text",
                "text": {
                "content": "The title2"
                }
            }
            ]	
  },
  "Price" :{
    "number": 1234
  },
        "Description":{"rich_text":[{'type': 'text', 'text': {'content': '学习工作总结： ', 'link': None}, 'annotations': {'bold': True, 'italic': False, 'strikethrough': False, 'underline': False, 'code': False, 'color': 'default'}, 'plain_text': '学习工作总结： ', 'href': None}, {'type': 'text', 'text': {'content': 'chatgpt 有一个插件可以侧边栏。', 'link': None}, 'annotations': {'bold': False, 'italic': False, 'strikethrough': False, 'underline': False, 'code': False, 'color': 'default'}, 'plain_text': 'chatgpt 有一个插件可以侧边栏。', 'href': None}, {'type': 'text', 'text': {'content': '希望能够连接小程序，然后在小程序上将每次的总结，写入我的notion中。公众号也可以吧。', 'link': None}, 'annotations': {'bold': False, 'italic': False, 'strikethrough': False, 'underline': False, 'code': False, 'color': 'default'}, 'plain_text': '希望能够连接小程序，然后在小程序上将每次的总结，写入我的notion中。公众号也可以吧。', 'href': None}, {'type': 'text', 'text': {'content': '但是手头更紧急的事情似乎还没有开始干。 ', 'link': None}, 'annotations': {'bold': False, 'italic': False, 'strikethrough': False, 'underline': False, 'code': False, 'color': 'default'}, 'plain_text': '但是手头更紧急的事情似乎还没有开始干。 ', 'href': None}]
  },
    "In stock": {
            "checkbox": True
        },
         "Food group": {
            "select": {
    			"name": "🥦Vegetable",
            }
        },        "Last ordered": {
             "date": {
      "start": "2021-05-11T11:00:00.000-04:00"
    }
        },
                "Store availability": {
                "multi_select": [
      {
        "name": "Duc Loi Market"
      },
      {
        "name": "Rainbow Grocery"
      }
    ]
        },"Photo": {
            "files":  [
      {
        "type": "external",
        "name": "Space Wallpaper",
        "external": {
          	"url": "https://website.domain/images/space.png"
        }
      }
    ]},},

	"children": [
		{
			"object": "block",
			"type": "heading_2",
			"heading_2": {
				"rich_text": [{ "type": "text", "text": { "content": "Lacinato kale" } }]
			}
		},
		{
			"object": "block",
			"type": "paragraph",
			"paragraph": {
				"rich_text": [
					{
						"type": "text",
						"text": {
							"content": "Lacinato kale is a variety of kale with a long tradition in Italian cuisine, especially that of Tuscany. It is also known as Tuscan kale, Italian kale, dinosaur kale, kale, flat back kale, palm tree kale, or black Tuscan palm.",
							"link": { "url": "https://en.wikipedia.org/wiki/Lacinato_kale" }
						}
					}
				]
			}
		}
	]
}
# 发送 POST 请求
response = requests.post(url, headers=headers, data=json.dumps(data))

# 打印响应
print(response.text)