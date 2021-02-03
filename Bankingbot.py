from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time

PATH = "/Users/joeltaban/Desktop/Python/chromedriver"

date_price = []
category = []

class BankBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(PATH)
        self.driver.maximize_window() 
        self.driver.implicitly_wait(60)
        self.driver.get("https://secure.bankofamerica.com/login/sign-in/signOnV2Screen.go")
        self.driver.find_element_by_name("dummy-onlineId").send_keys(username)
        self.driver.find_element_by_name("dummy-passcode").send_keys(password)
        self.driver.find_element_by_class_name("btn-bofa-blue-lock").click()
    
    def get_account_name(self, account_name):
        account_name = self.driver.find_element_by_link_text(account_name)
        account_name.click()
    
    def get_date(self, date):
        transction_search = self.driver.find_element_by_id("transaction-search-input")
        transction_search.clear()
        transction_search.send_keys(date)
        transction_search.send_keys(Keys.RETURN)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        self.driver.implicitly_wait(5)

    def get_transactions(self):
        try:
            rows = len(self.driver.find_elements_by_xpath("/html/body/div[1]/div/div[4]/div[1]/div/table/tbody/tr"))
    
            actual = rows - 3
            if actual == 3:
                actual += 1
            plus = (actual-1) * 2
            rows = actual + plus
    
            numb = 6
            even_tag = 4
     
            for row in range(3, rows, 2):
                try:
                    line = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[1]/div/table/tbody/tr["+str(row)+"]").text
                    #print(line)
                    date_price.append(line)
                    drop = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[1]/div/table/tbody/tr["+str(row)+"]/td[2]/div/a[1]/span[3]").click()
                    #drop.click()
                    try:
                        parent = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[1]/div/table/tbody/tr["+str(even_tag)+"]/td[2]/dl/dd[6]/span/span[2]").text
                        #print(parent)
                        category.append(parent)
                    except:
                        parent = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[1]/div/table/tbody/tr["+str(even_tag)+"]/td[2]/dl/dd[9]/span/span[2]").text
                        #print(parent)
                        category.append(parent)
                    drop.click()
                    #row += 2

                except:
                    try:
                        if row == numb:
                            line = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[1]/div/table/tbody/tr["+str(numb)+"]").text
                            #print(line)
                            date_price.append(line)
                            drop = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[1]/div/table/tbody/tr["+str(numb)+"]/td[2]/div/a[1]/span[3]").click()
                            #drop.click()
                            child = self.driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[1]/div/table/tbody/tr["+str(numb+1)+"]/td[2]/dl/dd[9]/span/span[2]").text
                            #print(child)
                            category.append(child)
                            drop.click()
                            numb += 2
                        else:
                           pass
                    except:
                        pass
                        
                finally:
                    pass
        
                even_tag += 2
                
            self.driver.implicitly_wait(5)
 
        finally:
            time.sleep(5)
            self.driver.quit()



