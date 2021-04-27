from selenium import webdriver
import time

# start web browser
# browser = webdriver.Chrome()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')
browser = webdriver.Chrome(options=chrome_options)


def internet(t):
	browser.get("http://gate1.urmia.ac.ir:8090/")

	user = browser.find_element_by_xpath('''//*[@id="username"]''')
	user.send_keys("a.jabbary")

	psw = browser.find_element_by_xpath('''//*[@id="password"]''')
	psw.send_keys("66263674Ax!")

	login = browser.find_element_by_xpath('''//*[@id="loginbutton"]''')
	login.click()

	print("Internet connected seccessfully! -- {}".format(t))

# internet()

minute = 60

for i in range(100):
	internet(i)
	time.sleep(2*minute)