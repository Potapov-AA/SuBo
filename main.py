from selenium import webdriver
import time

#Добавление данных google профиля и расположение файла chromedriver.exe
FILE_NAME_PROFILE = r'C:\Users\asus\AppData\Local\Google\Chrome\User Data'
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=" + FILE_NAME_PROFILE)
driver = webdriver.Chrome(executable_path=r"C:\\Users\\chromedriver.exe", options=options)

#Заходим на страницу с нужным товаром
driver.get('https://www.supremenewyork.com/shop/shorts/y3gjn08dp/g79nh82lm')
#Добавляем товар в корзину
driver.find_element_by_name("commit").click()
#Делаем остановку чтобы страница прогрузилась
time.sleep(2)
#Открываем страницу оформления покупки
driver.execute_script("window.open('https://www.supremenewyork.com/checkout', 'new_window')")
#Закрваем текущую страницу
driver.close()
#Переходим на страницу с офрмление покупки
driver.switch_to.window(driver.window_handles[0])
#Автозаполняем поля
driver.find_element_by_id("order_billing_name").send_keys("some text")
driver.find_element_by_id("order_email").send_keys("some text")
driver.find_element_by_id("order_tel").send_keys("some text")
driver.find_element_by_name("order[billing_address]").send_keys("some text")
driver.find_element_by_name("order[billing_address_2]").send_keys("some text")
driver.find_element_by_id("order_billing_address_3").send_keys("some text")
driver.find_element_by_id("order_billing_city").send_keys("some text")
driver.find_element_by_id("order_billing_zip").send_keys("1")





driver.execute_script("window.open('https://www.supremenewyork.com/shop/cart', 'new_window')")

elem = driver.find_elements_by_css_selector(".button.remove")
elem[0].click()