#1
# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
#
# options = Options()
# options.add_argument("--start-maximized")
#
# driver = webdriver.Chrome(options=options)
#
# try:
#     driver.get("https://www.saucedemo.com")
#     print(f"Заголовок страницы: {driver.title}")
#     print(f"Текущий URL: {driver.current_url}")
#     time.sleep(3)
# finally:
#     driver.quit()


#2
# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
#
# options = Options()
# options.add_argument("--start-maximized")
#
# driver = webdriver.Chrome(options=options)
#
# try:
#     driver.get("https://www.saucedemo.com")
#     if 'login' in driver.page_source:
#         print('Слово "login" найдено в коде страниц')
#     else:
#         print('Не найдено')
#     time.sleep(3)
# finally:
#     driver.quit()

#3
# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
#
# options = Options()
# options.add_argument("--start-maximized")
#
# driver = webdriver.Chrome(options=options)
#
# try:
#     driver.get("https://www.saucedemo.com")
#     print(f"Заголовок страницы: {driver.title}")
#     driver.get("https://obrazavr.ru/cards/")
#     print(f"Заголовок страницы: {driver.title}")
#     driver.get("https://metanit.com/")
#     print(f"Заголовок страницы: {driver.title}")
#     time.sleep(3)
# finally:
#     driver.quit()