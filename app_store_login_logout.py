import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# 浏览器窗口最大化
driver.maximize_window()

# 设置浏览器窗口具体尺寸 x坐标 y坐标 width height
# driver.set_window_rect(200, 0, 1680, 1000)

wait = WebDriverWait(driver, 10)

driver.get("http://appstore.yunlogin.com/home")

show_login_modal = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#__layout > div > header > div > div.sing-in > div.login-btn"))
)
show_login_modal.click()

time.sleep(1)

# 等待输入框 phone 可交互
input_phone = wait.until(EC.element_to_be_clickable((By.ID, "phone")))
input_phone.send_keys("123456")

# 等待输入框 password 可交互
input_password = wait.until(EC.element_to_be_clickable((By.ID, "password")))
input_password.send_keys("111111")

input_password.send_keys(Keys.RETURN)

time.sleep(5)

# 显示下拉
show_select = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#__layout > div > header > div > div.sing-in > div.logined"))
)
show_select.click()

# 退出
log_out = wait.until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#__layout > div > header > div > div.sing-in > div.select > div.logout > a"))
)
log_out.click()

driver.execute_script("alert('退出成功!');")

time.sleep(3)

# 关闭驱动
driver.quit()
