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
				"content": "The title"
				}
			}
		]
  },
        "Description":{"rich_text": [
      {
        "type": "text",
        "text": {
          "content": "Some more text with "
        }
      },
      {
        "type": "text",
        "text": {
          "content": "some"
        },
        "annotations": {
          "italic": True
        }
      },
      {
        "type": "text",
        "text": {
          "content": " "
        }
      },
      {
        "type": "text",
        "text": {
          "content": "fun"
        },
        "annotations": {
          "bold": True
        }
      },
      {
        "type": "text",
        "text": {
          "content": " "
        }
      },
      {
        "type": "text",
        "text": {
          "content": "formatting"
        },
        "annotations": {
          "color": "pink"
        }
      }
    ]
  },
        "In stock": {
            "checkbox": True
        },
        "Food group": {
            "select": {
    			"name": "🥦Vegetable",
            }
        },
        "Price":  {
    "number": 1234
  },
        "Last ordered": {
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
        },
        "+1": {
            "people": [
				{
					"object": "user",
					"id": "3e01cdb8-6131-4a85-8d83-67102c0fb98c"
				}]
        },
        "Photo": {
            "files":  [
      {
        "type": "external",
        "name": "Space Wallpaper",
        "external": {
          	"url": "https://website.domain/images/space.png"
        }
      }
    ]
        }
    },
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