from selenium import webdriver
import time

def web (username, password):

    driver.get("https://www.instagram.com/")
    time.sleep(1)
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_xpath('//*[@id="loginForm"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    time.sleep(3)
    login(username)

def login (username):
    driver.get(f"https://www.instagram.com/{username}")
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]').click()
    # driver.find_element_by_xpath('//*[@id="f2ee7f18ebbcae8"]/div/div/div').click()
    time.sleep(3)
    unfollow()

def unfollow():
    for i in range(10):
        driver.find_element_by_xpath('//button[text()="Following"]').click()
        time.sleep(2)
        # for j in range(i):
        driver.find_element_by_xpath('//button[text()="Unfollow"]').click()
        time.sleep(2)
    driver.refresh()
    login()

if __name__ == '__main__':
    print('github : https://github.com/Anasg4')
    user = input("Input your Username: ")
    pas = input("Input your password: ")
    # change to yours chromedriver location
    driver = webdriver.Chrome(executable_path="C:/Users/Anas/Downloads/chromedriver")
    web(user, pas)
