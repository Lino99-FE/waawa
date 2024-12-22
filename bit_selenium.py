from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from bit_api import *
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_helper import *

# /browser/open 接口会返回 selenium使用的http地址，以及webdriver的path，直接使用即可
def initBrowser(bId):
    res = openBrowser(bId)  # 窗口ID从窗口配置界面中复制，或者api创建后返回

    print(res)

    if res['success']:
        driverPath = res['data']['driver']
        debuggerAddress = res['data']['http']

        # selenium 连接代码
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("debuggerAddress", debuggerAddress)

        chrome_service = Service(driverPath)
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

        # 以下为PC模式下，打开baidu，输入 BitBrowser，点击搜索的案例
        driver.get('https://app.griffinai.io/en/main/playground')

        # input = driver.find_element(By.CSS_SELECTOR, 's_ipt')
        # input.send_keys('BitBrowser')
        WebDriverWait(driver, 30).until(
            lambda _: driver.find_element(By.XPATH, '//button[text()="Check it out now!"]')
        )

        btnList = driver.find_elements(By.XPATH, '//button[text()="Check it out now!"]')
        # print('捕捉到按钮数量：'+len(btnList))
        # debugger(driver)
        btnList[0].click()
        # debugger(driver)

        # driver.quit()

        print('after click')
    else:
        print('请求结果无效')