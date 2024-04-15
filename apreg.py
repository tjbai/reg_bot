import sys
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

def parse_args():
    if len(sys.argv) != 4:
        print('Usage: py3 reg.py <yyyy/mm/dd/hh/mm> <username> <password>')
        exit(0)
    
    _, time_str, uname, pw = sys.argv
    reg_time = datetime(*list(map(int, time_str.split('/'))), 0)
    
    return uname, pw, reg_time

def click_button(driver, reg_button):
    reg_button.click()
    print(f'Button clicked at {datetime.now()}')
    driver.quit()

def main():
    uname, pw, reg_time = parse_args()

    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)

    driver.get('https://sis.jhu.edu/sswf/')

    # sign in
    signin_button = driver.find_element(by=By.ID, value='linkSignIn')
    signin_button.click()

    username_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'i0116')))
    username_input.send_keys(uname)
    username_input.send_keys(Keys.RETURN)

    password_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'i0118')))
    password_input.send_keys(pw)
    password_input.send_keys(Keys.RETURN)

    # go to cart
    driver.get(f'https://sis.jhu.edu/sswf/SSS/EnrollmentCart/SSS_EnrollmentCart.aspx')
    select_all = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'SelectAllCheckBox')))
    select_all.click()

    reg_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'ctl00_contentPlaceHolder_ibEnroll')))

    scheduler = BlockingScheduler()
    scheduler.add_job(click_button, 'date', run_date=reg_time, args=[driver, reg_button])

    print(f'Button click scheduled for {reg_time}')
    scheduler.start()

if __name__ == '__main__':
    main()