from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")

print(f"Заголовок страницы: {driver.title}")
print(f"Текущий URL: {driver.current_url}")

driver.quit()