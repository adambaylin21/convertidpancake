# -*- coding: utf-8 -*-

import json, re
from requests import session
from define import *

from urllib3 import disable_warnings , exceptions

disable_warnings(exceptions.InsecureRequestWarning)
import warnings
warnings.filterwarnings("ignore")

ss = session()
ss.verify = ss.trust_env = False

def getidpancake(api, idpost):
    apiNew = api + f'103086742653331/conversations/{idpost}'
    response = ss.get(url=apiNew , params=params, cookies=cookies, headers = header).text
    data = json.loads(response)
    return data['customers'][0]['id']

def getidprofile(api, idpost, idcake):
    idpage = idpost.split('_')[0]
    apiNew = api + f'{idpage}/conversations/{idpost}/messages'
    params2['customer_id'] = idcake
    response = ss.get(url=apiNew , params=params2, cookies=cookies, headers = header).text
    data = json.loads(response)
    return f"{data['global_id']}|{data['customers'][0]['name']}|{data['lives_in']}"

def extract_numbers(url):
    match = re.search(r'(\d+_\d+)', url)
    if match: return match.group(1)
    else: return None

def convertID(url):
    idpost = extract_numbers(url)
    idcake = getidpancake(api, idpost)
    idfb = getidprofile(api, idpost, idcake)
    return idfb

if __name__ == '__main__':

    # url = 'https://pancake.vn/uyquyenluxuryfan?c_id=103086742653331_25165769423069417'
    # a = convertID(url)
    # print(a)

    # with open('response.txt', 'r', encoding='utf8') as f:
    #     a = f.read()
    #     data = json.loads(a)
    
    pass