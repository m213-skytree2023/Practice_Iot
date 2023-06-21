import subprocess

def rotate_fan(status):
    if (status):
        subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe -url http://192.168.0.101:8000/?servo=0")
        return False
    else:
        subprocess.run(r"C:\Program Files\Google\Chrome\Application\chrome.exe -url http://192.168.0.101:8000/?servo=180")
        return True