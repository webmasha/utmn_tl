import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

MODEUS_LOGIN = os.environ["MODEUS_LOGIN"]
MODEUS_PASSWORD = os.environ["MODEUS_PASSWORD"]
MODEUS_REMOTE = os.environ.get("MODEUS_REMOTE", "localhost")

class Parser():
    url = "https://utmn.modeus.org"

    def __init__(self, local, debug = True):
        self.debug = debug
        self.local = local

    def start(self):
        if self.debug:
            print(f"parsing start ... local is {bool(self.local)}")
        options = webdriver.ChromeOptions()
        options.add_argument("--avoid-stats") 
        # options.add_argument("--disable-blink-features=AutomationControlled") # Чтобы браузер был менее заметным
        if self.local:
            self.driver = webdriver.Chrome(options=options)
        else:
            options.add_argument("--headless=new")
            self.driver = webdriver.Remote(options=options, command_executor=f"http://{MODEUS_REMOTE}:4444")

    def login(self):
        self.driver.get(Parser.url)
        if self.debug:
            print('login:', self.driver.title)
        self.sleep(1)

        self.driver.find_element(By.ID, "userNameInput").send_keys(MODEUS_LOGIN)
        self.driver.find_element(By.ID, "passwordInput").send_keys(MODEUS_PASSWORD)
        self.driver.find_element(By.ID, "submitButton").click()

        if self.debug:
            print("after click:", self.driver.title)

    def sleep(self, seconds = 1):
        time.sleep(seconds)
        if self.debug:
            print(f"after sleep({seconds}): {self.driver.title}")

    def get_jwt(self):
        self.jwt = self.driver.execute_script("return window.sessionStorage.id_token")
        return self.jwt

    def save_jwt(self):
        with open('tmp/jwt.txt', 'w') as f:
            f.write(self.jwt)


if __name__ == '__main__':
    p = Parser(1)
    p.start()
    p.login()
    p.sleep(1)
    print(f"jwt: {p.get_jwt()}")
    p.save_jwt()
    p.driver.quit()
