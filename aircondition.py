from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

#return temp & humid
def get_air():
    option = Options()     
    option.add_argument('--headless')
    driver = webdriver.Firefox(options=option)
    driver.get("http://192.168.0.103:8000/?temp=on")
    res = driver.page_source
    soup = BeautifulSoup(res, 'html.parser')
    return float(soup.find(id="json").text[1:5]), float(soup.find(id="json").text[7:11])

if __name__ == "__main__":
    print(get_air())