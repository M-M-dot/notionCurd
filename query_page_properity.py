import requests
NOTION_API_KEY = 'secret_RLHQMBg7eBvv8D1PraFdlzQ5hX9yyueD0RhkVH234XY'
PAGE_ID = '2024-3-15b8fc30fee24afe8658ed0e5b0c03dc'

page_url = 'https://api.notion.com/v1/pages/'+ PAGE_ID
header = {

    'Notion-Version': '2022-06-28',
    'Authorization': f'Bearer {NOTION_API_KEY}'
}

response = requests.get(page_url, headers=header)
print(response.json())