import os
import signal
import psutil

def stop_tts():
    current_pid = os.getpid()
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            # 检查进程名称和命令行参数是否匹配 main.py 路径
            if (
                proc.info['name'] == 'python.exe'
                and proc.pid != current_pid
                and any(
                    os.path.abspath(arg) == os.path.abspath(r'D:\R2025\AHK\ms-tts\main.py')
                    for arg in proc.info.get('cmdline', [])
                )
            ):
                os.kill(proc.pid, signal.SIGTERM)
                print(f"已终止进程: {proc.pid}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

if __name__ == '__main__':
    stop_tts()