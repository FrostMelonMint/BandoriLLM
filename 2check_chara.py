import os
import shutil

def check_and_move_files(source_folder, target_folder,chara):
    """
    检查指定源文件夹中的所有文件，若文件中的 Name 字段包含 "chara"，则将该文件移动到目标文件夹。

    参数:
    source_folder (str): 源文件夹的路径。
    target_folder (str): 目标文件夹的路径。

    返回:
    None
    """
    # 若目标文件夹不存在，则创建它
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # 遍历源文件夹中的所有文件
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                    flag = "Name: " + chara
                    if flag in content:
                        target_file_path = os.path.join(target_folder, file)
                        shutil.copy(file_path, target_file_path)
                        print(f"已将 {file} 移动到 {target_folder}")
            except Exception as e:
                print(f"处理文件 {file} 时出错: {e}")


def process_file(file_path, chara):
    """
    处理单个文件，将相邻包含 "Name: chara" 行中的后续行 "Word: " 内容移动到第一行末尾。

    参数:
    file_path (str): 要处理的文件的路径。
    chara (str): 要匹配的角色名称。

    返回:
    None: 直接修改文件内容。
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_lines = []
    i = 0
    while i < len(lines):
        current_line = lines[i].strip()
        if f"Name: {chara}" in current_line:
            # 合并所有相邻的包含 "Name: {chara}" 的行
            merged_line = current_line
            j = i + 1
            while j < len(lines) and f"Name: {chara}" in lines[j]:
                next_line = lines[j].strip()
                if "Word: " in next_line:
                    word_content = next_line.split("Word: ")[1]
                    merged_line += word_content
                j += 1
            new_lines.append(merged_line + '\n')
            i = j
        else:
            new_lines.append(lines[i])
            i += 1

    # 如果 new_lines 的第一个元素以 "Name: chara" 开头，则删除第一个元素
    if new_lines and new_lines[0].startswith(f"Name: {chara}"):
        print("hit")
        new_lines.pop(0)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

def process_folder(folder_path,chara):
    """
    处理文件夹内的所有文件。

    参数:
    folder_path (str): 要处理的文件夹的路径。
    """

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        process_file(file_path,chara)


if __name__ == "__main__":
    # 请根据实际情况修改源文件夹路径
    source_folder = "./talk"
    target_folder = "./target"
    # 目标角色名称 根据实际情况修改
    target_chara = "真白"

    check_and_move_files(source_folder, target_folder,target_chara)
    process_folder(target_folder,target_chara)