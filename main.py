# main.py - 主程序入口
import eel
import multiprocessing
import os
import platform

# 导入自定义模块
from modules import utils
from modules import video2audio
from modules import speech2text
from modules import recording

# 获取CPU核心数，用于设置最大并行转换数
MAX_WORKERS = max(1, min(multiprocessing.cpu_count() - 1, 16))

# 初始化 eel
def initialize_app():
    # 初始化 eel，指定 web 目录
    eel.init('web')
    
    # 确保所有需要的目录都存在
    os.makedirs('output', exist_ok=True)

# 由于前端已经使用了 start_conversion，我们不能直接修改函数名
# 但我们可以取消暴露这个函数，而是直接暴露模块中的函数

if __name__ == '__main__':
    # 设置环境变量抑制 Tk 弃用警告
    os.environ['TK_SILENCE_DEPRECATION'] = '1'
    
    initialize_app()
    
    # 启动 eel 应用
    try:
        # 使用通用的窗口设置，避免干扰对话框
        eel.start('index.html', 
                 size=(1280, 1000), 
                 mode='chrome')
    except Exception as e:
        print(f"启动应用时出错: {str(e)}")
 