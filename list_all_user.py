


import requests
NOTION_API_KEY = 'secret_RLHQMBg7eBvv8D1PraFdlzQ5hX9yyueD0RhkVH234XY'
PAGE_ID = 'f996056e8d5a496789a8c3fb937a8855'
PAGE_SIZE = 100
page_url = f'https://api.notion.com/v1/users'
header = {
    'Notion-Version': '2022-06-28',
    'Authorization': f'Bearer {NOTION_API_KEY}'
}

response = requests.get(page_url, headers=header)
print(response.json())