import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置 ChromeDriver 路径（如果需要）
# driver_path = "C:/WebDriver/bin/chromedriver.exe"  # 适用于 Windows
# driver_path = "/usr/local/bin/chromedriver"  # 适用于 macOS/Linux

# 创建浏览器实例
# driver = webdriver.Chrome(executable_path=driver_path)  # 如果需要设置 ChromeDriver 路径
driver = webdriver.Chrome()  # 如果 ChromeDriver 已添加到系统 PATH

# 打开网站
driver.get("https://www.google.com")

# 在搜索框中输入 "yuanki.cn"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("yuanki.cn")
search_box.send_keys(Keys.RETURN)

# 点击搜索结果的第一个链接
first_result = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#rso > div:nth-child(1) > div > div > div.Z26q7c.UK95Uc.jGGQ5e > div > a"))
)
first_result.click()

# 点击元素 "#aside > div > div.navi-wrap.scroll-y.scroll-hide > nav > ul > li:nth-child(4) > a"
nav_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#aside > div > div.navi-wrap.scroll-y.scroll-hide > nav > ul > li:nth-child(4) > a"))
)
nav_element.click()

# 点击元素 "#post-panel > div > div > div > figure:nth-child(5) > a"
post_element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#post-panel > div > div > div > figure:nth-child(5) > a"))
)
post_element.click()

# 创建一个目录来保存图片
image_directory = "images"
if not os.path.exists(image_directory):
    os.makedirs(image_directory)

# 获取 #md_handsome_origin 下的所有 img 元素（不限于 div 的直接子元素）
images = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#md_handsome_origin img"))
)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/94.0.4606.81 Safari/537.36",
    "Referer": driver.current_url,
}

# 遍历所有 img 元素并保存图片
for index, img in enumerate(images):
    src = img.get_attribute("src")
    if src:
        image_path = os.path.join(image_directory, f"image_{index}.jpg")

        response = requests.get(src, headers=headers, stream=True)
        if response.status_code == 200:
            with open(image_path, "wb") as file:
                for chunk in response.iter_content(8192):
                    file.write(chunk)
        else:
            print(f"Error downloading image {index}: {response.status_code}")

# 注意：请根据需要在代码结束时关闭驱动程序，例如： driver.quit()
