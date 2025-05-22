import requests
import re
from tqdm import tqdm
import os

hearders = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
    'Referer':'https://bestdori.com/',
    'Host':'bestdori.com'
}

url = 'https://bestdori.com/assets/cn/scenario/eventstory/'
story_list = ['event1', 'event10', 'event100', 'event101', 'event102', 'event103', 'event104', 'event105', 'event106', 'event107', 'event108', 'event109', 'event11', 'event110', 'event111', 'event112', 'event113', 'event114', 'event115', 'event116', 'event118', 'event119', 'event12', 'event120', 'event121', 'event122', 'event123', 'event124', 'event126', 'event127', 'event128', 'event13', 'event130', 'event131', 'event132', 'event133', 'event134', 'event136', 'event137', 'event138', 'event139', 'event14', 'event140', 'event142', 'event143', 'event144', 'event145', 'event146', 'event148', 'event149', 'event15', 'event150', 'event151', 'event152', 'event153', 'event154', 'event155', 'event157', 'event158', 'event159', 'event16', 'event160', 'event161', 'event162', 'event163', 'event164', 'event166', 'event167', 'event168', 'event169', 'event17', 'event170', 'event171', 'event173', 'event174', 'event175', 'event176', 'event177', 'event178', 'event179', 'event18', 'event180', 'event181', 'event182', 'event183', 'event184', 'event185', 'event186', 'event187', 'event188', 'event189', 'event19', 'event190', 'event191', 'event192', 'event193', 'event194', 'event195', 'event196', 'event197', 'event198', 'event199', 'event2', 'event20', 'event200', 'event201', 'event202', 'event203', 'event204', 'event205', 'event206', 'event207', 'event208', 'event209', 'event21', 'event210', 'event211', 'event212', 'event213', 'event214', 'event215', 'event216', 'event217', 'event218', 'event219', 'event22', 'event220', 'event221', 'event222', 'event223', 'event224', 'event225', 'event226', 'event227', 'event228', 'event229', 'event23', 'event230', 'event231', 'event232', 'event233', 'event234', 'event235', 'event236', 'event237', 'event238', 'event239', 'event24', 'event240', 'event241', 'event242', 'event243', 'event244', 'event245', 'event246', 'event247', 'event249', 'event25', 'event250', 'event251', 'event252', 'event253', 'event254', 'event255', 'event256', 'event257', 'event258', 'event259', 'event26', 'event260', 'event261', 'event262', 'event263', 'event264', 'event265', 'event266', 'event267', 'event268', 'event269', 'event27', 'event270', 'event271', 'event272', 'event273', 'event274', 'event275', 'event276', 'event277', 'event278', 'event279', 'event28', 'event280', 'event281', 'event29', 'event3', 'event30', 'event31', 'event32', 'event33', 'event34', 'event35', 'event36', 'event37', 'event38', 'event39', 'event4', 'event40', 'event41', 'event42', 'event43', 'event44', 'event45', 'event47', 'event48', 'event49', 'event5', 'event50', 'event51', 'event52', 'event53', 'event55', 'event56', 'event58', 'event59', 'event6', 'event60', 'event61', 'event62', 'event63', 'event64', 'event65', 'event66', 'event67', 'event68', 'event69', 'event7', 'event70', 'event71', 'event72', 'event73', 'event74', 'event75', 'event76', 'event77', 'event78', 'event79', 'event8', 'event80', 'event81', 'event82', 'event83', 'event84', 'event85', 'event86', 'event87', 'event88', 'event89', 'event9', 'event90', 'event91', 'event92', 'event93', 'event94', 'event95', 'event96', 'event97', 'event98', 'event99', 'event999']

try:
    os.makedirs("./story")
except:
    pass

with tqdm(total = len(story_list)) as pbar:
    for story in story_list:
        if len(story) == len('event1'):
            story_id = "event0" + str(int(story[5]))
        else:
            story_id = story
        for index in range(1, 15):
            if index <10:
                index = "0" + str(index)
            else:
                index = str(index)
            try:
                req_url = url + story + "_rip/Scenario" + story_id + "-" + index + ".asset"
                #print(req_url)
                data = requests.get(req_url, headers=hearders)
                
                with open("./story/" + story_id+"-" + index + ".txt", "wb") as f:
                    f.write(data.content)
            except:
                print("passed")
                pass
        pbar.update(1)


