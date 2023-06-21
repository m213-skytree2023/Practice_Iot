import urllib3
from urllib3.exceptions import InsecureRequestWarning
import time
import schedule
import subprocess

urllib3.disable_warnings(InsecureRequestWarning)

def set_alarm(transcript = "15時25分に起こして。"):
    #transcript = "15時25分に起こして。"
    id_hour = transcript.find("時")
    id_minute = transcript.find("分")
    hour_ = transcript[:id_hour]
    minute_ = transcript[id_hour+1:id_minute]
    #アラームをならす
    def task():
        subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe -url http://192.168.0.103:8000/?buzzer=on")
        time.sleep(10)
        subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe -url http://192.168.0.101:8000/?buzzer=on")
        time.sleep(10)
        subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe -url http://192.168.0.104:8000/?buzzer=on")
    #時間になったらtask()を実行
    schedule.every().day.at(f"{hour_.zfill(2)}:{minute_.zfill(2)}").do(task)
    #print(f"{hour_.zfill(2)}:{minute_.zfill(2)}")
    while True:
        schedule.run_pending()
        time.sleep(1)

def stop_alarm():
    subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe -url http://192.168.0.103:8000/?buzzer=off")
    subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe -url http://192.168.0.101:8000/?buzzer=off")
    subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe -url http://192.168.0.104:8000/?buzzer=off")