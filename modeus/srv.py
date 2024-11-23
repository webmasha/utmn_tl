import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

MODEUS_LOGIN = os.environ["MODEUS_LOGIN"]
MODEUS_PASSWORD = os.environ["MODEUS_PASSWORD"]
MODEUS_REMOTE = os.environ.get("MODEUS_REMOTE", "localhost")

class Parser():

    def __init__(self, local):
        print(f"parsing start ... local is {bool(local)}")
        options = webdriver.ChromeOptions()
        options.add_argument("--avoid-stats") 
        # options.add_argument("--disable-blink-features=AutomationControlled") # Чтобы браузер был менее заметным
        if local:
            self.driver = webdriver.Chrome(options=options)
        else:
            options.add_argument("--headless=new")
            self.driver = webdriver.Remote(options=options, command_executor=f"http://{MODEUS_REMOTE}:4444")

    def login(self):
        self.driver.get("https://utmn.modeus.org")
        print('login:', self.driver.title)
        self.sleep(1)

        self.driver.find_element(By.ID, "userNameInput").send_keys(MODEUS_LOGIN)
        self.driver.find_element(By.ID, "passwordInput").send_keys(MODEUS_PASSWORD)
        self.driver.find_element(By.ID, "submitButton").click()

        print("after click:", self.driver.title)

    def sleep(self, seconds = 1):
        time.sleep(seconds)
        print(f"after sleep({seconds}): {self.driver.title}")

    def get_jwt(self):
        return self.driver.execute_script("return window.sessionStorage.id_token")


if __name__ == '__main__':
    p = Parser(1)
    p.login()
    print(p.get_jwt())
    p.driver.quit()
