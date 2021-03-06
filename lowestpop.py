from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

url = "https://www.roblox.com/login"
gamemode = "https://www.roblox.com/games/2317712696/The-Wild-West" #url of game
usern = ""
passw = ""

driver = webdriver.Chrome()

def login():
    driver.get(url)
    driver.find_element_by_id("login-username").send_keys(usern)
    driver.find_element_by_id("login-password").send_keys(passw)
    driver.find_element_by_id("login-button").click()
    WebDriverWait(driver, 5).until(EC.title_contains("Home"))

def find_games():
    driver.get(gamemode+"#!/game-instances")
    while True:
        time.sleep(2)
        i = load_more()
        try:
            i.click()
        except:
            break

def load_more():
    return driver.find_element_by_class_name("rbx-running-games-load-more")
            
def parse_games():
    p = driver.find_element_by_id("game-detail-page")
    placeid = p.get_attribute("data-place-id")
    ul = driver.find_element_by_class_name("rbx-game-server-item-container")
    items = ul.find_elements_by_tag_name("li")
    u = 0
    gamestr = {}
    for i in range(len(items)-6,len(items)-1):
        gamestr[u] = "Roblox.GameLauncher.joinGameInstance("+placeid+", \""+items[i].get_attribute('data-gameid')+"\")"
        print(str(u+1)+": "+gamestr[u])
        u += 1
    val = input("Pick 1-5: ")

    driver.execute_script(gamestr[int(val)-1])
    
login()
find_games()
time.sleep(2)
parse_games()
