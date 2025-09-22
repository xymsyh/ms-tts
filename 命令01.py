import edge_tts
import asyncio
import nest_asyncio

nest_asyncio.apply()  # 修复事件循环已关闭的问题

async def run_tts(text, output, voice='zh-CN-XiaoxiaoNeural'):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output)

if __name__ == '__main__':
    asyncio.run(run_tts('你好, 我是您的朋友，我叫晓晓', 'edge-tts-output.mp3'))
    print("语音生成完成：edge-tts-output.mp3")
