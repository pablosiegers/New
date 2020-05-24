from selenium import webdriver
from time import sleep

class TinderBot():

    #New Terminal
    #py -i tinderbot.py
    #bot = TinderBot()
    #

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')
        sleep(10)
        #Accept politics
        politicas_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        politicas_btn.click()
        
    def login2(self):
        sleep(5)
        #Saving base window 
        base_window = self.driver.window_handles[0]
        #Switching to popup window
        popup = self.driver.switch_to_window(self.driver.window_handles[1])
        #Enter email
        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys('lpabloimvu@gmail.com')
        #Enter password
        password_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        password_in.send_keys('viaje123')
        #Login btn
        login_btn = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')
        login_btn.click()
        #Switch to base window
        self.driver.switch_to_window(base_window)
        sleep(10)
        #Popup permitir ubicacion
        permitir_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        permitir_btn.click()
        #popup notificaciones
        nointeresa_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        nointeresa_btn.click()


    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def auto_swipe(self):
        while True:
            sleep(5)
            try:
                self.like()
            except Exception:
                try:
                    sleep(3)
                    self.close_popup()
                except Exception:
                    sleep(3)
                    self.match()
    
    def close_popup(self):
        nopopup_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        nopopup_btn.click()

    def match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()
    
