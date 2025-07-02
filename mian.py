import pyperclip
import pyautogui
import time
import tkinter as tk
import chardet
import os
"""pyinstaller --onefile --add-data "example.txt;." main.py """
"""   pyinstaller --onefile --noconsole --icon=icon.ico --name=Google --add-data "example.txt;." mian.py    """
def get_example_path():
    """获取脚本目录下的 example.txt"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, "example.txt")

def detect_encoding(file_path):
    """使用 chardet 自动检测文件编码"""
    with open(file_path, 'rb') as f:
        raw = f.read(10000)
        result = chardet.detect(raw)
        return result['encoding'] or 'utf-8'

def find_text_in_file(keyword, file_path):
    """查找包含关键字的一行，返回换行替代制表符的内容"""
    encoding = detect_encoding(file_path)
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            for line in f:
                if keyword in line:
                    return line.strip().replace('\t', '\n')
    except Exception as e:
        return f"[读取文件失败: {e}]"
    return "[未找到匹配内容]"

def show_tooltip(text, x, y):
    """在指定位置显示 tooltip"""
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.geometry(f"+{x}+{y}")
    label = tk.Label(root, text=text, bg="lightyellow", justify='left',
                     relief='solid', borderwidth=1, font=("Arial", 10))
    label.pack(ipadx=10, ipady=5)
    root.after(4000, root.destroy)
    root.mainloop()

def main_loop(file_path):
    last_text = ""
    print(f"监听剪贴板中，使用文件：{file_path}")
    while True:
        time.sleep(0.5)
        try:
            current_text = pyperclip.paste().strip()
            if current_text != last_text and current_text:
                print(f"[检测到复制内容]：{current_text}")
                last_text = current_text
                result = find_text_in_file(current_text, file_path)
                x, y = pyautogui.position()
                show_tooltip(result, x + 20, y + 20)
        except Exception as e:
            print(f"发生错误：{e}")

if __name__ == "__main__":
    file_path = get_example_path()
    if os.path.exists(file_path):
        main_loop(file_path)
    else:
        print(f"找不到 example.txt 文件：{file_path}")
