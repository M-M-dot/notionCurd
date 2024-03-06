

import requests
import json
NOTION_API_KEY = 'secret_RLHQMBg7eBvv8D1PraFdlzQ5hX9yyueD0RhkVH234XY'
PAGE_ID = '15b8fc30-fee2-4afe-8658-ed0e5b0c03dc'
PAGE_SIZE = 100
page_url = f'https://api.notion.com/v1/blocks/{PAGE_ID}/children?page_size={PAGE_SIZE}'
# page_url = f'https://api.notion.com/v1/blocks/{PAGE_ID}'
header = {

    'Notion-Version': '2022-06-28',
    'Authorization': f'Bearer {NOTION_API_KEY}'
}

response = requests.get(page_url, headers=header)
j = response.json()
print(type(j))
dict_structure = json.dumps(j, indent=4)
with open('dict.json', 'w') as file:
    json.dump(j, file, indent=4)
given_datetime = datetime.fromisoformat(given_time.replace('Z', '+00:00'))
print(j["results"][4]['created_time'])