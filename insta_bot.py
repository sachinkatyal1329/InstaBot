from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time
import random
import database as db

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path = '../Insta_Bot/chromedriver')

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(1)
        login_button = driver.find_element_by_xpath("//a[starts-with(@href, '/accounts/login')]")
        login_button.click()

        time.sleep(1)
        username_elem = driver.find_element_by_xpath("//input[@name= 'username']")
        username_elem.send_keys(self.username)

        password_elem = driver.find_element_by_xpath("//input[@name= 'password']")
        password_elem.send_keys(self.password)

        login_button = driver.find_element_by_xpath("//button[@type= 'submit']")
        login_button.click()

        time.sleep(1)
        not_now_butt = driver.find_element_by_xpath("//button[text()='Not Now']")
        not_now_butt.click()

    def signUp(self):
        file_handler = db.FileHandler("names.txt", "usernames.txt")
        rand_name = file_handler.get_rand_name()
        rand_username = file_handler.get_rand_username()
        rand_password = file_handler.get_rand_password()


        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(1)
        input_field = driver.find_element_by_xpath("//input[@name= 'emailOrPhone']")
        input_field.send_keys(rand_username + "@gmail.com")

        input_field = driver.find_element_by_xpath("//input[@name= 'fullName']")
        input_field.send_keys(rand_name)

        input_field = driver.find_element_by_xpath("//input[@name = 'username']")
        input_field.send_keys(rand_username)

        input_field = driver.find_element_by_xpath("//input[@name = 'password']")
        input_field.send_keys(rand_password)

        button = driver.find_element_by_xpath("//button[@type = 'submit']")
        button.click()

        #ssfErrorAlert
        self.login_()

        
    def login_(self):
        driver = self.driver
        try:
            text = driver.find_element_by_xpath("//p[@id = 'ssfErrorAlert']")
            time.sleep(1)
            not_now_butt = driver.find_element_by_xpath("//button[text()='Not Now']")
            not_now_butt.click()

        except:
            text = driver.find_element_by_xpath("//p[@id = 'ssfErrorAlert']")
            
            #self.signUp()

ig = InstagramBot("sachinawesomeguy", "Randolph2019")
ig.signUp()


#records = db.Database("Instagram Bots")
#records.print_records()

#ig = InstagramBot("sachinawesomeguy", "Randolph2019")
#ig.login()

#href="/accounts/login/?source=auth_switcher"
# "//a[@href'accounts/login']"
# "//input[@name'username']"
#"//input[@name'passowrd']"
