import subprocess

for i in range(0,10):
    if i% 2 == 0 :
        subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe -url http://192.168.0.101:8000/?servo=0")
    else :
        subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe -url http://192.168.0.101:8000/?servo=180")

