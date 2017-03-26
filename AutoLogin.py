import requests, time, sys
from datetime import datetime
from lxml import html
from selenium import webdriver
 
CHOICE = -1
url_github = 'https://github.com/login'
url_gmail  = 'https://accounts.google.com/ServiceLogin#identifier'
url_facebook = 'https://en-gb.facebook.com/login/'
class AutoLogin(object):
        
        def __init__(self,login):
                self.username = login[0]
                self.password = login[1]
        
        def schedule(self,Time):
                self.setTime = Time
        
        def get_username(self):
                return self.username
        
        def get_password(self):
                return self.password
        
        def process_selenium_github(self):
                try :           
                        browser = webdriver.Chrome()    # Check.
                        browser.get(url_github)
                        time.sleep(3)
                        ID = browser.find_element_by_id('login_field')          
                        ID.send_keys(self.get_username())
                        PASS = browser.find_element_by_id('password')           
                        PASS.send_keys(self.get_password())
                        PASS.submit()
                except:
                        print 'Error Logging in...'
        def process_selenium_gmail(self):
                try :           
                        browser = webdriver.Chrome()    # Check.
                        browser.get(url_gmail)
                        time.sleep(3)
                        loginEmail = browser.find_element_by_id('Email')
                        loginEmail.send_keys(mail)
                        Next = browser.find_element_by_id('next')
                        Next.click()
                        time.sleep(3)
                        loginPassword = browser.find_element_by_id('Passwd')
                        loginPassword.send_keys(password)
                        signin = browser.find_element_by_id('signIn')
                        signin.click()
                except:
                        print 'Error Logging in...'
                                
        def process_selenium_facebook(self):
                try :           
                        browser = webdriver.Chrome()    # Check.
                        browser.get(url_facebook)
                        ID = browser.find_element_by_id('email')          
                        ID.send_keys(self.get_username())
                        PASS = browser.find_element_by_id('pass')           
                        PASS.send_keys(self.get_password())
                        signin = browser.find_element_by_id('loginbutton')
                        signin.click()
                except:
                        print 'Error Logging in...'
       
        def process(self):              
                payload = {
                        'login'   : self.get_username(),
                        'password': self.get_password(),
                          }
                with requests.session() as s:
                        result = s.post(url,data = payload)
                        print result.content                    
                return True
        
        def Login(self):
                while True:
                        now = datetime.now()
                        now = now.strftime("%H:%M")
                        print 'Current Time:',now
                        if self.setTime <= now:
                                if CHOICE == '1':
                                        self.process_selenium_facebook()
                                elif CHOICE == '2':
                                        self.process_selenium_github()
                                elif CHOICE == '3':
                                        self.process_selenium_gmail()
                                print 'Login Completed!'
                                return
                        else:
                                time.sleep(10)   #Sleep for 1 Second.
                                                
def main():
        global CHOICE
        while CHOICE not in ['1','2','3']:
                CHOICE   = raw_input("Login to :\n1. Facebook\n2. Github\n3. Gmail\n>>> ")
        username = raw_input("Enter Username: ")
        password = raw_input("Enter Password: ")
        auto_login = AutoLogin((username,password))
        while True:
                try:
                        Time = datetime.strptime(raw_input("Enter Scheduled Login Time(HH:MM): "),"%H:%M")
                        break
                except ValueError:
                        print "Enter in Correct Format (HH : MM)"
        Time = Time.strftime("%H:%M")
        auto_login.schedule(Time)
        auto_login.Login()
        #auto_login.process()
                
if __name__ == "__main__":
        main()
