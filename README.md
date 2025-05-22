# BandoriLLM
Extract dialogues from the plot text of Bandori to train LLMS  
从bangdream的第三方游戏数据库中下载剧情文件，并提取剧情文本用于训练LLMS  
该仓库导出的数据集目前仅支持训练instruct格式的对话
## Requiremnets 
requests  
re  
tqdm  
将仓库内scripts文件夹下所有脚本放置于同一文件夹即可使用
## 下载剧情文件
**1.1下载活动剧情**
执行`python 1get_event_story.py`  

该脚本会将活动剧情下载至./story下，并以*story_id*-*index*.txt 命名剧情文件

**1.2下载乐队剧情**
1.2.1 打开该网站  [乐队剧情位置](https://bestdori.com/tool/explorer/asset/cn/scenario/band "乐队剧情位置")

1.2.12打开你想要下载的乐队的数据文件
数据文件与乐队对应关系：
- 001 Poppin'Party
- 002 Afterglow
- 003 Hello, Happy World!
- 004 Pastel*Palettes
- 005 Roselia
- 018 RAISE A SUILEN
- 021 Morfonica
- 045 MyGO!!!!!
如图所示选中页面内所有文件，并复制其文件名

![image](https://github.com/FrostMelonMint/BandoriLLM/blob/main/imgs/bandstory.jpg)

打开`1band_story_list.py`，将复制的内容粘贴到
```python
text = """Scenarioband7-001.asset
Scenarioband7-002.asset
Scenarioband7-003.asset
Scenarioband7-004.asset
Scenarioband7-005.asset
Scenarioband7-006.asset
Scenarioband7-007.asset
Scenarioband7-008.asset
"""
```
的多行引号内，保存并执行`python 1band_story_list.py`  

将控制台的输出覆盖到`1get_band_story.py`第16行的`story_list`列表  
同时修改该文件第15行的band_id变量为乐队的id **注意要id需要补足为三位数，如21要写021 **  
保存并执行`python 1get_band_story.py`  
该脚本会将乐队剧情下载至./story下，并以Scenario*bandid*-*index*.asset.txt 命名剧情文件  
## 导出对话
执行`python 2extract_talk.py`
该脚本会将剧情文件中的对话文本提取至./talk下，并以原文件名命名 

修改`2check_chara.py`第96行的target_chara为你所需要训练的角色名  
保存并执行`python 2check_chara.py`
该脚本会将含有目标角色的的对话文本提取至./target下，并以原文件名命名  
同时也会进行合并目标角色重复回复的句子等处理，使之更适应alphaca格式

## 导出数据集
修改`3export_dataset.py`第86行的target_chara为你所需要训练的角色名  
保存并执行`python 3export_dataset.py`
该脚本会将含目标角色的所有对话处理并合并为target.json  
该文件即可用于LLMS的训练
该数据集的参考dataset信息为
```json
"bandori": {
  "file_name": "target.json",
  "columns": {
    "prompt": "instruction",
    "query": "input",
    "response": "output",
    "system": "system",
    "history": "history"
  }
},
```
推荐使用[LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory "LLaMA-Factory")进行训练



