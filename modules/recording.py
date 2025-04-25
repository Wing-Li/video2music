# recording.py - 录音功能模块
import eel
import os
from pathlib import Path

@eel.expose
def save_recording(audio_data, output_dir, filename):
    """
    保存从前端发送的录音数据到指定目录
    
    参数:
        audio_data: 音频数据的字节数组
        output_dir: 输出目录路径
        filename: 文件名
    
    返回:
        保存的文件完整路径
    """
    try:
        # 确保输出目录存在
        os.makedirs(output_dir, exist_ok=True)
        
        # 构建完整的文件路径
        file_path = os.path.join(output_dir, filename)
        
        # 将字节数组写入文件
        with open(file_path, 'wb') as f:
            # 将JavaScript数组转换为字节
            byte_data = bytes(audio_data)
            f.write(byte_data)
        
        eel.update_status(f"录音已保存到: {file_path}")
        return file_path
    except Exception as e:
        error_msg = f"保存录音失败: {str(e)}"
        eel.update_status(error_msg)
        return None