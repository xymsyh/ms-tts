import os
import signal
import psutil

def stop_tts():
    # 获取当前进程的 PID
    current_pid = os.getpid()
    
    # 遍历所有进程
    for proc in psutil.process_iter(['pid', 'name']):
        # 检查进程名称是否与播放音频的进程匹配
        if proc.info['name'] == 'python.exe' and proc.pid != current_pid:
            # 发送终止信号
            os.kill(proc.pid, signal.SIGTERM)
            print(f"已终止进程: {proc.pid}")

if __name__ == '__main__':
    stop_tts()