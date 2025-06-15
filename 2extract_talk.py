import os

save_path = "./talk"

def process_story_files(story_path):
    """
    处理指定路径下的所有故事文件，提取并整理对话信息，同时删除对话中的 "\\n"，
    然后将每个文件的处理结果保存为同名文件，存储到 save_path 文件夹中。

    参数:
    story_path (str): 故事文件所在的目录路径。

    返回:
    无
    """
    # 提取story_path下所有文件名到列表
    story_list = os.listdir(story_path)
    # 确保保存路径存在
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    for file in story_list:
        talk_list = []
        file_path = os.path.join(story_path, file)
        with open(file_path, "r", encoding="utf-8") as f:
            data = f.read()
            while data.find('windowDisplayName":"') > -1:
                start_index = data.find('windowDisplayName":"') + 20
                data = data[start_index:]
                name_end_index = data.find('","')
                name = data[:name_end_index]
                data = data[name_end_index + 10:]
                body_end_index = data.find('"')
                word = data[:body_end_index]
                # 删除 "\\n,拆分多人说同一句"
                word = word.replace("\\n", "")
                separators = ["・", "、"]
                for sep in separators:
                    if sep in name:
                        names = name.split(sep)
                        for n in names:
                            talk_list.append({"name": n, "word": word})
                        break
                else:
                    talk_list.append({"name": name, "word": word})
        
        # 将处理结果保存到文件

        save_file_path = os.path.join(save_path, file)
        if talk_list:
            with open(save_file_path, "w", encoding="utf-8") as f:
                for item in talk_list:
                    f.write(f"Name: {item['name']}, Word: {item['word']}\n")

process_story_files("./story")

