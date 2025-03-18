# Video2Music 视频转音频工具

一个简单易用的视频转音频工具，可以批量将视频文件转换为MP3格式的音频文件。

![image](https://github.com/Wing-Li/video2music/blob/res/screenshot.png)


## 功能特点

- 支持批量转换视频到MP3
- 简洁的图形界面
- 支持多种视频格式（mp4, avi, mov, mkv, flv, wmv, webm）
- 智能的并行处理，自动优化系统资源使用
- 实时转换进度显示
- 详细的转换状态反馈

## 系统要求

- Python 3.x
- FFmpeg（需要预先安装）

## 安装依赖

```bash
pip install eel
```

### FFmpeg 安装说明

#### Windows 系统
1. 访问 [FFmpeg官网](https://ffmpeg.org/download.html) 或 [FFmpeg Windows构建](https://www.gyan.dev/ffmpeg/builds/)
2. 下载最新的稳定版本（推荐下载"essentials build"）
3. 解压下载的压缩包到任意位置，例如 `C:\ffmpeg`
4. 将FFmpeg的bin目录添加到系统环境变量Path中：
   - 右键点击"此电脑"→"属性"→"高级系统设置"→"环境变量"
   - 在"系统变量"中找到"Path"并编辑
   - 添加FFmpeg的bin目录路径，例如 `C:\ffmpeg\bin`
5. 重启命令提示符或PowerShell
6. 验证安装：在命令行中输入 `ffmpeg -version` 确认显示版本信息

#### macOS 系统
使用Homebrew安装：
```bash
brew install ffmpeg
```

#### Linux 系统
Ubuntu/Debian:
```bash
sudo apt update
sudo apt install ffmpeg
```

CentOS/RHEL:
```bash
sudo yum install epel-release
sudo yum install ffmpeg
```

同时确保系统中已安装 FFmpeg，并且可以在命令行中访问。

## 使用方法

1. 运行程序：
   ```bash
   python main.py
   ```

2. 在打开的界面中：
   - 点击"选择输入目录"按钮选择包含视频文件的文件夹
   - 点击"选择输出目录"按钮选择音频文件的保存位置
   - 点击"开始转换"按钮开始批量转换

3. 转换过程中：
   - 状态窗口会实时显示转换进度
   - 显示当前处理的是第几个文件（例如：3/10）
   - 显示每个文件的转换状态（成功/失败）

## 支持的视频格式

- MP4 (.mp4)
- AVI (.avi)
- MOV (.mov)
- MKV (.mkv)
- FLV (.flv)
- WMV (.wmv)
- WebM (.webm)

## 注意事项

- 确保有足够的磁盘空间存储转换后的音频文件
- 转换过程中请勿关闭程序窗口
- 如果文件较多，程序会自动控制并行转换数量，避免系统负载过高
- 所有转换后的音频文件将保存为MP3格式

## 技术说明

- 使用 FFmpeg 进行音频转换
- 使用 Python Eel 构建图形界面
- 采用线程池进行并行处理
- 自动根据CPU核心数优化并行转换数量
