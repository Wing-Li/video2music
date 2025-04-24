# video2audio.py - 视频转音频功能模块
import eel
import os
import subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

def convert_with_ffmpeg(input_path, output_path, filename, current_index, total_files):
    """使用 FFmpeg 将视频文件转换为音频文件"""
    try:
        cmd = [
            'ffmpeg',
            '-i', input_path,
            '-vn',          # 禁用视频流
            '-acodec', 'libmp3lame',  # 使用 MP3 编码
            '-q:a', '2',    # 音频质量（0-9，0 最好）
            '-y',           # 覆盖输出文件
            output_path
        ]
        
        process = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            encoding='utf-8',
            errors='replace'
        )

        if process.returncode == 0:
            eel.update_status(f"成功 ({current_index}/{total_files}): {filename} 转换完成")
            return True
        else:
            error_msg = process.stderr.split('\n')[-2]
            eel.update_status(f"失败 ({current_index}/{total_files}): {filename} - {error_msg}")
            return False
            
    except Exception as e:
        eel.update_status(f"异常 ({current_index}/{total_files}): {filename} - {str(e)}")
        return False

@eel.expose
def start_conversion(input_dir, output_dir):
    """批量处理视频转音频转换任务
    
    这个函数名需要与前端JavaScript中调用的函数名一致
    """
    # 计算合适的最大工作线程数
    max_workers = max(1, min(os.cpu_count() - 1, 16))
    
    # 创建输出目录（如果不存在）
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # 获取所有视频文件
    video_files = []
    extensions = ['.mp4','.avi','.mov','.mkv','.flv','.wmv','.webm']
    
    # 修改文件获取逻辑，确保正确处理文件路径
    input_path = Path(input_dir)
    for f in input_path.iterdir():
        if f.is_file() and f.suffix.lower() in extensions:
            video_files.append(f.name)
    
    total_files = len(video_files)
    eel.update_status(f"找到 {total_files} 个视频文件")
    
    # 使用线程池来限制同时转换的数量
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for index, filename in enumerate(video_files, 1):
            input_file = input_path / filename
            output_file = Path(output_dir) / f"{Path(filename).stem}.mp3"
            
            future = executor.submit(convert_with_ffmpeg, str(input_file), str(output_file), filename, index, total_files)
            futures.append(future)
            eel.update_status(f"已添加到队列 ({index}/{total_files}): {filename}")
        
        # 等待所有转换完成
        success_count = 0
        for future in futures:
            try:
                if future.result():  # 检查转换是否成功
                    success_count += 1
            except Exception as e:
                eel.update_status(f"转换过程出错: {str(e)}")
        
        eel.update_status(f"所有转换完成。成功: {success_count}/{total_files}")
        return {
            "total": total_files,
            "success": success_count,
            "failed": total_files - success_count
        } 