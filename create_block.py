

import requests
import json 
NOTION_API_KEY = 'secret_RLHQMBg7eBvv8D1PraFdlzQ5hX9yyueD0RhkVH234XY'
PAGE_ID = 'f996056e8d5a496789a8c3fb937a8855'
PAGE_URL = f'https://api.notion.com/v1/blocks/{PAGE_ID}/children'
print(PAGE_URL)
# 请求头
headers = {
    'Authorization': f'Bearer {NOTION_API_KEY}',
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'
}

data={
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
response = requests.patch(PAGE_URL, headers=headers, data=json.dumps(data))

# 打印响应
print(response.text)