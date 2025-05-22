import os
import json

def make_conversation(target_folder, chara):
    """
    将指定文件夹内的所有文件内容读取到一个列表中。
    :target_folder: 目标文件夹路径
    :chara: 包含所有文件内容的列表

    """
    a = []

    # 遍历目标文件夹内的所有文件
    for file in os.listdir(target_folder):
            print(file)
            if True:
                file_path = os.path.join(target_folder, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = [line.replace("\n","") for line in f.readlines()]

                    index = 0
                    while index < len(lines):
                        line = lines[index].strip()
                        if f"Name: {chara}" in line:
                            prev_lines = lines[:index+1]
                            cache = []
                            while prev_lines:
                                prv_index = 0
                                for item in prev_lines:
                                    if f"Name: {chara}" in item:


                                        if prv_index > 0:
                                            cache.append("".join(prev_lines[:prv_index]))
                                        cache.append(prev_lines[prv_index])
                                        prev_lines = prev_lines[prv_index + 1:]
                                        break
                                    prv_index += 1


                            a.append(cache)
                        index += 1
    
    return a

def convert_to_json_structure(conversations):
    """
    将 make_conversation 返回的对话列表转换为指定 JSON 结构

    参数:
        conversations (list): make_conversation 返回的列表（每个元素是对话子列表）

    返回:
        list: 包含目标 JSON 对象的列表
    """
    json_list = []
    for cache in conversations:
        if len(cache) < 2:
            continue  # 跳过不满足条件的对话（至少需要2个元素）
        
        # 提取 instruction 和 output
        instruction = cache[-2]
        output = cache[-1]
        
        # 处理 history 字段
        if len(cache) == 2:
            history = []
        else:
            # 剩余元素为前 len(cache)-2 个元素，按顺序两两分组
            remaining = cache[:-2]
            history = [remaining[i:i+2] for i in range(0, len(remaining), 2)]
        
        # 构建 JSON 对象
        json_obj = {
            "instruction": instruction,
            "input": "",
            "output": output,
            "system": "",
            "history": history
        }
        json_list.append(json_obj)
    return json_list

if __name__ == "__main__":
    target_folder = "./target"
    target_chara = "真白"  # 可根据需要修改

    conversations = make_conversation(target_folder, target_chara)
    output = convert_to_json_structure(conversations)
    #保存为json文件
    with open(f"./target.json", "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=4)
