# 视频音频处理工具

一个多功能的视频和音频处理工具，具有以下功能：

1. 视频转音频：将视频文件批量转换为 MP3 格式
2. 语音转文本：使用 OpenAI Whisper 模型将语音内容转换为文本

## 项目结构

```
├── main.py               # 主程序入口
├── modules/              # 功能模块目录
│   ├── __init__.py       # 使 modules 成为 Python 包
│   ├── video2audio.py    # 视频转音频功能
│   ├── speech2text.py    # 语音转文本功能
│   └── utils.py          # 通用工具函数
└── web/                  # 前端界面
    └── index.html        # 主界面
```

## 依赖项

- Python 3.9+
- FFmpeg
- OpenAI Whisper

## 安装

1. 安装 Python 依赖

```bash
pip install eel openai-whisper
```

2. 安装 FFmpeg

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt install ffmpeg
```

**Windows:**
```bash
choco install ffmpeg
```

## 使用方法

1. 运行应用

```bash
python main.py
```

2. 使用视频转音频功能
   - 点击"视频转音频"标签
   - 选择包含视频文件的输入目录
   - 选择输出目录
   - 点击"开始转换"

3. 使用语音转文本功能
   - 点击"语音转文字"标签
   - 选择音频或视频文件
   - 选择合适的模型（tiny、base、small、medium、large）
   - 选择语言（或使用自动检测）
   - 点击"加载模型"，然后点击"开始转录"

## 模块说明

### video2audio.py

视频转音频模块，使用 FFmpeg 将视频文件转换为 MP3 格式的音频文件。支持批量处理。

### speech2text.py

语音转文本模块，使用 OpenAI Whisper 模型将语音内容转换为文本。支持多种语言和不同大小的模型。

### utils.py

通用工具模块，提供文件选择对话框等功能。
