import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By


class linkedin_auto:
    def __init__(self, userid, password, text):
        self.userid = userid
        self.password = password
        self.post_ = text

    def post(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        driver = webdriver.Chrome(options=chrome_options)

        driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")


        username = driver.find_element(By.NAME, "session_key")
        username.send_keys(self.userid)  
        username.send_keys(Keys.RETURN)


        password = driver.find_element(By.NAME, "session_password")
        password.send_keys(self.password)  
        password.send_keys(Keys.RETURN)


        post_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.share-box-feed-entry__trigger')))
        post_btn.click()

        time.sleep(3)  
        modal = driver.find_element(By.CLASS_NAME,"ql-editor")
        post2 = self.post_
        modal.send_keys(post2)


        post_btn = driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/button/span')
        post_btn.click()
