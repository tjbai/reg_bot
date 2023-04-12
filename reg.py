import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def run():
    desired_reg_time = input('REG TIME YYYY/MM/DD/HH/MM: ')
    reg_time_arr = desired_reg_time.split('/')
    pause_time = datetime.datetime(
        int(reg_time_arr[0]),
        int(reg_time_arr[1]),
        int(reg_time_arr[2]),
        int(reg_time_arr[3]),
        int(reg_time_arr[4]),
        0
    )

    USERNAME = input('SIS USER: ')
    PASSWORD = input('SIS PW: ')

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(
        ChromeDriverManager().install(),
        chrome_options=chrome_options
    )
    driver.get('https://sis.jhu.edu/sswf/')

    signin_button = driver.find_element(by=By.ID, value='linkSignIn')
    signin_button.click()

    username_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'i0116')))
    username_input.send_keys(USERNAME)
    username_input.send_keys(Keys.RETURN)

    password_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'i0118')))
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)

    driver.get(f'https://sis.jhu.edu/sswf/SSS/EnrollmentCart/SSS_EnrollmentCart.aspx')

    select_all = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'SelectAllCheckBox')))
    select_all.click()

    reg_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'ctl00_contentPlaceHolder_ibEnroll')))

    print('waiting...')
    while True:
        current_time = datetime.datetime.now()
        if current_time >= pause_time:
            reg_button.click()
            print(f'REGISTRATION ATTEMPTED AT {datetime.datetime.now()}')
            break
        time.sleep(0.005)


if __name__ == '__main__': run()
