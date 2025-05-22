import requests
import re
from tqdm import tqdm
import os

hearders = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
    'Referer':'https://bestdori.com/',
    'Host':'bestdori.com'
}

url = 'https://bestdori.com/assets/cn/scenario/band/'


band_id = "021"
story_list = ['Scenarioband6-001.asset', 'Scenarioband6-002.asset', 'Scenarioband6-003.asset', 'Scenarioband6-004.asset', 'Scenarioband6-005.asset', 'Scenarioband6-006.asset', 'Scenarioband6-007.asset', 'Scenarioband6-008.asset', 'Scenarioband6-009.asset', 'Scenarioband6-010.asset', 'Scenarioband6-011.asset', 'Scenarioband6-012.asset', 'Scenarioband6-013.asset', 'Scenarioband6-014.asset', 'Scenarioband6-015.asset', 'Scenarioband6-016.asset', 'Scenarioband6-017.asset', 'Scenarioband6-018.asset', 'Scenarioband6-019.asset', 'Scenarioband6-020.asset', 'Scenarioband6-021.asset', 'Scenarioband6-022.asset', 'Scenarioband6-023.asset', 'Scenarioband6-024.asset', 'Scenarioband6-025.asset', 'Scenarioband6-026.asset', 'Scenarioband6-027.asset', 'Scenarioband6-028.asset', 'Scenarioband6-029.asset', 'Scenarioband6-030.asset', 'Scenarioband6-031.asset', 'Scenarioband6-032.asset', 'Scenarioband6-033.asset', 'Scenarioband6-034.asset', 'Scenarioband6-035.asset']
url = url + band_id + "_rip/"

with tqdm(total = len(story_list)) as pbar:
    for story in story_list:
        
        try:
            req_url = url + story
            #print(req_url)
            data = requests.get(req_url, headers=hearders)
                
            with open("./story/" + story + ".txt", "wb") as f:
                f.write(data.content)
        except:
            print("passed")
            pass
        pbar.update(1)


