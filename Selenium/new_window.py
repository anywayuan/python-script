from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 启动驱动程序
driver = webdriver.Chrome()
# 打开网址
driver.get("https://seleniumhq.github.io")

# 设置等待
wait = WebDriverWait(driver, 10)

# 存储原始窗口的 ID
original_window = driver.current_window_handle

# 检查一下，我们还没有打开其他的窗口
assert len(driver.window_handles) == 1

# 单击在新窗口中打开的链接
driver.find_element(By.LINK_TEXT, "new window").click()

# 等待新窗口或标签页
wait.until(EC.number_of_windows_to_be(2))

# 循环执行，直到找到一个新的窗口句柄
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

# 等待新标签页完成加载内容
wait.until(EC.title_is("SeleniumHQ Browser Automation"))