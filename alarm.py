import time
import datetime
import schedule
import subprocess

def task():   
    subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe -url http://192.168.0.103:8000/?buzzer=on")
    subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe -url http://192.168.0.103:8000/?led=white,on")
    time.sleep(10)
    subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe -url http://192.168.0.101:8000/?buzzer=on")
    subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe -url http://192.168.0.101:8000/?led=white,on")
    time.sleep(10)
    subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe -url http://192.168.0.104:8000/?buzzer=on")
    subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe -url http://192.168.0.104:8000/?led=white,on")

#transcript = "15時25分に起こして。"
def set_alarm(hour_, minute_):
    dt_today = datetime.datetime.today()
    alarm_time = f"{dt_today.year}-{dt_today.month}-{dt_today.day} {hour_.zfill(2)}:{minute_.zfill(2)}:00"
    time_array = time.strptime(alarm_time, "%Y-%m-%d %H:%M:%S")
    time_stamp = int(time.mktime(time_array))*1000
    while (time_stamp - int(round(time.time() * 1000))) > 0:
        schedule.run_pending()
        time.sleep(1)
    task()

def stop_alarm():
    subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe -url http://192.168.0.103:8000/?buzzer=off")
    subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe -url http://192.168.0.101:8000/?buzzer=off")
    subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe -url http://192.168.0.104:8000/?buzzer=off")
    subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe -url http://192.168.0.103:8000/?led=white,off")
    subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe -url http://192.168.0.101:8000/?led=white,off")
    subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe -url http://192.168.0.104:8000/?led=white,off")