import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

profilefolder = '--user-data-dir=' + 'C:\\Users\\member\\AppData\\Local\\Google\\Chrome\\User Data\\Default'
options = webdriver.ChromeOptions()
options.add_argument(profilefolder)
driver = webdriver.Chrome(
    executable_path = 'C:\\Users\\member\\Desktop\\slideBrowser\\chromedriver.exe',
    options = options
)

url = "https://docs.google.com/document/d/15np149VBy_hrHiiDk-_7zMdWziNIr7k_rs19oIQoae8/edit"
driver.get(url)
time.sleep(5)

element = driver.find_element_by_id("lst-ib")
time.sleep(3)
element.send_keys("入力テスト")
element.send_keys(Keys.CONTROL,Keys.SHIFT,"s")