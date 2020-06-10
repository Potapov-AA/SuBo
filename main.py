from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time



#Добавление данных google профиля и расположение файла chromedriver.exe
FILE_NAME_PROFILE = r'C:\Users\asus\AppData\Local\Google\Chrome\User Data'
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=" + FILE_NAME_PROFILE)
driver = webdriver.Chrome(executable_path=r"C:\\Users\\chromedriver.exe", options=options)

#Заходим на страницу с нужным товаром
driver.get('https://www.supremenewyork.com/shop/shorts/y3gjn08dp/g79nh82lm')

####################################
#############TEST ZONE##############
####################################
time.sleep(2)
test_input = 1
while test_input == 1:
    time.sleep(2)
    driver.refresh()
    test_input = int(input("test_input = "))
####################################
####################################

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
#Автозаполнение полей
#Данные пользователя и доставка
driver.find_element_by_id("order_billing_name").send_keys("P")#full name
driver.find_element_by_id("order_email").send_keys("Sa")#email
driver.find_element_by_id("order_tel").send_keys("8922")#tel
driver.find_element_by_name("order[billing_address]").send_keys("U")#addres
driver.find_element_by_name("order[billing_address_2]").send_keys("")#addres_2
driver.find_element_by_id("order_billing_address_3").send_keys("G. SANKT-PETERBURG")#addres_3
driver.find_element_by_id("order_billing_city").send_keys("G. SANKT-PETERBURG")#sity
driver.find_element_by_id("order_billing_zip").send_keys("")#index
Select(driver.find_element_by_id("order_billing_country")).select_by_visible_text('RUSSIA')
Select(driver.find_element_by_id("credit_card_type")).select_by_visible_text('')
driver.find_element_by_id("cnb").send_keys("")
driver.find_element_by_id("vval").send_keys("")

driver.find_elements_by_class_name("icheckbox_minimal")[1].click()

driver.find_element_by_name("commit").click()




temp_test = int(input("Введи 1, чтобы продолжить: "))
if temp_test == 1:
    driver.execute_script("window.open('https://www.supremenewyork.com/shop/cart', 'new_window')")

    driver.find_elements_by_css_selector(".button.remove")[0].click()

