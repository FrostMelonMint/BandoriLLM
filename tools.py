import requests
import re
from tqdm import tqdm
import os
import webbrowser
import pyautogui
import time
import pyperclip

hearders = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
    'Referer':'https://bestdori.com/',
    'Host':'bestdori.com'
}

url = 'https://bestdori.com/tool/explorer/asset/cn/scenario/band/001'

def get_page_content(url):
    webbrowser.open(url)
    # 等待页面加载 时间间隔可以调节
    time.sleep(5)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('a')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('a')

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('c')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('c')

    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('w')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('w')

    clipboard_content = pyperclip.paste()
    return clipboard_content
