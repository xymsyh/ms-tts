import edge_tts
import asyncio
import nest_asyncio
import argparse
import os
from playsound import playsound  # 用于播放音频

nest_asyncio.apply()  # 修复事件循环已关闭的问题

# 默认保存路径
DEFAULT_SAVE_FOLDER = r"D:\Code\langDuBaoCun"

async def run_tts(text, output_path, voice='zh-CN-XiaoxiaoNeural'):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Edge TTS 命令行朗读工具')
    parser.add_argument('text', type=str, help='要朗读的文本')
    parser.add_argument('--voice', type=str, default='zh-CN-XiaoxiaoNeural', help='语音类型')

    args = parser.parse_args()

    # 确保保存目录存在
    os.makedirs(DEFAULT_SAVE_FOLDER, exist_ok=True)

    # 输出文件路径
    output_file = os.path.join(DEFAULT_SAVE_FOLDER, 'edge-tts-output.mp3')

    # 生成语音文件
    asyncio.run(run_tts(args.text, output_file, args.voice))

    # 先播放一次
    print("正在朗读文本...")
    playsound(output_file)

    print(f"语音已保存到：{output_file}")
