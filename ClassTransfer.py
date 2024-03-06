
import logging
import requests
import json
from datetime import datetime,timedelta
from ClassNewPage import PageDatabase
'''
@param  dict of a block
'''
class Page:
    def __init__(self,page_id,NOTION_API_KEY):
        self.NOTION_API_KEY = NOTION_API_KEY
        self.PAGE_SIZE = 100
        self.PAGE_ID = page_id
        self.page_url = f'https://api.notion.com/v1/blocks/{PAGE_ID}/children?page_size={self.PAGE_SIZE}'
        self.header = {
            'Notion-Version': '2022-06-28',
            'Authorization': f'Bearer {NOTION_API_KEY}'
        }
        self.logPath = 'Page.log'
        logging.basicConfig(filename=self.logPath , encoding='utf-8', level=logging.DEBUG)

    def get_page(self,page_id ):
        page_url = f'https://api.notion.com/v1/blocks/{page_id}/children?page_size={self.PAGE_SIZE}'    
        response = requests.get(page_url, headers=self.header)
        j = response.json()
        
        return j['results']
    
    def exract_plain_text(self,dicts): 
        text = ""
        if type(dicts)==list: 
            for t in dicts: 
                key = t['type']
                if 'text' in t: 
                    text+=t['plain_text']
        if type(dicts)== dict: 
            key = dicts['type']
            if "rich_text"  in dicts[key]: 
                for t in dicts[key]["rich_text"]: 
                    text += t['plain_text']
        return text 

    def exract_rich_text(self,dict): 
        key = dict['type']
        if "rich_text" not in dict[key]: 
            return ''
        return dict[key]["rich_text"] 
    
    def extract_tablerow_texts(self,obj,time_flag):
        tablerow_id = obj['id']
        objli = self.get_page(tablerow_id)
        texts = []
        keys = []
        dates = []
        for obj in objli: 
            block_time = obj['last_edited_time']
            today_date = datetime.utcnow().date()
            block_datetime = datetime.fromisoformat(block_time.replace('Z', '+00:00'))
            # print(block_datetime.date())
            # print(today_date)
            # print(obj)
            if time_flag and block_datetime.date()!=today_date: 
                continue
            key = obj['type']
            if key == 'table_row': 
                dict = obj[key]
                # print(dict)
            else: 
                logging.info("it's not table format but transfer in table page!!!")
                return
            cells = dict['cells']
            size = len(dict['cells'])
            for i in range(size):
                plain_text = self.exract_plain_text(cells[i])
                print(plain_text)
                for t in target: 
                    if plain_text.startswith(t): 
                        texts.append(cells[i])
                        keys.append(t)
                        dates.append(block_time)
        # print(texts,keys,dates)
        return texts,keys,dates 
    def add_number_richtext(self,rich_text,numbered_id): 
        rich_text[0]['text']['content'] = f"{numbered_id}. " + rich_text[0]['text']['content']
        rich_text[0]['plain_text'] = f"{numbered_id}. " + rich_text[0]['plain_text']
        rich_text[-1]['plain_text'] = rich_text[-1]['plain_text']+"\n"
        rich_text[-1]['text']['content'] =  rich_text[-1]['text']['content']+"\n"
        if numbered_id==0:
            rich_text[0]['text']['content'] = f"\n" + rich_text[0]['text']['content']
            rich_text[0]['plain_text'] = f"\n " + rich_text[0]['plain_text']
    def get_page_content(self,target,time_flag = True):
        '''
        target 是options  
        time_flag 用于判断是只更新昨天的日志。
        '''
        response = requests.get(self.page_url, headers=self.header)
        j = response.json()
        target_begin = False
        keys = []
        values = []
        rich_texts = []
        dates = []
        numbered_id = -1
        for i in j["results"]: 
            block_time = i['created_time']
            today_date = datetime.utcnow().date()
            block_datetime = datetime.fromisoformat(block_time.replace('Z', '+00:00'))
            type = i['type'] 
            # print(i)
            if type == 'table':
                texts,table_keys,table_dates = self.extract_tablerow_texts(i,time_flag) 
                values.extend(texts)
                keys.extend(table_keys)
                dates.extend(table_dates)
                continue 
            if time_flag and block_datetime.date() != today_date: 
                rich_texts = []
                target_begin = False
                numbered_id = -1
                continue
            plain_text = self.exract_plain_text(i)
            rich_text = self.exract_rich_text(i)
            if target_begin and (i['type']=='numbered_list_item' or i['type']=='bulleted_list_item')  :
                self.add_number_richtext(rich_text,numbered_id=numbered_id)
                numbered_id+=1
                rich_texts.extend(rich_text)
                logging.info(f'rich_text {rich_text}')
                continue
            elif target_begin: 
                target_begin = False
                values.append(rich_texts)
                rich_texts = []
            # 判断是plain_text 是否满足target要求，满足则放入rich_texts
            for t in target: 
                if plain_text.startswith(t): 
                    keys.append(t)
                    dates.append(block_time)
                    target_begin = True
                    numbered_id = 0 
                    logging.info(f'rich_text {rich_text}')
                    rich_texts.extend(rich_text)
        if len(rich_texts)!=0: 
            values.append(rich_texts)

        return keys,values,dates

    def insert_into_database(self,DatabaseID,keys,values,dates):
        p = PageDatabase(DatabaseID)
        for i in range(len(keys)): 
            key = keys[i]
            date = dates[i]
            value = values[i]

            data = p.constructDBPageData(date,key,values[i])
            # print(json.loads(data))
            logging.info(p.addPagedata(date,key,value))
            logging.info(data)
            # print(key,date,value)

DatabaseID = '58ef614a-caf7-4f82-912e-dc435c6ee90b'
target = ["学习工作","社会经验","心情","身体","生活日常"]
PAGE_ID = '15b8fc30-fee2-4afe-8658-ed0e5b0c03dc'
NOTION_API_KEY = 'secret_RLHQMBg7eBvv8D1PraFdlzQ5hX9yyueD0RhkVH234XY'
transfer = Page(PAGE_ID,NOTION_API_KEY)
keys,values,dates = transfer.get_page_content(target,False)
print(len(keys)==len(values))
print(len(dates)==len(values))

respos = transfer.insert_into_database(DatabaseID,keys,values,dates)
print(respos)