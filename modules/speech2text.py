# speech2text.py - 语音转文本功能模块
import eel
import os
import tempfile
import whisper
from pathlib import Path
# 避免循环引用，改为在函数内部导入
# from . import video2audio

# 全局变量用于存储加载的模型
whisper_model = None

@eel.expose
def load_whisper_model(model_name="base"):
    """加载 Whisper 模型"""
    global whisper_model
    try:
        eel.update_status(f"正在加载语音识别模型 {model_name}...")
        whisper_model = whisper.load_model(model_name)
        eel.update_status(f"模型 {model_name} 加载完成")
        return True
    except Exception as e:
        eel.update_status(f"模型加载失败: {str(e)}")
        return False

@eel.expose
def transcribe_audio(file_path, language=None):
    """使用 Whisper 转录音频文件"""
    global whisper_model
    
    # 如果模型未加载，自动加载 base 模型
    if whisper_model is None:
        success = load_whisper_model("base")
        if not success:
            return {"error": "无法加载语音识别模型"}
    
    try:
        eel.update_status(f"开始转录: {Path(file_path).name}")
        
        # 处理输入的视频文件，先转为临时音频
        file_path = Path(file_path)
        is_video = file_path.suffix.lower() in ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm']
        
        if is_video:
            eel.update_status("检测到视频文件，先转换为音频...")
            temp_audio = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False)
            temp_audio.close()
            
            # 在需要时导入 video2audio 以避免循环引用
            from . import video2audio
            # 使用 FFmpeg 转换为音频
            video2audio.convert_with_ffmpeg(str(file_path), temp_audio.name, file_path.name, 1, 1)
            file_path = temp_audio.name
            
        # 设置转录选项
        options = {}
        if language and language != "auto":
            options["language"] = language
        
        # 执行转录
        result = whisper_model.transcribe(str(file_path), **options)
        
        # 如果是临时文件，转录后删除
        if is_video and 'temp_audio' in locals():
            os.unlink(temp_audio.name)
            
        eel.update_status("转录完成")
        
        # 返回转录结果
        return {
            "text": result["text"],
            "segments": [{"start": seg["start"], "end": seg["end"], "text": seg["text"]} 
                         for seg in result["segments"]]
        }
    except Exception as e:
        eel.update_status(f"转录失败: {str(e)}")
        return {"error": str(e)}

@eel.expose
def get_available_models():
    """获取可用的 Whisper 模型列表"""
    return [
        {"name": "tiny", "description": "最小模型 (39M) - 速度最快，精度最低"},
        {"name": "base", "description": "基础模型 (74M) - 速度快，精度一般"},
        {"name": "small", "description": "小型模型 (244M) - 速度和精度平衡"},
        {"name": "medium", "description": "中型模型 (769M) - 速度较慢，精度较高"},
        {"name": "large", "description": "大型模型 (1.5G) - 速度最慢，精度最高"}
    ]

@eel.expose
def get_available_languages():
    """获取 Whisper 支持的语言列表"""
    return [
        {"code": "auto", "name": "自动检测"},
        {"code": "zh", "name": "中文"},
        {"code": "en", "name": "英语"},
        {"code": "ja", "name": "日语"},
        {"code": "ko", "name": "韩语"},
        {"code": "fr", "name": "法语"},
        {"code": "de", "name": "德语"},
        {"code": "es", "name": "西班牙语"},
        {"code": "ru", "name": "俄语"},
        {"code": "it", "name": "意大利语"}
    ] 