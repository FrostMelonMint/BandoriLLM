text = """Scenarioband6-001.asset
Scenarioband6-002.asset
Scenarioband6-003.asset
Scenarioband6-004.asset
Scenarioband6-005.asset
Scenarioband6-006.asset
Scenarioband6-007.asset
Scenarioband6-008.asset
Scenarioband6-009.asset
Scenarioband6-010.asset
Scenarioband6-011.asset
Scenarioband6-012.asset
Scenarioband6-013.asset
Scenarioband6-014.asset
Scenarioband6-015.asset
Scenarioband6-016.asset
Scenarioband6-017.asset
Scenarioband6-018.asset
Scenarioband6-019.asset
Scenarioband6-020.asset
Scenarioband6-021.asset
Scenarioband6-022.asset
Scenarioband6-023.asset
Scenarioband6-024.asset
Scenarioband6-025.asset
Scenarioband6-026.asset
Scenarioband6-027.asset
Scenarioband6-028.asset
Scenarioband6-029.asset
Scenarioband6-030.asset
Scenarioband6-031.asset
Scenarioband6-032.asset
Scenarioband6-033.asset
Scenarioband6-034.asset
Scenarioband6-035.asset"""

# 将文本变量 text 按行分开，存储在 li 列表中
def split_text_into_list():
    """
    功能：将文本变量 text 按行分开，存储在列表中。
    参数：无
    返回值：包含按行分割后的文本的列表
    """
    li = text.split('\n')
    # 过滤掉空字符串
    li = [line for line in li if line.strip()]
    return li

# 调用函数并打印结果
result = split_text_into_list()
print(result)