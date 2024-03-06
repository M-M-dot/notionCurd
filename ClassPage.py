
import logging
import requests
import json
from datetime import datetime
class Page: 
    def __init__(self,page_id,NOTION_API_KEY):
        self.NOTION_API_KEY = NOTION_API_KEY
        self.PAGE_SIZE = 100
        self.PAGE_ID = page_id
        self.page_url = f'https://api.notion.com/v1/blocks/{self.PAGE_ID}/children?page_size={self.PAGE_SIZE}'
        self.header = {
            'Notion-Version': '2022-06-28',
            'Authorization': f'Bearer {self.__class__NOTION_API_KEY}'
        }
        self.logPath = 'Page.log'
        logging.basicConfig(filename=self.logpath, encoding='utf-8', level=logging.DEBUG)
    def exract_plain_text(self,dict): 
        key = dict['type']
        text = ""
        if "rich_text" not in dict[key]: 
            return ''
        for t in dict[key]["rich_text"]: 
            text += t['plain_text']
        return text 
    
    def exract_rich_text(self,dict): 
        key = dict['type']
        if "rich_text" not in dict[key]: 
            return ''
        return dict[key]["rich_text"] 
    
    
class TablerowPage(Page):  
    def __init__(self,page_id,table_width,has_column_header,has_row_header):
       super(Page, self).__init__(page_id)
       self.table_width = table_width
       self.has_column_header = has_column_header
       self.has_row_header = has_row_header
    def getPage(self): 
        response = requests.get(self.page_url, headers=self.header)
        j = response.json()
        return j 
    def extract_cell_text(self): 
        dict = self.getPage()
        key = dict['type']
        if key == 'table_row': 
            dict = dict[key]
        else: 
            logging.info("it's not table format but transfer in table page!!!")
            return
        cells = dict['cells']
        texts =[]
        size = len(dict['cells'])
        for i in range(size):
            texts.extend[cells[i]]
        return texts 
class TogglePage(Page): 
    def __init__(self,page_id):
       super(Page, self).__init__(page_id)
    def getPage(self): 
        response = requests.get(self.page_url, headers=self.header)
        j = response.json()
        return j 
    def extract_Toggle_text(self,dict): 
        dict = self.getPage()
        key = dict['type']
        if key == 'toggle': 
            dict = dict[key]
        else: 
            logging.info("it's not Toggle format but transfer in toggle page!!!")
            return
        cells = dict['cells']
        texts =[]
        size = len(dict['cells'])
        for i in range(size):
            texts.extend[cells[i]]
        return texts 